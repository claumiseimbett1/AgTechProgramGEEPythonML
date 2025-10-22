# 🌾 Certificación Internacional AgTech
## Google Earth Engine, Machine Learning y Python

![AgTech](https://img.shields.io/badge/AgTech-Certification-green)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Earth Engine](https://img.shields.io/badge/Google-Earth%20Engine-yellow)
![Machine Learning](https://img.shields.io/badge/ML-scikit--learn-orange)

---

## 📋 Descripción

Este repositorio contiene los ejercicios prácticos desarrollados durante la **Certificación Internacional en AgTech** enfocada en el uso de:

- 🛰️ **Google Earth Engine (GEE)** para análisis de imágenes satelitales
- 🤖 **Machine Learning** aplicado a agricultura de precisión
- 🐍 **Python** como lenguaje principal de desarrollo
- 🗺️ **Análisis Geoespacial** con GeoPandas y Shapely

El proyecto se centra en el análisis de vegetación mediante índices espectrales (NDVI) utilizando imágenes satelitales de **MODIS** y **Sentinel-2**, con aplicaciones prácticas en silvopasturas y agricultura de precisión.

---

## 🎯 Objetivos del Proyecto

1. **Análisis Temporal de NDVI**: Monitoreo de la salud vegetal a lo largo del tiempo
2. **Comparación de Sensores**: Análisis comparativo entre MODIS (250m) y Sentinel-2 (10m)
3. **Firmas Espectrales**: Caracterización espectral de diferentes coberturas (vegetación, suelo, agua)
4. **Análisis por Zonas**: Extracción de estadísticas NDVI usando shapefiles de parcelas
5. **Visualización Interactiva**: Mapas web interactivos con geemap y folium
6. **Segmentación**: Clustering K-means para zonificación de áreas agrícolas

---

## 📂 Estructura del Repositorio

```
AgTechProgramGEEPythonML/
│
├── 1-DescargarImagYFirmasfromGEE.ipynb    # Descarga de imágenes y firmas espectrales
├── 2-NDVI_DRON_SATELLITE.ipynb            # Comparación NDVI dron vs satélite
├── 3-Generar Parcelas SHAPEFILES.ipynb    # Generación de shapefiles de parcelas
├── 4-NDVI_Satellite_Shapes.ipynb          # Análisis NDVI con shapefiles
├── 5-Segmentación_Kmeans/                 # Segmentación con K-means
├── 6-DescargarImagFusionSentModisSerieTEmporal.ipynb  # Fusión de series temporales
├── 7-Visualizar_NDVI_Mapa_Embebido.ipynb  # Mapas interactivos
│
├── aoi_parcela.shp                         # Shapefile de área de interés
├── requirements.txt                        # Dependencias del proyecto
├── .gitignore                              # Archivos excluidos del repositorio
└── README.md                               # Este archivo
```

---

## 🚀 Características Principales

### 1. **Análisis Multitemporal NDVI**
- Monitoreo de 4 zonas durante 2022-2023
- Extracción automática de datos mensuales
- Visualización de patrones estacionales
- Detección de cambios en la cobertura vegetal

### 2. **Integración con Google Earth Engine**
- Acceso a catálogos completos de imágenes satelitales
- Procesamiento en la nube sin descargas
- Filtrado por nubes y calidad de datos
- Exportación a Google Drive

### 3. **Comparación de Sensores**
- **MODIS**: 23 puntos/año (cada 16 días), resolución 250m
- **Sentinel-2**: 12 puntos/año (mensual), resolución 10m
- Análisis de diferencias y complementariedad

### 4. **Firmas Espectrales**
- Caracterización de 7 bandas MODIS
- 6 bandas Sentinel-2
- Clasificación de coberturas terrestres

### 5. **Mapas Interactivos**
- Visualización web con geemap
- Capas NDVI con escala de colores
- Superposición de shapefiles
- Exportación a HTML para GitHub Pages

---

## 🛠️ Tecnologías Utilizadas

| Tecnología | Versión | Uso |
|-----------|---------|-----|
| Python | 3.11+ | Lenguaje principal |
| earthengine-api | 1.6.13 | API de Google Earth Engine |
| geemap | 0.36.5 | Mapas interactivos con GEE |
| geopandas | 1.1.1 | Análisis geoespacial vectorial |
| shapely | 2.1.2 | Manipulación de geometrías |
| matplotlib | 3.10.7 | Visualización de datos |
| pandas | 2.3.3 | Análisis de datos tabulares |
| numpy | 2.3.4 | Operaciones numéricas |
| scikit-learn | 1.7.2 | Machine Learning |
| jupyter | 1.1.1 | Notebooks interactivos |

---

## 📦 Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/AgTechProgramGEEPythonML.git
cd AgTechProgramGEEPythonML
```

### 2. Crear entorno virtual
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Autenticar Google Earth Engine
```bash
earthengine authenticate
```

Sigue las instrucciones para autenticarte con tu cuenta de Google.

---

## 🎓 Uso

### Ejemplo 1: Análisis NDVI Temporal
```python
import ee
import geemap

# Inicializar Earth Engine
ee.Initialize(project='tu-proyecto-id')

# Definir área de interés
aoi = ee.Geometry.Rectangle([-75.89, 8.88, -75.86, 8.91])

# Obtener colección Sentinel-2
s2 = ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED') \
    .filterDate('2023-01-01', '2023-12-31') \
    .filterBounds(aoi) \
    .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20))

# Calcular NDVI
ndvi = s2.median().normalizedDifference(['B8', 'B4'])

# Visualizar
Map = geemap.Map()
Map.addLayer(ndvi, {'min': 0, 'max': 1, 'palette': ['red', 'yellow', 'green']}, 'NDVI')
Map
```

### Ejemplo 2: Análisis con Shapefiles
```python
import geopandas as gpd

# Cargar shapefile
parcelas = gpd.read_file('aoi_parcela.shp')

# Extraer estadísticas NDVI por parcela
for idx, parcela in parcelas.iterrows():
    stats = ndvi.reduceRegion(
        reducer=ee.Reducer.mean(),
        geometry=ee.Geometry(parcela.geometry.__geo_interface__),
        scale=10
    ).getInfo()
    print(f"Parcela {idx}: NDVI = {stats['nd']:.3f}")
```

---

## 📊 Resultados y Visualizaciones

### Mapa NDVI Interactivo
🔗 **[Ver Mapa en Vivo](https://tu-usuario.github.io/AgTechProgramGEEPythonML/)**

### Comparación MODIS vs Sentinel-2
- MODIS ofrece mayor frecuencia temporal (23 vs 12 observaciones/año)
- Sentinel-2 proporciona mayor resolución espacial (10m vs 250m)
- Ambos sensores muestran patrones estacionales consistentes

### Estadísticas por Zona
| Zona | NDVI Promedio | NDVI Min | NDVI Max | Desv. Est. |
|------|---------------|----------|----------|------------|
| Norte | 0.785 | 0.623 | 0.892 | 0.045 |
| Sur | 0.721 | 0.598 | 0.834 | 0.052 |
| Este | 0.756 | 0.612 | 0.867 | 0.048 |
| Oeste | 0.798 | 0.645 | 0.901 | 0.041 |

---

## 📈 Aplicaciones Prácticas

1. **Agricultura de Precisión**
   - Detección de áreas con estrés hídrico
   - Optimización de aplicación de fertilizantes
   - Monitoreo de crecimiento de cultivos

2. **Silvopasturas**
   - Evaluación de cobertura arbórea
   - Zonificación de pasturas
   - Planificación de manejo

3. **Cambio Climático**
   - Monitoreo de sequías
   - Análisis de patrones estacionales
   - Detección de anomalías

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📝 Licencia

Este proyecto fue desarrollado como parte de la Certificación Internacional en AgTech y está disponible para fines educativos.

---

## 👤 Autor

**Nombre del Estudiante**
- Certificación: AgTech Internacional
- Enfoque: Google Earth Engine, Machine Learning y Python
- Año: 2024

---

## 🙏 Agradecimientos

- Google Earth Engine por proporcionar acceso a datos satelitales
- Programa de Certificación AgTech
- Comunidad de desarrolladores de geemap y geopandas

---

## 📧 Contacto

Para preguntas o colaboraciones, por favor contacta a través de:
- GitHub: [@tu-usuario](https://github.com/tu-usuario)
- Email: tu-email@example.com

---

**⭐ Si este proyecto te fue útil, considera darle una estrella en GitHub**
