<template>
  <div class="card" style="width: 18rem; margin: 15px;">
    <div class="card-body">
      <h5 class="card-title">{{ nombre }}</h5>

      <p class="card-text">
        "{{ nombre }}" es una mascota del sexo {{ sexo }} que tiene una edad
        de {{ edad }} años.
      </p>
      <p class="card-text">
        Rescatado el día {{ fecha_rescate }}, por {{ persona }}.
      </p>
    </div>

    <div class="card-footer text-muted">
      Vacunas aplicadas:

      <div v-if="!!vacunas.length">
          <span
              v-for="vacuna in vacunas"
              :key="vacuna.nombre + '-' + vacuna.id">
            {{ vacuna.nombre }} -
          </span>
      </div>
      <div v-else>
        <span>Ninguna</span>
      </div>
    </div>

    <div class="card-footer">
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CardMascotaDetails',
  props: {
    nombre: String,
    sexo: Number,
    edad: Number,
    fecha_rescate: String,
    persona: String,
    vacunas: {
      type: Array,
      default: function () {
        return []
      },
    }
  },
}
</script>
