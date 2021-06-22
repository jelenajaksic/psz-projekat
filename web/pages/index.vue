<template>
  <div>
    <v-row justify="center" align="center">
      <v-col cols="12" lg="4">
        <v-card class="elevation-0">
          <v-card-title class="headline"> Most common in BGD</v-card-title>
          <v-card-text he>
            <full-donut :series="commonAllData" :labels="commonAllLabels" />
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="12" lg="4">
        <v-card class="elevation-0">
          <v-card-title class="headline"> Most common sell in BGD</v-card-title>
          <v-card-text>
            <full-donut :series="commonSellData" :labels="commonSellLabels" />
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="12" lg="4">
        <v-card class="elevation-0">
          <v-card-title class="headline"> Most common rent in BGD</v-card-title>
          <v-card-text>
            <full-donut :series="commonRentData" :labels="commonRentLabels" />
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <v-row justify="center" align="center">
      <v-col cols="12" lg="5">
        <v-card class="elevation-0">
          <v-card-title class="headline">Count by size</v-card-title>
          <v-card-text>
            <bar-chart :series="countBySize" :categories="sizeCategories" />
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="12" lg="5">
        <v-card class="elevation-0">
          <v-card-title class="headline">Count by year</v-card-title>
          <v-card-text>
            <bar-chart :series="countByYear" :categories="yearCategories" />
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <v-row justify="center" align="center">
      <v-col
        v-for="item in sellRentRatio"
        :key="item.location"
        cols="12"
        lg="4"
      >
        <v-card class="elevation-0">
          <v-card-title class="headline">
            Sell / Rent Ratio for {{ item.location }}
          </v-card-title>
          <v-card-text>
            <simple-donut
              :series="[item.sell, item.rent]"
              :labels="['Sell', 'Rent']"
              :display-total="true"
            />
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <v-row justify="center" align="center">
      <v-col cols="12" lg="4">
        <v-card class="elevation-0">
          <v-card-title class="headline">Count by price</v-card-title>
          <v-card-text>
            <bar-chart :series="countByPrice" :categories="priceCategories" />
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <v-row justify="center" align="center">
      <v-col cols="12" lg="4">
        <v-card class="elevation-0">
          <v-card-title class="headline">
            With / Without parking ratio for Beograd
          </v-card-title>
          <v-card-text>
            <simple-donut
              :series="parkingData"
              :labels="['With Parking', 'Total']"
              :display-total="false"
            />
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import BarChart from '../components/BarChart.vue'
import FullDonut from '../components/FullDonut.vue'
import SimpleDonut from '../components/SimpleDonut'
// import MostCommon from '../components/MostCommon.vue'
export default {
  components: { BarChart, FullDonut, SimpleDonut },
  async asyncData({ $axios }) {
    const [one, two, three, four, five, six] = await Promise.all([
      $axios.get('/most_common'),
      $axios.get('/count_props_by_size'),
      $axios.get('/count_props_by_year'),
      $axios.get('/sell_rent_ratio'),
      $axios.get('/count_props_by_price_category'),
      $axios.get('/num_of_properties_with_parking'),
    ])
    console.log(six.data.parking)
    return {
      commonSellLabels: one.data.sell.labels,
      commonSellData: one.data.sell.data,
      commonRentLabels: one.data.rent.labels,
      commonRentData: one.data.rent.data,
      commonAllLabels: one.data.all.labels,
      commonAllData: one.data.all.data,
      countBySize: [
        {
          name: 'Number of properties',
          data: two.data,
        },
      ],
      countByYear: [
        {
          name: 'Number of properties',
          data: three.data,
        },
      ],
      sellRentRatio: four.data,
      countByPrice: [
        {
          name: 'Number of properties',
          data: five.data,
        },
      ],
      parkingData: six.data.parking,
    }
  },
  data() {
    return {
      realestate: [],
      commonSell: [],
      commonRent: [],
      commonAll: [],
      sellRentRatio: [],
      sizeCategories: [
        'Less than 35',
        '36 - 50',
        '51 - 65',
        '66 - 80',
        '81 - 95',
        '96 - 110',
        'More than 110',
        'No size data',
      ],
      yearCategories: [
        'Before 1951',
        '1951 - 1960',
        '1961 - 1970',
        '1971 - 1980',
        '1981 - 1990',
        '1991 - 2000',
        '2001 - 2010',
        '2011 - 2020',
        'Aftrer 2021',
      ],
      priceCategories: [
        'Less then 49,999',
        '50,000 - 99,999',
        '100,000 - 149,999',
        '150,000 - 199,999',
        'Greater then 200,000',
      ],
    }
  },
}
</script>
