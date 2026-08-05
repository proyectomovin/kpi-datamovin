# DataMovin KPI

Aplicacion de gestion y recoleccion de datos de campo utilizada por DataMovin.
Este repositorio contiene el frontend, las APIs y los componentes compatibles
con OpenRosa que se publican en los dominios de `data.movin.com.ar`.

[![Validacion](https://github.com/proyectomovin/kpi-datamovin/actions/workflows/validate.yml/badge.svg)](https://github.com/proyectomovin/kpi-datamovin/actions/workflows/validate.yml)

## Endpoints

- Aplicacion y API principal: `https://kf.data.movin.com.ar`
- API compatible con OpenRosa: `https://kc.data.movin.com.ar`
- Formularios web: `https://ee.data.movin.com.ar`
- OpenAPI principal: `https://kf.data.movin.com.ar/api/v2/docs/`
- OpenAPI OpenRosa: `https://kf.data.movin.com.ar/api/openrosa/docs/`

El autorregistro esta desactivado. Las cuentas operativas son creadas por Movin
y deben utilizar autenticacion multifactor.

## Desarrollo

La aplicacion conserva los nombres internos y contratos de KPI, KoboCAT,
KoboCollect y OpenRosa que son necesarios para compatibilidad tecnica.

```bash
npm ci
npm run lint
SKIP_TS_CHECK=true npm run build:app
npm run test:unit
```

Las dependencias Python se administran desde `dependencies/pip/`. Los schemas
OpenAPI y clientes derivados deben regenerarse desde sus fuentes:

```bash
./scripts/generate_api.sh --skip-orval
npm run build:orval
```

No se deben editar manualmente archivos dentro de `static/openapi/` ni
`jsapp/js/api/`.

## Imagen

La publicacion oficial usa tags inmutables y genera SBOM y procedencia:

```text
ghcr.io/proyectomovin/kpi-datamovin:2.026.21a-datamovin.1
```

El alias `datamovin-stable` puede moverse entre releases. Los despliegues de
produccion deben fijar el digest `sha256` de la imagen inmutable.

## Soporte

- Correo: `hola@movin.com.ar`
- Sitio: https://movin.com.ar/product-datos-campo

## Procedencia Y Licencia

DataMovin KPI deriva de KoboToolbox KPI `2.026.21a`. Se mantienen los nombres,
avisos y licencias necesarios para cumplir AGPL-3.0 y las licencias de los
componentes OpenRosa. Consultar [NOTICE.md](NOTICE.md) y [LICENSE](LICENSE).

