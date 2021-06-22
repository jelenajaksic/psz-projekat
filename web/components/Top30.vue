<template>
  <v-data-table
    :headers="headers"
    :items="items"
    disable-sort
    fixed-header
    :items-per-page="10"
    class="elevation-0"
  >
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
      required: true,
    },
  },
  data() {
    return {
      headers: [
        { text: 'Location', value: 'location' },
        { text: 'Price', value: 'price' },
        { text: 'Link', value: 'url' },
      ],
    }
  },
}
</script>

<style></style>
