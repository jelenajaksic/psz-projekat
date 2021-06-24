<template>
  <v-data-table
    :headers="headers"
    :items="items"
    disable-pagination
    disable-sort
    hide-default-footer
    fixed-header
    class="elevation-0"
    height="450px"
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
        { text: 'Location', value: 'location' },
        { text: 'Number', value: 'number' },
      ],
    }
  },
}
</script>

<style></style>
