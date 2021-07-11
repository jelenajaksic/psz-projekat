<template>
  <v-card class="elevation-0">
    <v-card-title class="headline">Predict price with KNN</v-card-title>
    <v-card-text>
      <v-form ref="form" v-model="valid" lazy-validation>
        <v-checkbox v-model="setK" label="Set K"></v-checkbox>

        <v-text-field
          v-if="setK"
          v-model="k"
          :rules="kRules"
          label="K"
          :required="setK"
        ></v-text-field>

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
      {{ priceEuc }}
    </v-card-text>
    <v-card-text class="headline">
      {{ priceMan }}
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
    priceEuc: '',
    priceMan: '',
    setK: false,
    k: '',
    kRules: [(v) => !!v || 'K is required if Set K is checked'],
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
        k_nbrs: this.setK ? Number(this.k) : 97,
      }
      this.$axios.post('predict_knn', body).then((res) => {
        this.priceEuc = `Price with euc: ${this.mapAnswer(
          res.data.res_euc
        )} EUR`
        this.priceMan = `Price with man: ${this.mapAnswer(
          res.data.res_man
        )} EUR`
      })
    },
    mapAnswer(price) {
      if (price === 1) {
        return 'less than 49K'
      } else if (price === 2) {
        return '50K - 99K'
      } else if (price === 3) {
        return '100K - 149K'
      } else if (price === 4) {
        return '150K - 199K'
      } else if (price === 5) {
        return 'more than 200K'
      }
    },
  },
}
</script>
