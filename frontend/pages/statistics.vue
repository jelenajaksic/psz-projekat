<template>
  <div>
    <v-row justify="center" align="center">
      <v-col cols="6">
        <v-card color="accent" :elevation="0">
          <v-row class="ma-0">
            <v-col cols="8">
              <v-list-item two-line class="mt-8">
                <v-list-item-content>
                  <v-list-item-title class="headline mb-1 white--text">
                    <strong>{{ sellCount.toLocaleString() }}</strong>
                  </v-list-item-title>
                  <v-list-item-subtitle class="white--text"
                    >Number of properties for sale</v-list-item-subtitle
                  >
                </v-list-item-content>
              </v-list-item>
            </v-col>
            <v-col cols="4">
              <v-avatar size="100" class="my-2" tile>
                <span class="sell-icon" />
              </v-avatar>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
      <v-col cols="6">
        <v-card color="accent" :elevation="0">
          <v-row class="ma-0">
            <v-col cols="8">
              <v-list-item two-line class="mt-8">
                <v-list-item-content>
                  <v-list-item-title class="headline mb-1 white--text">
                    <strong>{{ rentCount.toLocaleString() }}</strong>
                  </v-list-item-title>
                  <v-list-item-subtitle class="white--text"
                    >Number of properties for rent</v-list-item-subtitle
                  >
                </v-list-item-content>
              </v-list-item>
            </v-col>
            <v-col cols="4">
              <v-avatar size="100" class="my-2" tile>
                <span class="rent-icon" />
              </v-avatar>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
    <!-- <v-row justify="center" align="center"> -->
    <registered :item="houseRegistration" type="houses" />
    <!-- </v-row>
    <v-row justify="center" align="center"> -->
    <registered :item="apartmentsRegistration" type="apartments" />
    <!-- </v-row> -->
    <v-row justify="center" align="center">
      <v-col cols="12" md="6">
        <v-card :elevation="0">
          <v-card-title class="headline">
            Top 30 houses houses for sell by price
          </v-card-title>
          <v-card-text>
            <top-30 :items="top30houses" />
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="12" md="6">
        <v-card :elevation="0">
          <v-card-title class="headline">
            Top 30 apartments for sell by price
          </v-card-title>
          <v-card-text>
            <top-30 :items="top30apartments" />
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <v-row justify="center" align="center">
      <v-col cols="12">
        <top-100
          :top-apartments="top100apartments"
          :top-houses="top100houses"
        />
      </v-col>
    </v-row>
    <v-row justify="center" align="center">
      <v-col cols="12">
        <sell-rent-2020 :sell="sell2020" :rent="rent2020" />
      </v-col>
    </v-row>
    <v-row justify="center" align="center">
      <v-col cols="12" md="6">
        <v-card :elevation="0">
          <v-card-title class="headline">
            Top 30 properties sorted by number of rooms
          </v-card-title>
          <v-card-text>
            <top-30-rooms :items="top30rooms" />
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="12" md="6">
        <v-card :elevation="0">
          <v-card-title class="headline">
            Top 30 houses sorted by area
          </v-card-title>
          <v-card-text>
            <top-30-area :items="top30area" />
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <v-row justify="center" align="center">
      <v-col cols="12">
        <v-card :elevation="0">
          <v-card-title class="headline">
            Number of properties for sale in each city
          </v-card-title>
          <v-card-text>
            <count-by-location :items="countByLocation" />
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import CountByLocation from '../components/CountByLocation.vue'
import Registered from '../components/Registered.vue'
import SellRent2020 from '../components/SellRent2020.vue'
import Top100 from '../components/Top100.vue'
import Top30 from '../components/Top30.vue'
import Top30Area from '../components/Top30Area.vue'
import Top30Rooms from '../components/Top30Rooms.vue'
export default {
  components: {
    CountByLocation,
    Registered,
    Top30,
    Top100,
    SellRent2020,
    Top30Rooms,
    Top30Area,
  },
  async asyncData({ $axios }) {
    const [one, two, three, four, five, six, seven] = await Promise.all([
      $axios.get('/num_of_properties'),
      $axios.get('/num_of_sell_by_city'),
      $axios.get('/registration_count'),
      $axios.get('/top30'),
      $axios.get('/top100'),
      $axios.get('/2020'),
      $axios.get('/top30_rooms_area'),
    ])
    return {
      sellCount: one.data.sell,
      rentCount: one.data.rent,
      allCount: one.data.all,
      countByLocation: two.data,
      houseRegistration: three.data.houses,
      apartmentsRegistration: three.data.apartments,
      top30houses: four.data.houses,
      top30apartments: four.data.apartments,
      top100houses: five.data.houses,
      top100apartments: five.data.apartments,
      sell2020: six.data.sell,
      rent2020: six.data.rent,
      top30rooms: seven.data.rooms,
      top30area: seven.data.area,
    }
  },
}
</script>

<style scoped>
.sell-icon {
  mask: url('~/assets/sale1.svg');
  height: 100px;
  width: 100px;
  mask-size: contain;
  background: white;
}

.rent-icon {
  mask: url('~/assets/rent1.svg');
  height: 100px;
  width: 100px;
  mask-size: contain;
  background: white;
}
</style>
>
