<template>
  <v-row justify="center" align="center">
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
export default {
  asyncData({ app }) {
    return app.$axios
      .$get('/realestate')
      .then((realestate) => {
        return {
          realestate,
        }
      })
      .catch((error) => console.log(error))
  },
  data() {
    return {
      realestate: [],
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
