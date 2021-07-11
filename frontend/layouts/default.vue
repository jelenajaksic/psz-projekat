<template>
  <v-app>
    <v-navigation-drawer permanent :mini-variant="true" fixed app>
      <v-list>
        <v-list-item
          v-for="(item, i) in items"
          :key="i"
          :to="item.to"
          router
          exact
          color="primary"
        >
          <v-list-item-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title v-text="item.title" />
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-main>
      <v-container fluid>
        <nuxt />
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      clipped: false,
      drawer: false,
      fixed: false,
      items: [
        {
          icon: 'mdi-chart-donut',
          title: 'Dashboard',
          to: '/',
        },
        {
          icon: 'mdi-chart-line',
          title: 'Statistics',
          to: '/statistics',
        },
        {
          icon: 'mdi-database',
          title: 'Database',
          to: '/inspire',
        },
        {
          icon: 'mdi-chart-scatter-plot',
          title: 'Predictions',
          to: '/predictions',
        },
      ],
      miniVariant: false,
      right: true,
      rightDrawer: false,
      title: 'Vuetify.js',
    }
  },
}
</script>

<style scoped>
.color {
  background-color: red !important;
}
</style>
