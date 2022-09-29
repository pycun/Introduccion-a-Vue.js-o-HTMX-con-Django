<template>
  <div class="container">
    <div class="row">
      <CardMascotaDetails
          :nombre="mascota.nombre"
          :sexo="mascota.sexo"
          :edad="mascota.edad"
          :fecha_rescate="mascota.fecha_rescate"
          :persona="`${mascota.persona.nombre} ${mascota.persona.apellidos}`"
          :vacunas="mascota.vacunas"
          class="col-6"
      >
        <button
            class="btn btn-outline-primary"
            @click="edit = !edit"
        >
          {{ edit ?  'Cancelar' : 'Editar' }}
        </button>
      </CardMascotaDetails>

      <div v-if="edit" class="card col-6" style="width: 18rem; margin: 15px;" >
        <div class="card-body">
          <slot></slot>
        </div>
      </div>

    </div>
  </div>
</template>

<script>

import CardMascotaDetails from '@/app/components/CardMascotaDetails';

export default {
  name: 'CardMascotaForm',
  components: {
    CardMascotaDetails,
  },
  data: function () {
    return {
      edit: false,
    }
  },
  props: ['mascota', 'error'],
  mounted() {
    // Si desde Django informamos un error del formulario en los props
    // entonces iniciamos el componente mostrando el form
    this.edit = this.error;
  }
}
</script>
