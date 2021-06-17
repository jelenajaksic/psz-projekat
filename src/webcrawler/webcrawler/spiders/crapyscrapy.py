import scrapy
from ..items import *


class CrapyScrapy(scrapy.Spider):
    name = "CrapyScrapy"
    start_urls = [
        'https://www.nekretnine.rs/stambeni-objekti/stanovi/izdavanje-prodaja/prodaja/lista/po-stranici/20/',
        # 'https://www.nekretnine.rs/stambeni-objekti/stanovi/izdavanje-prodaja/izdavanje/lista/po-stranici/20/',
        # 'https://www.nekretnine.rs/stambeni-objekti/kuce/izdavanje-prodaja/prodaja/lista/po-stranici/20/',
        # 'https://www.nekretnine.rs/stambeni-objekti/kuce/izdavanje-prodaja/izdavanje/lista/po-stranici/20/'
        # 'https://www.nekretnine.rs/stambeni-objekti/stanovi/izdavanje-prodaja/izdavanje/lista/po-stranici/10/',
        # 'https://www.4zida.rs/prodaja-stanova'
    ]

    def parse(self, response):
        # album_links_on_page = self.get_albums_on_page(response)
        # for album_link in album_links_on_page:
        #     yield response.follow(album_link, callback=self.parse_album)

        props_on_page = self.get_properties_on_page(response)
        for prop_page in props_on_page:
            yield response.follow(prop_page, callback=self.parse_prop)

        next_page = response.css("a.next-article-button::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def get_properties_on_page(self, response):
        prop_links = [link.get() for link in response.css("h2 a::attr(href)")]
        return prop_links

    def get_location(self, response):
        # print(response.css("div.property__location ul"))
        return response.css("div.property__location ul li:nth-child(3)::text").get()

    def govno(self, tag, pat):
        for li in tag:
            if li.css("li::text").get().strip() == pat:
                return tag.index(li)+1

        return -1

    def get_details(self, response):
        details_tag = response.css(
            "section#detalji div.property__amenities")[0]

        add_type_index = self.govno(details_tag.css("ul li"), "Transakcija:")
        add_type = details_tag.css("ul li:nth-child({}) strong::text".format(
            add_type_index)).get().strip() if add_type_index > -1 else None

        size_index = self.govno(details_tag.css("ul li"), "Kvadratura:")
        size = float(details_tag.css("ul li:nth-child({}) strong::text".format(
            size_index)).get().strip().split(" ")[0]) if size_index > -1 else None

        year_index = self.govno(details_tag.css("ul li"), "Godina izgradnje:")
        year = int(details_tag.css("ul li:nth-child({}) strong::text".format(year_index)
                                   ).get().strip()) if year_index > -1 else None

        rooms_index = self.govno(details_tag.css("ul li"), "Ukupan broj soba:")
        rooms = float(details_tag.css("ul li:nth-child({}) strong::text".format(
            rooms_index)).get().strip()) if rooms_index > -1 else None

        toiletes_index = self.govno(details_tag.css("ul li"), "Broj kupatila:")
        toiletes = int(details_tag.css("ul li:nth-child({}) strong::text".format(
            toiletes_index)).get().strip()) if toiletes_index > -1 else None

        storey_index = self.govno(details_tag.css("ul li"), "Spratnost:")
        storey = details_tag.css("ul li:nth-child({}) strong::text".format(
            storey_index)).get().strip() if storey_index > -1 else None
        if storey == 'Prizemlje' or storey == 'Visoko prizemlje':
            storey = 0
        if storey == 'Suteren':
            storey = -1
        if storey != None:
            storey = int(storey)

        total_storeys_index = self.govno(
            details_tag.css("ul li"), "Ukupan broj spratova:")
        total_storeys = int(details_tag.css("ul li:nth-child({}) strong::text".format(
            total_storeys_index)).get().strip()) if total_storeys_index > -1 else None

        registered_index = self.govno(details_tag.css("ul li"), "Uknjiženo:")
        registered = details_tag.css("ul li:nth-child({}) strong::text".format(
            registered_index)).get().strip() if registered_index > -1 else None
        if registered != None:
            registered = True if registered == 'Da' else False
        return add_type, size, year, rooms, toiletes, storey, total_storeys, registered

    def get_price(self, response):
        price = response.css("h4.stickyBox__price::text").get()
        if len(price) > 1:
            price = price.split(" ")[:-2]
            price = ("").join(price)
            price = float(price)

        return price

    def get_heat_parking(self, response):
        main_tag = response.css("div.property__main-details ul li")
        heat = main_tag[2].css("li span::text").extract()[1]
        parking = main_tag[3].css("li span::text").extract()[1]
        parking = True if parking == 'Da' else False
        return heat, parking

    def parse_prop(self, response):
        item = WebcrawlerItem()
        prop_type = 'a' if response.url.split("/")[-4] == 'stanovi' else 'h'
        location = self.get_location(response)
        add_type, size, year, rooms, toiletes, storey, total_storeys, registered = self.get_details(
            response)
        price = self.get_price(response)
        heat_type, parking = self.get_heat_parking(response)
        other = ''
        # print(prop_type, location, add_type,size,year,rooms,toiletes,storey,total_storeys,registered, price)
        # print(heat_type, parking)

        item["url"] = response.url
        item["property_type"] = prop_type
        item["location"] = location
        item["add_type"] = add_type
        item["size"] = size
        item["year"] = year
        item["rooms"] = rooms
        item["toiletes"] = toiletes
        item["storey"] = storey
        item["total_storeys"] = total_storeys
        item["registered"] = registered
        item["price"] = price
        item["other"] = other
        item["area"] = None
        item["heat_type"] = heat_type
        item["parking"] = parking

        yield item