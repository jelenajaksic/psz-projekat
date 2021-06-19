<template>
  <v-data-table
    :headers="headers"
    :items="items"
    disable-pagination
    disable-sort
    hide-default-footer
    class="elevation-0"
  />
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
        { text: 'Part of the city', value: 'block' },
        { text: 'Number', value: 'number' },
      ],
    }
  },
}
</script>

<style></style>
