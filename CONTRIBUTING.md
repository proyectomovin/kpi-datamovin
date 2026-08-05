# Contribuir a DataMovin KPI

DataMovin recibe correcciones y mejoras mediante pull requests en
`proyectomovin/kpi-datamovin`.

## Flujo

1. Crear una rama desde `main`.
2. Mantener intactos los contratos tecnicos de KPI, KoboCAT, KoboCollect y
   OpenRosa salvo que el cambio aprobado indique lo contrario.
3. Agregar pruebas para todo cambio de comportamiento.
4. Regenerar OpenAPI y Orval cuando cambie una interfaz publica.
5. Ejecutar lint, type-check, build y pruebas antes de abrir el pull request.
6. Explicar riesgos de migracion, despliegue y retroceso cuando corresponda.

Los reportes de errores se registran en
<https://github.com/proyectomovin/kpi-datamovin/issues>. Los reportes de
seguridad deben enviarse en privado a `hola@movin.com.ar`.

Las contribuciones se publican bajo la misma licencia AGPL-3.0 incluida en
[LICENSE](./LICENSE).

## Estilo

Las reglas automaticas se encuentran en `.editorconfig`, `eslint.config.mjs`,
`.stylelintrc.js`, `biome.jsonc`, `coffeelint.json` y `pyproject.toml`. Las
convenciones manuales estan en `CODING_STYLE_FE.md` y `CODING_STYLE_BE.md`.
