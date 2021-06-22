<template>
  <v-card class="elevation-0">
    <v-card-title class="headline"
      >Properties built in 2020. sorted by price
    </v-card-title>
    <v-tabs v-model="tab">
      <v-tab href="#sell">
        Sell
        <!-- <v-icon>mdi-home</v-icon> -->
      </v-tab>

      <v-tab href="#rent">
        Rent
        <!-- <v-icon>mdi-office-building</v-icon> -->
      </v-tab>
    </v-tabs>

    <v-tabs-items v-model="tab">
      <v-tab-item v-for="i in ['sell', 'rent']" :key="i" :value="i">
        <v-card-text>
          <price-location-size-table :items="i == 'sell' ? sell : rent" />
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
    sell: {
      type: Array,
      default: () => {
        return []
      },
    },
    rent: {
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
