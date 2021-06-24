<template>
  <v-data-table
    :headers="headers"
    :items="items"
    disable-sort
    fixed-header
    :items-per-page="10"
    class="elevation-0"
  >
    <template #[`item.property_type`]="{ item }">
      {{ item.property_type == 'a' ? 'Apartment' : 'House' }}
    </template>
    <template #[`item.size`]="{ item }">
      {{ item.size !== '' ? item.size.toLocaleString() : '--' }} m<sup>2</sup>
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
</template>

<script>
export default {
  props: {
    items: {
      type: Array,
      default: () => {
        return []
      },
    },
  },
  data() {
    return {
      headers: [
        { text: 'Property type', value: 'property_type' },
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
