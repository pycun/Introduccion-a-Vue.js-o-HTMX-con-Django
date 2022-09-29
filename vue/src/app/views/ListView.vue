<template>
  <h1>Listado de Mascotas con Vue.js</h1>

  <div class="container">
    <div class="row" v-if="!!listaMascotas.length">
      <div
          v-for="(mascota, index) in listaMascotas"
          :key="index"
          class="col">

          <CardMascotaDetails
              :nombre="mascota.nombre"
              :sexo="mascota.sexo"
              :edad="mascota.edad"
              :fecha_rescate="mascota.fecha_rescate"
              :persona="`${mascota.persona.nombre} ${mascota.persona.apellidos}`"
              :vacunas="mascota.vacunas"
          >
            <button
                class="btn btn-outline-primary"
                @click="$router.push({
                  name: 'retrieve',
                  params: { id: mascota.id },
                })"
            >
              Ver
            </button>
          </CardMascotaDetails>

      </div>
    </div>
    <div v-else> ¡Ups!... Parece que no hay nada aqui. </div>
  </div>
</template>

<script>
import axios from 'axios';
import CardMascotaDetails from '@/app/components/CardMascotaDetails.vue'

export default {
  name: 'ListView',

  components: {
    CardMascotaDetails,
  },

  data: function () {
    return {
      listaMascotas: [],
    }
  },

  methods: {
    fetchListaMascotas: async function () {
      const response = await axios.get('/api/mascotas/')
      this.listaMascotas = response.data;
    },
  },

  mounted() {
    this.fetchListaMascotas()
  }
}
</script>
