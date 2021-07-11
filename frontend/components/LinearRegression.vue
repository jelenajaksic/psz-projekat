<template>
  <v-card class="elevation-0">
    <v-card-title class="headline">
      Predict price with Linear Regression
    </v-card-title>
    <v-card-text>
      <v-form ref="form" v-model="valid" lazy-validation>
        <v-text-field
          v-model="size"
          :rules="sizeRules"
          label="Size [m2]"
          required
        ></v-text-field>

        <v-text-field
          v-model="dist"
          :rules="distRules"
          label="Distance From Centre [km]"
          required
        ></v-text-field>

        <v-text-field
          v-model="rooms"
          :rules="roomsRules"
          label="Number of rooms"
          required
        ></v-text-field>

        <v-select
          v-model="year"
          :items="yearOptions"
          :rules="[(v) => !!v || 'Year is required']"
          label="Year"
          required
        ></v-select>

        <v-btn :disabled="!valid" color="success" class="mr-4" @click="predict">
          Predict
        </v-btn>

        <v-btn color="warning" class="mr-4" @click="reset"> Reset Form </v-btn>
      </v-form>
    </v-card-text>
    <v-card-text class="headline">
      {{ price }}
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  data: () => ({
    valid: true,
    size: '',
    sizeRules: [(v) => !!v || 'Size is required'],
    rooms: '',
    roomsRules: [(v) => !!v || 'Number of rooms is required'],
    dist: '',
    distRules: [(v) => !!v || 'Distance from centre is required'],
    year: null,
    yearOptions: ['New', 'Old', 'No data'],
    price: '',
  }),

  methods: {
    validate() {
      this.$refs.form.validate()
    },
    reset() {
      this.$refs.form.reset()
      this.price = ''
    },
    predict() {
      const body = {
        size: Number(this.size),
        dist: Number(this.dist),
        rooms: Number(this.rooms),
        nodata: Number(this.year === 'No data'),
        new: Number(this.year === 'New'),
        old: Number(this.year === 'Old'),
      }
      this.$axios.post('linear_regression', body).then((res) => {
        this.price = `Price: ${res.data} EUR`
      })
    },
  },
}
</script>
