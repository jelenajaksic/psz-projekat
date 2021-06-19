SELECT MAX(id) FROM db.realestate

select count(*) from db.realestate where add_type = 's'

select count(*) from db.realestate where add_type='r'

select location, COUNT(*) from db.realestate where add_type = 's' group by location 



select registered, count(*) from db.realestate where property_type = 'a' group by registered 

select registered, count(*) from db.realestate where property_type = 'h' group by registered 



select location, price, url from db.realestate where property_type='a' order by price desc limit 30

select location, price, url from db.realestate where property_type='h' order by price desc limit 30



select location, size, url from db.realestate where property_type='a' order by size desc limit 100

select location, size, url from db.realestate where property_type='h' order by size desc limit 100


select location, property_type, price, url from db.realestate where add_type='r' and year=2020 order by price desc

select location, property_type, price, url from db.realestate where add_type='s' and year=2020 order by price desc


select location, rooms, url from db.realestate order by rooms desc limit 30

select location, size, url from db.realestate where property_type='a' order by size desc limit 30

select location, area, url from db.realestate where property_type='h' order by area desc limit 30

