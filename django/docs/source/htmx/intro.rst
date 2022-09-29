===================
Introducción a HTMX
===================

.. raw:: html

    <script src="https://unpkg.com/htmx.org@1.8.0"></script>


HTMX es una biblioteca que agrega herramientas de alto poder para HTML
sin utilizar JavaScript.

Para entender htmx, primero echemos un vistazo a una etiqueta de anclaje:

.. code:: html

    <a href="/blog">Blog</a>

Naturalmente, esta etiqueta le dice a un navegador:

    Cuando un usuario hace clic en este enlace:
        1. emite una solicitud HTTP GET a "/blog"
        2. carga el contenido de la respuesta en la ventana del navegador


Con eso en mente, vamos a analizar el siguiente fragmento de HTML:

.. code:: html

    <div id="parent-div">
        Hola PyCun
    </div>

    <button hx-get="/htmx/intro/clicked/"
        hx-trigger="click"
        hx-target="#parent-div"
        hx-swap="outerHTML"
    >
        Click Me!
    </button>


.. admonition:: .
    :class: hint

    .. raw:: html

        <div id="parent-div">
            Hola PyCun
        </div>

        <button hx-get="/htmx/intro/clicked/"
            hx-trigger="click"
            hx-target="#parent-div"
            hx-swap="outerHTML"
        >
            Click Me!
        </button>


Esto le dice a htmx:

    Cuando un usuario hace clic en este botón:
        1. emite una solicitud HTTP POST a "/click", y
        2. usa el contenido de la respuesta para reemplazar el elemento del DOM con el selector "#parent-div".


AJAX
====

El núcleo de HTMX es un conjunto de atributos que le permiten emitir solicitudes
AJAX directamente desde HTML:

==============  =============
  Atributo       Description
--------------  -------------
==============  =============
    hx-get        Emite una solicitud GET a la URL dada
    hx-post       Emite una solicitud POST a la URL dada
    hx-put        Emite una solicitud PUT a la URL dada
    hx-patch      Emite una solicitud PATCH a la URL dada
    hx-delete     Emite una solicitud DELETE a la URL dada
==============  =============

Triggers
========

De forma predeterminada, las solicitudes AJAX se activan por el evento "natural"
de un elemento:

- ``input``, ``textarea`` y ``select`` se activan en el evento ``change``.
- ``form`` se activa en el evento ``submit``
- todo lo demás es desencadenado por el evento ``click``

Si desea un comportamiento diferente, el atributo hx-trigger permite especificar
qué evento provocará la solicitud.

.. code:: html

    <!-- Se realiza la solicitud cuando el mouse ingresa en el div -->
    <div hx-get="/htmx/intro/mouseenter" hx-trigger="mouseenter">
        [Here Mouse, Mouse!]
    </div>


.. admonition:: .
    :class: hint

    .. raw:: html

        <!-- Se realiza la solicitud cuando el mouse ingresa en el div -->
        <div hx-get="/htmx/intro/mouseenter" hx-trigger="mouseenter">
            [Here Mouse, Mouse!]
        </div>

Targets
=======

Para que la respuesta se cargue en un elemento diferente al que realizó la solicitud,
se puede utilizar el atributo ``hx-target``, que recibe un selector CSS.


.. code:: html

    <input type="text" name="q"
        hx-get="/trigger_delay"
        hx-trigger="keyup delay:500ms changed"
        hx-target="#search-results"
        placeholder="Search..."
    >
    <div id="search-results"></div>

Los resultados de la búsqueda se cargarán en ``div#search-results``, en lugar de en
la etiqueta de entrada.


Swapping
========

HTMX ofrece algunas formas diferentes de intercambiar el HTML devuelto al DOM.
De forma predeterminada, el contenido reemplaza al innerHTMLdel elemento de destino.

Esto puede modificarse utilizando el atributo hx-swap con cualquiera de los siguientes valores:

==============  =============
    Nombre       Description
--------------  -------------
==============  =============
  innerHTML       Coloca el contenido dentro del elemento de destino
  outerHTML       Reemplaza todo el elemento de destino con el contenido devuelto
  afterbegin      Antepone el contenido antes del primer niño dentro del objetivo
  beforebegin     Antepone el contenido antes del objetivo en el elemento principal de objetivos
  beforeend       Agrega el contenido después del último elemento secundario dentro del objetivo
  afterend        Agrega el contenido después del objetivo en el elemento principal de objetivos
==============  =============

.. code:: html

    <div id="parent-div-2">
        Hola PyCun
    </div>

    <button hx-get="/htmx/intro/clicked/"
        hx-trigger="click"
        hx-target="#parent-div-2"
        hx-swap="afterend"
    >
        Click Me!
    </button>


.. admonition:: .
    :class: hint

    .. raw:: html

        <div id="parent-div-2">
            Hola PyCun
        </div>

        <button hx-get="/htmx/intro/clicked/"
            hx-trigger="click"
            hx-target="#parent-div-2"
            hx-swap="afterend"
        >
            Click Me!
        </button>


¿Qué se consigue con HTMX?
==========================

- Ahora cualquier elemento puede emitir una solicitud HTTP.
    Ya no solo anclas y formularios.
- Ahora cualquier evento pueden desencadenar solicitudes.
    Ya no solo los clics o los envíos de formularios.
- Ahora se puede usar cualquier verbo HTTP.
    Ya no solo GET y POST.
- Ahora cualquier elemento puede ser el objetivo de la actualización** mediante la solicitud.
    Ya no toda la ventana.

.. admonition:: .
    :class: important

    Cuando usa HTMX generalmente se responde con HTML, no con JSON.