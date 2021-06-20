<template>
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
    <v-col cols="12" lg="4">
      <v-card class="elevation-0">
        <v-card-title class="headline">Count by size</v-card-title>
        <v-card-text>
          <bar-chart :series="countBySize" :categories="sizeCategories" />
        </v-card-text>
      </v-card>
    </v-col>
    <v-col cols="12" lg="4">
      <v-card class="elevation-0">
        <v-card-title class="headline">Count by year</v-card-title>
        <v-card-text>
          <bar-chart :series="countByYear" :categories="yearCategories" />
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import BarChart from '../components/BarChart.vue'
import FullDonut from '../components/FullDonut.vue'
// import MostCommon from '../components/MostCommon.vue'
export default {
  components: { BarChart, FullDonut },
  async asyncData({ $axios }) {
    const [one, two, three] = await Promise.all([
      $axios.get('/most_common'),
      $axios.get('/count_props_by_size'),
      $axios.get('/count_props_by_year'),
    ])
    return {
      commonSellLabels: one.data.sell.labels,
      commonSellData: one.data.sell.data,
      commonRentLabels: one.data.rent.labels,
      commonRentData: one.data.rent.data,
      commonAllLabels: one.data.all.labels,
      commonAllData: one.data.all.data,
      countBySize: [
        {
          data: two.data,
        },
      ],
      countByYear: [
        {
          data: three.data,
        },
      ],
    }
  },
  data() {
    return {
      realestate: [],
      commonSell: [],
      commonRent: [],
      commonAll: [],
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
    }
  },
}
</script>
