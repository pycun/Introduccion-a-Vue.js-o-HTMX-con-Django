<template>
  <div style="width: 100%; margin: auto;">
    <CardMascotaForm
        v-if="mascota"
        :mascota="mascota"
    />
  </div>
</template>

<script>
import axios from 'axios';
import CardMascotaForm from '@/app/components/CardMascotaForm';

export default {
  name: 'UpdateView',
  components: {
    CardMascotaForm,
  },
  data: function () {
    return {
      mascota: null,
    }
  },
  mounted() {
    this.fetchMascota(this.$route.params.id);
  },
  methods: {
    fetchMascota: async function (pk) {
      const response = await axios.get(`/api/mascotas/${pk}/`)
      this.mascota = response.data;
    },
  }
}
</script>