<template>
  <v-card class="elevation-0">
    <v-card-title class="headline"> Top 100 by size </v-card-title>
    <v-tabs v-model="tab">
      <v-tab href="#houses">
        Houses
        <v-icon>mdi-home</v-icon>
      </v-tab>

      <v-tab href="#apartments">
        Apartments
        <v-icon>mdi-office-building</v-icon>
      </v-tab>
    </v-tabs>

    <v-tabs-items v-model="tab">
      <v-tab-item v-for="i in ['houses', 'apartments']" :key="i" :value="i">
        <v-card-text>
          <price-location-size-table
            :items="i == 'houses' ? topHouses : topApartments"
          />
        </v-card-text>
      </v-tab-item>
    </v-tabs-items>
  </v-card>
</template>

<script>
import PriceLocationSizeTable from './PriceLocationSizeTable.vue'
export default {
  components: { PriceLocationSizeTable },
  props: {
    topHouses: {
      type: Array,
      default: () => {
        return []
      },
    },
    topApartments: {
      type: Array,
      default: () => {
        return []
      },
    },
  },
  data() {
    return {
      tab: null,
      headers: [
        { text: 'Location', value: 'location' },
        { text: 'Size', value: 'size' },
        { text: 'Price', value: 'price' },
        { text: 'Link', value: 'url' },
      ],
    }
  },
}
</script>

<style></style>
