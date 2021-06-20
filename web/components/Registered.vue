<template>
  <v-row justify="center" align="center" class="mx-0">
    <v-col cols="4">
      <v-card color="cyan darken-1" :elevation="0">
        <v-row class="ma-0">
          <v-col cols="8">
            <v-list-item two-line class="mt-8">
              <v-list-item-content>
                <v-list-item-title class="headline mb-1 white--text">
                  {{ item.registered.toLocaleString() }}
                </v-list-item-title>
                <v-list-item-subtitle class="white--text"
                  >Number of registered {{ type }}</v-list-item-subtitle
                >
              </v-list-item-content>
            </v-list-item>
          </v-col>
          <v-col cols="4">
            <v-avatar size="100" class="my-2" tile>
              <span class="registered" />
            </v-avatar>
          </v-col>
        </v-row>
      </v-card>
    </v-col>
    <v-col cols="4">
      <v-card color="cyan darken-1" :elevation="0">
        <v-row class="ma-0">
          <v-col cols="8">
            <v-list-item two-line class="mt-8">
              <v-list-item-content>
                <v-list-item-title class="headline mb-1 white--text">
                  {{ item.unregistered.toLocaleString() }}
                </v-list-item-title>
                <v-list-item-subtitle class="white--text"
                  >Number of not registered {{ type }}</v-list-item-subtitle
                >
              </v-list-item-content>
            </v-list-item>
          </v-col>
          <v-col cols="4">
            <v-avatar size="100" class="my-2" tile>
              <span class="unregistered" />
            </v-avatar>
          </v-col>
        </v-row>
      </v-card>
    </v-col>
    <v-col cols="4">
      <v-card color="cyan darken-1" :elevation="0">
        <v-row class="ma-0">
          <v-col cols="8">
            <v-list-item two-line class="mt-8">
              <v-list-item-content>
                <v-list-item-title class="headline mb-1 white--text">
                  {{ item.nodata.toLocaleString() }}
                </v-list-item-title>
                <v-list-item-subtitle class="white--text"
                  >Number of {{ type }} with no registration data
                </v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </v-col>
          <v-col cols="4">
            <v-avatar size="100" class="my-2" tile>
              <span class="nodata" />
            </v-avatar>
          </v-col>
        </v-row>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
export default {
  props: {
    item: {
      type: Object,
      required: true,
    },
    type: {
      type: String,
      default: '',
    },
  },
}
</script>

<style scoped>
.registered {
  mask: url('~/assets/verify.svg');
  height: 100px;
  width: 100px;
  mask-size: contain;
  background: white;
}

.unregistered {
  mask: url('~/assets/remove.svg');
  height: 100px;
  width: 100px;
  mask-size: contain;
  background: white;
}

.nodata {
  mask: url('~/assets/question-mark.svg');
  height: 100px;
  width: 100px;
  mask-size: contain;
  background: white;
}
</style>
>
