<template>
  <apexchart
    type="bar"
    height="350"
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
  },
  data() {
    return {
      chartOptions: {
        theme: {
          mode: 'light',
        },
        chart: {
          fontFamily: 'Roboto, sans-serif',
          type: 'bar',
          background: 'transparent',
          height: 350,
          toolbar: {
            show: false,
          },
        },
        plotOptions: {
          bar: {
            horizontal: false,
            columnWidth: '55%',
            endingShape: 'rounded',
          },
        },
        dataLabels: {
          enabled: false,
        },
        stroke: {
          show: true,
          width: 2,
          colors: ['transparent'],
        },
        xaxis: {
          categories: [
            'Less than 35',
            '36 - 50',
            '51 - 65',
            '66 - 80',
            '81 - 95',
            '96 - 110',
            'More than 110',
            'No size data',
          ],
        },
        yaxis: {
          title: {
            text: 'Number of properties',
          },
        },
        fill: {
          opacity: 1,
        },
        status: {
          filter: {
            type: 'none',
          },
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
