<template>
  <v-row>
    <v-col cols="12">
      <v-card class="elevation-0">
        <v-card-title class="headline"> Realestate </v-card-title>
        <v-card-text>
          <v-data-table
            :headers="headers"
            :items="realestate"
            :options.sync="options"
            :loading="loading"
            :items-per-page="15"
            :footer-props="footerProps"
            :server-items-length="24900"
            class="elevation-0"
          >
            <template #[`item.size`]="{ item }">
              {{ item.size !== '' ? item.size : '--' }} m<sup>2</sup>
            </template>
            <template #[`item.price`]="{ item }">
              {{ item.price !== '' ? item.price.toLocaleString() : '--' }}
              &euro;
            </template>
            <template #[`item.url`]="{ item }">
              <v-btn icon link :href="item.url" target="_blank">
                <v-icon> mdi-link-variant </v-icon>
              </v-btn>
            </template>
          </v-data-table>
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
export default {
  data() {
    return {
      options: {},
      realestate: [],
      loading: false,
      headers: [
        { text: 'Add Type', value: 'add_type' },
        { text: 'Property Type', value: 'property_type' },
        { text: 'Location', value: 'location' },
        { text: 'Size', value: 'size' },
        { text: 'Price', value: 'price' },
        { text: 'Link', value: 'url' },
      ],
      footerProps: { 'items-per-page-options': [15, 20, 50] },
    }
  },
  watch: {
    options: {
      handler() {
        this.getData()
      },
      deep: true,
    },
  },
  methods: {
    async getData() {
      this.loading = true
      const { sortBy, sortDesc, page, itemsPerPage } = this.options
      const body = {
        page,
        itemsPerPage,
        sortBy,
        sortDesc,
      }
      const response = await this.$axios.post('/realestate', body)
      this.realestate = response.data
      this.loading = false
    },
  },
}
</script>
