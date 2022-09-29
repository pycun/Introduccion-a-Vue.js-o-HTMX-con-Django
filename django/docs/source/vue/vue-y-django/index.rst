===================================
El equilibrio entre Vue.js y Django
===================================

Para este proyecto creamos otra instancia de vue dentro del mismo proyecto llamada ``app_min``.

De esta manera, contamos con la dos instancias de vue dentro del proyecto: 1) ``app`` y 2) ``app_min``.

En esta nueva instancia de Vue ya no haremos uso de:
    - Componente raíz App, no hace falta porque utilizaremos el sistema de plantillas de Django y ahi llamaremos los componentes de Vue.
    - Vue-router, las urls serán manejadas por el servidor de Django.

.. toctree::
    :maxdepth: 1

    list
    update
