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
        <v-card-title class="headline"> Most common rent in BGD</v-card-title>
        <v-card-text>
          <count-size :series="series" />
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
import CountSize from '../components/CountSize.vue'
import MostCommon from '../components/MostCommon.vue'
export default {
  components: { MostCommon, CountSize },
  async asyncData({ $axios }) {
    // const data = app.$axios.get(`/most_common`)
    // console.log(data)
    // return {
    //   commonSell: data.sell,
    //   commonRent: data.rent,
    //   commonAll: data.all,
    // }
    const [one, two] = await Promise.all([
      $axios.get('/most_common'),
      $axios.get('/count_props_by_size'),
    ])
    // console.log(one, two)

    return {
      commonSell: one.data.sell,
      commonRent: one.data.rent,
      commonAll: one.data.all,
      series: [
        {
          data: two.data,
        },
      ],
    }
    // return $axios
    //   .all(['/most_common', '/count_props_by_size'])
    //   .then(
    //     $axios.spread((...responses) => {
    //       // .$get('/most_common')
    //       // .then((data) => {
    //       const responseOne = responses[0]
    //       const responseTwo = responses[1]
    //       console.log(responseOne)
    //       console.log(responseTwo)
    //       return {
    //         commonSell: responseOne.sell,
    //         commonRent: responseOne.rent,
    //         commonAll: responseOne.all,
    //         series: [
    //           {
    //             data: responseTwo,
    //           },
    //         ],
    //       }
    //     })
    //   )
    //   .catch((error) => console.log(error))
  },
  data() {
    return {
      realestate: [],
      commonSell: [],
      commonRent: [],
      commonAll: [],
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
