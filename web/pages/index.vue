<template>
  <v-row justify="center" align="center">
    <v-col cols="12" lg="4">
      <v-card>
        <v-card-title class="headline"> Most common in BGD</v-card-title>
        <v-card-text>
          <most-common :items="commonAll" />
        </v-card-text>
      </v-card>
    </v-col>
    <v-col cols="12" lg="4">
      <v-card>
        <v-card-title class="headline"> Most common sell in BGD</v-card-title>
        <v-card-text>
          <most-common :items="commonSell" />
        </v-card-text>
      </v-card>
    </v-col>
    <v-col cols="12" lg="4">
      <v-card>
        <v-card-title class="headline"> Most common rent in BGD</v-card-title>
        <v-card-text>
          <most-common :items="commonRent" />
        </v-card-text>
      </v-card>
    </v-col>
    <v-col cols="12">
      <v-card>
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
import MostCommon from '../components/MostCommon.vue'
export default {
  components: { MostCommon },
  asyncData({ app }) {
    // const data = app.$axios.get(`/most_common`)
    // console.log(data)
    // return {
    //   commonSell: data.sell,
    //   commonRent: data.rent,
    //   commonAll: data.all,
    // }
    return app.$axios
      .$get('/most_common')
      .then((data) => {
        return {
          commonSell: data.sell,
          commonRent: data.rent,
          commonAll: data.all,
        }
      })
      .catch((error) => console.log(error))
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
