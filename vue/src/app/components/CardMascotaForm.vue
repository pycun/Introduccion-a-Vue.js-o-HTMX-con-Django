<template>
  <div class="container">
    <div class="row">

      <CardMascotaDetails
          :nombre="nombre"
          :sexo="sexo"
          :edad="edad"
          :fecha_rescate="fecha_rescate"
          :persona="personaSeleccionada"
          :vacunas="vacunasSeleccionadas"
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
          <form class="container" v-if="!loading">
            <div :class="formGroupClass">
              <label :class="formLabelClass">Nombre</label>
              <input
                  v-model="nombre"
                  :class="formControlClass"
                  type="text"
                  maxlength="50"
                  required=""
              >
            </div>
            <div :class="formGroupClass">
              <label :class="formLabelClass">Sexo</label>
              <select
                  v-model="sexo"
                  :class="formControlClass"
                  required=""
              >
                <option value="1" selected="">Masculino</option>
                <option value="2">Femenino</option>
              </select>
            </div>
            <div :class="formGroupClass">
              <label :class="formLabelClass">Edad</label>
              <input
                  v-model="edad"
                  :class="formControlClass"
                  type="number"
                  required=""
              >
            </div>
            <div :class="formGroupClass">
              <label :class="formLabelClass">Fecha rescate</label>
              <input
                  v-model="fecha_rescate"
                  :class="formControlClass"
                  type="date"
                  required=""
              >
            </div>
            <div :class="formGroupClass">
              <label :class="formLabelClass">Asignado a</label>
              <select
                  v-model="persona"
                  :class="formControlClass"
                  required=""
              >
                <option
                    v-for="{id, nombre, apellidos, email:key } in listaPersonas"
                    :key="key"
                    :value="id"
                >
                  {{ nombre }} {{apellidos}}
                </option>
              </select>
            </div>
            <div :class="formGroupClass">
              <label for="id_vacunas" :class="formLabelClass">Vacunas aplicadas</label>
              <select
                  v-model="vacunas"
                  :class="formControlClass"
                  multiple
                  required=""
              >
                <option
                    v-for="{id, nombre } in listaVacunas"
                    :key="`${nombre}-${id}`"
                    :value="id"
                >
                  {{ nombre }}
                </option>
              </select>
            </div>
            <div class="row">
              <button
                  @click="submit"
                  :class="{'col-6 btn btn-outline-primary col-4': true, 'disabled placeholder': skeleton}"
              >
                Guardar
              </button>
            </div>
          </form>
          <div v-else>
            <div class="loading-container">
              <div class="loading"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import axios from "axios";
import CardMascotaDetails from '@/app/components/CardMascotaDetails';

export default {
  name: 'CardMascotaForm',
  components: {
    CardMascotaDetails,
  },
  data: function () {
    return {
      edit: false,
      skeleton: true,
      loading: false,
      listaVacunas: [],
      listaPersonas: [],

      nombre: null,
      sexo: null,
      edad: null,
      fecha_rescate: null,
      persona: null,
      vacunas: null,
    }

  },
  props: ['mascota'],
  mounted() {
    this.nombre = this.mascota.nombre;
    this.sexo = this.mascota.sexo;
    this.edad = this.mascota.edad;
    this.fecha_rescate = this.mascota.fecha_rescate;
    this.persona = this.mascota.persona.id;
    this.vacunas = this.mascota.vacunas.map((ele) => ele.id);

    // Consulta los datos de las vacunas y personas para agregar los options de los selects del form
    Promise.all([this.fetchVacunas(), this.fetchPersonas()])
        .then(() => this.skeleton = false)
        .catch(() => {
          // Si ocurrio un fallo al obtener los datos impedimos editar
          alert('Error obteniendo los datos del formulario')
          this.edit = false;
        });
  },
  computed: {
    formGroupClass() {
      return `form-group ${this.skeleton ? 'placeholder-glow' : ''}`
    },
    formLabelClass() {
      return this.skeleton ? 'placeholder' : '';
    },
    formControlClass() {
      return `form-control ${this.skeleton ? 'placeholder' : ''}`
    },
    personaSeleccionada() {
      const personas = this.listaPersonas.filter((persona) => {
        return persona.id === this.persona;
      });
      return personas.length
          ? `${personas[0].nombre} ${personas[0].apellidos}`
          : '';
    },
    vacunasSeleccionadas() {
      return this.listaVacunas.filter((vacuna) => {
        return this.vacunas.includes(vacuna.id);
      });
    },
  },
  methods: {
    async fetchVacunas() {
      const response = await axios.get('/api/vacunas/')
      this.listaVacunas = response.data;
    },

    async fetchPersonas() {
      const response = await axios.get('/api/personas/')
      this.listaPersonas = response.data;
    },

    /**
     * Envio del formulario para actualizar los datos de la mascota mediante
     * la API
     * @returns {Promise<void>}
     */
    async submit() {
      this.loading = true;
      try {
        // Actualiza el registro de mascota
        await axios.put(`/api/mascotas/${this.mascota.id}/`, {
          nombre: this.nombre,
          sexo: this.sexo,
          edad: this.edad,
          fecha_rescate: this.fecha_rescate,
          persona: this.persona,
          vacunas: this.vacunas,
        });
        this.edit = false;
      } catch (e) {
        console.error(e);
      } finally {
        // Notifica al parent componente (CardMascota) de la acción submit
        this.loading = false;
      }
    }
  }
}
</script>

<style scoped>
.loading-container {
  display: flex;
  justify-content: center;
  align-items: center;

  min-height: 150px;
}

.loading {
  width:20px;
  height:20px;
  background:#25b09b;
  box-shadow:0 0 60px 15px #25b09b;
  transform: translate(-80px);
  clip-path:inset(0);
  animation:
      w4-1 0.5s ease-in-out infinite alternate,
      w4-2 1s   ease-in-out infinite;
}

@keyframes w4-1 {
  100% {transform:translateX(80px)}
}

@keyframes w4-2 {
  33% {clip-path:inset(0 0 0 -100px)}
  50% {clip-path:inset(0 0 0 0)     }
  83% {clip-path:inset(0 -100px 0 0)}
}
</style>