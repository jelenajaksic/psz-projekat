<template>
  <apexchart
    type="donut"
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
    displayTotal: {
      type: Boolean,
      required: true,
    },
  },
  data() {
    return {
      chartOptions: {
        chart: {
          type: 'donut',
        },
        labels: this.labels,
        plotOptions: {
          pie: {
            donut: {
              labels: {
                show: true,
                name: {
                  show: true,
                  fontSize: '22px',
                  fontFamily: 'Helvetica, Arial, sans-serif',
                  fontWeight: 600,
                  formatter(val) {
                    return val
                  },
                },
                value: {
                  show: true,
                  fontSize: '22px',
                  fontFamily: 'Helvetica, Arial, sans-serif',
                  fontWeight: 600,
                  formatter(val) {
                    return val
                  },
                },
                total: {
                  show: this.displayTotal,
                  showAlways: false,
                  label: 'Total [Ratio]',
                  fontSize: '22px',
                  fontFamily: 'Helvetica, Arial, sans-serif',
                  fontWeight: 600,
                  color: '#373d3f',
                  formatter(w) {
                    return w.globals.seriesTotals.reduce((a, b) => {
                      return a && b ? `${a + b} [${(a / b).toFixed(2)}]` : a + b
                    }, 0)
                  },
                },
              },
            },
          },
        },
        dataLabels: {
          dropShadow: {
            enabled: false,
          },
        },
      },
    }
  },
}
</script>

<style></style>
