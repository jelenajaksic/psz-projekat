<template>
  <v-row justify="center" align="center">
    <v-col cols="6">
      <v-card color="cyan darken-1" :elevation="0">
        <v-row class="ma-0">
          <v-col cols="8">
            <v-list-item two-line class="mt-8">
              <v-list-item-content>
                <v-list-item-title class="headline mb-1 white--text">
                  {{ sellCount.toLocaleString() }}
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
      <v-card color="cyan darken-1" :elevation="0">
        <v-row class="ma-0">
          <v-col cols="8">
            <v-list-item two-line class="mt-8">
              <v-list-item-content>
                <v-list-item-title class="headline mb-1 white--text">
                  {{ rentCount.toLocaleString() }}
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
    <registered :item="houseRegistration" type="houses" />
    <registered :item="houseRegistration" type="apartments" />
    <v-col cols="12">
      <v-card :elevation="0">
        <v-card-title>
          Number of properties for sale in each city
        </v-card-title>
        <v-card-text>
          <count-by-location :items="countByLocation" />
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import CountByLocation from '../components/CountByLocation.vue'
import Registered from '../components/Registered.vue'
export default {
  components: { CountByLocation, Registered },
  async asyncData({ $axios }) {
    const [one, two, three] = await Promise.all([
      $axios.get('/num_of_properties'),
      $axios.get('/num_of_sell_by_city'),
      $axios.get('/registration_count'),
    ])
    return {
      sellCount: one.data.sell,
      rentCount: one.data.rent,
      allCount: one.data.all,
      countByLocation: two.data,
      houseRegistration: three.data.houses,
      apartmentsRegistration: three.data.apartments,
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
