# TC3041-P4-Primavera-2019

Antony Adrian Morales

Alberto Pascal

# Problema
El huerto urbano, equiparable al huerto en el jardín, en su concepto se trata de espacios cubiertos o no, para el cultivo de flores, aromáticas, hortalizas y frutales a escala doméstica. Para las personas principiantes resulta un tarea ardua estar al pendiente y conseguir los resultados esperados. La solucion inteligente ayuda a las plantas y cultivos a florecer. Sensores incorporados que monitorean el cultivo todo el día. 

# Descripción de las mediciones
## Series
- Humedad capacitiva del suelo (Rango 0 to 50%)
- Temperatura del ambiente (Cº)
- UV luz solar (μmol)

# Contribuir
## Requisitos previos
- Docker

## Ejecutar contenedores
- `docker run --name influxP4 -d -p 8086:8086 -v $HOME:/var/lib/influxdb influxdb`
- `docker run -d  -p 3000:3000 --name=grafana -e "GF_SERVER_ROOT_URL=http://grafana.server.name" -e "GF_SECURITY_ADMIN_PASSWORD=secret" grafana/grafana`

## Grafana
1. Ingresar a grafana: [http://localhost:3000](http://localhost:3000)
2. Credenciales:
    - Username: `admin`
    - Password: `secret`


En este documento debe incluir el plantemaiento del problema diseñado así como la descripción de las mediciones, series, valores y etiquetas identificados en el problema.