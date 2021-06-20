<template>
  <apexchart
    type="pie"
    height="400px"
    :options="chartOptions"
    :series="series"
  ></apexchart>
</template>

<script>
export default {
  props: {
    series: {
      type: Array,
      required: true,
    },
    labels: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      chartOptions: {
        chart: {
          type: 'pie',
          dropShadow: {
            enabled: false,
          },
        },
        labels: this.labels,
        theme: {
          monochrome: {
            enabled: true,
          },
        },
        plotOptions: {
          pie: {
            expandOnClick: false,
          },
        },
        dataLabels: {
          formatter(val, opts) {
            return [val.toFixed(1) + '%']
          },
          dropShadow: {
            enabled: false,
          },
        },
        legend: {
          show: true,
        },
        states: {
          active: {
            allowMultipleDataPointsSelection: false,
            filter: {
              type: 'none',
            },
          },
        },
      },
    }
  },
}
</script>

<style></style>
