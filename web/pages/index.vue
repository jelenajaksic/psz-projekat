<template>
  <v-row justify="center" align="center">
    <v-col cols="12" lg="4">
      <v-card class="elevation-0">
        <v-card-title class="headline"> Most common in BGD</v-card-title>
        <v-card-text>
          <most-common :items="commonAll" />
        </v-card-text>
      </v-card>
    </v-col>
    <v-col cols="12" lg="4">
      <v-card class="elevation-0">
        <v-card-title class="headline"> Most common sell in BGD</v-card-title>
        <v-card-text>
          <most-common :items="commonSell" />
        </v-card-text>
      </v-card>
    </v-col>
    <v-col cols="12" lg="4">
      <v-card class="elevation-0">
        <v-card-title class="headline"> Most common rent in BGD</v-card-title>
        <v-card-text>
          <most-common :items="commonRent" />
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
    <v-col cols="12">
      <v-card class="elevation-0">
        <v-card-title class="headline"> Realestate </v-card-title>
        <v-card-text>
          <v-data-table
            :headers="headers"
            :items="realestate"
            :items-per-page="5"
            class="elevation-0"
          />
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import BarChart from '../components/BarChart.vue'
import MostCommon from '../components/MostCommon.vue'
export default {
  components: { MostCommon, BarChart },
  async asyncData({ $axios }) {
    const [one, two, three] = await Promise.all([
      $axios.get('/most_common'),
      $axios.get('/count_props_by_size'),
      $axios.get('/count_props_by_year'),
    ])

    return {
      commonSell: one.data.sell,
      commonRent: one.data.rent,
      commonAll: one.data.all,
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
      headers: [
        { text: 'Location', value: 'location' },
        { text: 'URL', value: 'url' },
        { text: 'Add Type', value: 'add_type' },
        { text: 'Property Type', value: 'property_type' },
      ],
    }
  },
}
</script>
