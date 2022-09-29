import { createApp } from 'vue';

import CardMascotaDetails from "@/app/components/CardMascotaDetails";

// Utilizamos el componente desde app_min el cual sufrio modificaciones
import CardMascotaForm from "@/app_min/components/CardMascotaForm";

const app_min = createApp({});

app_min.component('card-mascota-details', CardMascotaDetails);

// Registramos el componente de forma global para utilizarlo
// dentro de nuestro template de Django
app_min.component('card-mascota-form', CardMascotaForm);

app_min.mount('#app_min');
