===================
Listado de Mascotas
===================

Modificaciones en Vue
=====================

**Archivo:** ``vue/src/app_min/main.js``

.. code:: js

   import { createApp } from 'vue';

   // Reutilizamos el mismo componente de la instancia "app"
   import CardMascotaDetails from "@/app/components/CardMascotaDetails";

   const app_min = createApp({});

   // Registramos el componente de forma global para utilizarlo
   // dentro de nuestro template de Django
   app_min.component('card-mascota-details', CardMascotaDetails);

   app_min.mount('#app_min');



Modificaciones en Django
========================

Creando las vistas
~~~~~~~~~~~~~~~~~~

Anteriormente nuestra vistas de Django no tenian ninguna otra responsabilidad
más que mostrar un template que contiene la aplicación de Vue.js

**Archivo:** ``django/src/apps/refugio/views/vue/app.py``

.. literalinclude :: ./../../../../src/apps/refugio/views/vue/app.py
   :language: python

---

Primero debemos escribir la vista para mostrar el listado de mascota.
Por default el ``generic.ListView`` agrega, al diccionario del context, el
queryset en la llave ``object_list``.

**Archivo:** ``django/src/apps/refugio/views/vue/app_min/list.py``

.. literalinclude :: ./../../../../src/apps/refugio/views/vue/app_min/list.py
   :language: python


Creando el template
~~~~~~~~~~~~~~~~~~~

Anteriormente nuestro template solo tenia un ``<div id="app></div>``
que contenia toda nuestra aplicación de Vue.js

**Archivo:** ``django/src/templates/vue/app.html``

.. literalinclude :: ./../../../../src/templates/vue/app.html
   :language: html

---


Ahora utilizaremos el sistema de plantillas de Django junto con Vue.js
para aprovechar ambos mundos.

**Archivo:** ``django/src/templates/vue/app_min/index.html``

.. literalinclude :: ./../../../../src/templates/vue/app_min/index.html
   :language: html