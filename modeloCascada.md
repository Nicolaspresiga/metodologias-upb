##Dificultades identificadas aplicando la metodología de desarrollo en cascada.(Desde el Backend).

- Rigidez del proceso

Una vez que se termina una fase, no se puede volver atrás fácilmente. Esto dificulta corregir errores descubiertos tarde.

- Dependencia de requisitos bien definidos

Si al principio no se recopilan todos los requisitos de forma precisa, el proyecto falla más adelante.

- Poca flexibilidad para iterar

No se permiten ajustes frecuentes ni mejoras continuas.

##Dificultades encontradas desde el Frontend

-Comunicación entre capas frontend y backend:
Al principio fue complejo lograr que el frontend interactuara correctamente con las funciones del backend, ya que la estructura del proyecto exigía una buena organización de importaciones y rutas relativas entre carpetas.

-Errores por importaciones incorrectas:
Varias veces se presentaron errores del tipo ModuleNotFoundError o ImportError debido a que los módulos del frontend intentaban importar funciones que no estaban bien expuestas o que no estaban ubicadas correctamente.

-Problemas con la ejecución y flujo del menú:
Se presentaron dificultades para mantener el menú interactivo activo después de seleccionar una opción, ya que en algunos momentos el flujo del programa se detenía inesperadamente por errores de indentación o mal manejo del bucle principal.

-Formato de impresión de datos en consola:
Inicialmente la impresión de listas de productos se hacía de forma manual con print(), lo que generaba resultados poco legibles. Se integró la librería tabulate para mejorar el formato, pero hubo errores de tipo como TypeError: 'module' object is not callable, lo cual se solucionó importando correctamente la función.

-Filas vacías al listar datos:
Al mostrar los productos, aparecían filas sin información (None) provenientes del archivo Excel. Se resolvió agregando validaciones dentro de la lógica del backend, pero esto afectaba directamente el comportamiento esperado en el frontend.