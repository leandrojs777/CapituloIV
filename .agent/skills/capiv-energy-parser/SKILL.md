---
name: capiv-energy-parser
description: Especialista en datos del Capítulo IV de Energía. Úsala para limpiar, normalizar y agrupar datos de producción de pozos (petróleo, gas, agua) de archivos CSV o Excel.
---



\# Instrucciones Operativas

1\. \[cite\_start]Identificar si el archivo tiene las columnas 'prod\_pet', 'prod\_gas' y 'cuenca'.

2\. Ejecutar el script 'scripts/normalize.py' para limpiar nulos en 'tipo\_de\_recurso'.

3\. \[cite\_start]Generar un resumen de producción por provincia.



\# Validaciones

\- El archivo debe ser un CSV separado por comas.

\- \[cite\_start]No procesar si faltan las columnas de año y mes\[cite: 187].

