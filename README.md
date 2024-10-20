# ✈️ Comparativa de Viajes: Madrid - París vs Madrid - Roma (2T 2025)

## 📖 Descripción

Este proyecto tiene como objetivo comparar dos posibles viajes para una pareja de novios que planean viajar en el segundo trimestre de 2025: uno de Madrid a París y otro de Madrid a Roma. Se analizan diferentes factores para ofrecer una recomendación basada en los costos de vuelos, alojamiento y actividades turísticas en cada ciudad.

Utilizando la **API de Amadeus**, se obtuvo información actualizada sobre vuelos para las dos rutas. Para los alojamientos, se recomienda utilizar la **API de Booking** o **Airbnb**, mientras que la información de actividades y atracciones en cada ciudad fue extraída a través de un *web scraping* de la página [HelloTickets](https://www.hellotickets.es/).

El análisis fue desarrollado íntegramente en **Python**, utilizando diferentes librerías para el manejo de APIs, scraping y visualización de datos.

## 🗂️ Estructura del Proyecto

```
├── data/                # Datos sobre vuelos, alojamientos y actividades
├── notebooks/           # Notebooks de Jupyter con análisis y visualización
├── src/                 # Scripts de procesamiento de datos y scraping
├── results/             # Gráficos comparativos y archivos de resultados
├── README.md            # Descripción del proyecto
```

## 🛠️ Instalación y Requisitos

Este proyecto utiliza **Python 3.8** y requiere las siguientes bibliotecas:

- pandas
- numpy
- matplotlib
- requests (para la conexión con APIs)
- BeautifulSoup (para el scraping)
- selenium (en caso de que sea necesario para scraping dinámico)

Para instalar las dependencias, ejecuta:

```bash
pip install -r requirements.txt
```

## 🚀 Procedimiento

1. **Vuelos**: Se consultaron las rutas Madrid-París y Madrid-Roma para obtener precios promedio usando la API de Amadeus, filtrando por vuelos directos en febrero de 2025.
   
2. **Alojamientos**: Se obtuvo una muestra representativa de precios y disponibilidad de hoteles y otros alojamientos en ambas ciudades, utilizando la API de [Booking](https://www.booking.com/).

3. **Actividades**: Se extrajeron datos de la web de HelloTickets sobre tours, atracciones y actividades para turistas en cada ciudad mediante *scraping* con BeautifulSoup.

4. **Análisis**: Se realizó una comparativa basada en costos, accesibilidad y recomendaciones para actividades en ambas ciudades.

## 📊 Resultados y Conclusiones

- **Costos de Vuelos**: Los vuelos de Madrid a París presentan precios ligeramente más bajos que los vuelos a Roma durante el segundo trimestre de 2025.
- **Alojamientos**: Los costos de alojamiento en París son, en promedio, más elevados que en Roma, especialmente en el centro de la ciudad.
- **Actividades**: Roma ofrece una mayor cantidad de actividades culturales y museos, mientras que Paris destaca en términos de tours históricos y gastronómicos.
  
En conclusión, para una pareja que busca una experiencia más económica y cultural, Roma es una mejor opción, mientras que París puede ser más interesante para aquellos interesados en el arte y la alta gastronomía.

## 🔄 Próximos Pasos

- Ampliar la base de datos de actividades incluyendo otras plataformas para obtener una muestra más amplia de atracciones.
- Incorporar análisis de transporte público y otros costos adicionales como restaurantes y vida nocturna.
- Crear una versión web interactiva que permita a los usuarios personalizar sus preferencias y obtener recomendaciones de viaje.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar el proyecto o agregar nuevas funcionalidades, por favor abre un *pull request* o una *issue*.

 
