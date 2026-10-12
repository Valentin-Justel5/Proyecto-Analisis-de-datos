# Proyecto-Analisis-de-datos
Análisis de ventas, clientes y logística de un e-commerce brasileño (Olist) con Python y pandas: evolución mensual, categorías, geografía, entregas, reseñas, medios de pago y recompra.


# Análisis de ventas de un e-commerce con pandas (Olist)

Proyecto de análisis de datos en Python y pandas sobre el **Brazilian E-Commerce Public Dataset by Olist**, un conjunto de datos reales y anonimizados de un marketplace brasileño. El objetivo es entender cómo se comportan las ventas, los clientes y la logística de la tienda, y proponer mejoras basadas en los datos.

## Dataset

- **Fuente:** [Brazilian E-Commerce Public Dataset by Olist (Kaggle)](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
- **Contenido:** unas 100.000 órdenes distribuidas en varias tablas relacionadas: pedidos, ítems, clientes, productos, vendedores, pagos, reseñas y geolocalización.
- **Los CSV no están incluidos en este repositorio** por su tamaño. Para reproducir el análisis, descargalos desde Kaggle y colocalos en una carpeta `csv/` en la raíz del proyecto.

## Preguntas que responde el proyecto

1. ¿Cómo evolucionaron las ventas mes a mes? ¿Hay estacionalidad?
2. ¿Cuáles son las 10 categorías de productos que más facturan?
3. ¿Qué estados o ciudades concentran más clientes e ingresos?
4. ¿Cuánto tarda en promedio la entrega y cuánto se desvía de la fecha estimada?
5. ¿Los retrasos en la entrega afectan la puntuación de las reseñas?
6. ¿Qué medios de pago se usan más y cuál es el ticket promedio de cada uno?
7. ¿Qué porcentaje de clientes compra más de una vez?

## Metodología

Cada pregunta se resolvió con el mismo esquema de trabajo:

1. **Métrica:** qué se quiere medir (total, promedio, cantidad, porcentaje).
2. **Dimensión:** por qué variable se abre el análisis (mes, categoría, estado, medio de pago).
3. **Datos:** qué tablas se necesitan y por qué columna se unen.
4. **Limpieza:** fechas, nulos, pedidos cancelados, duplicados.
5. **Resultado:** tablas y gráficos, y qué conclusión se puede sacar.

### Decisiones de análisis

- Se excluyeron los pedidos cancelados y no disponibles al calcular ventas.
- Los clientes se identifican con `customer_unique_id`, ya que `customer_id` cambia en cada pedido y contarlo inflaría la cantidad de clientes y ocultaría la recompra.
- Para el análisis de entregas solo se consideraron pedidos con fecha de entrega registrada.
- Cuando un pedido tiene varias reseñas, se usó la más reciente.
- Los meses incompletos al inicio y al final del dataset se excluyeron de la evolución mensual.

## Hallazgos principales

> Completar con los resultados obtenidos.

- **Ventas:** _tendencia, picos y estacionalidad observada._
- **Categorías:** _las 3 categorías principales y qué porcentaje de la facturación concentran._
- **Geografía:** _estados que concentran más ingresos y qué porcentaje del total representan._
- **Logística:** _días promedio de entrega y porcentaje de pedidos que llegaron tarde._
- **Reseñas:** _cómo cambia el puntaje promedio según el retraso._
- **Pagos:** _medio de pago más usado y ticket promedio de cada uno._
- **Recompra:** _porcentaje de clientes recurrentes._

## Recomendaciones

> Completar con 2 o 3 recomendaciones de negocio basadas en los hallazgos.

## Estructura del repositorio

```
.
├── codigo/          # scripts de Python, uno por pregunta
├── csv/             # datasets de Olist (no incluidos, ver sección Dataset)
├── .gitignore
└── README.md
```

## Cómo reproducirlo

1. Clonar el repositorio:

   ```
   git clone https://github.com/TU_USUARIO/NOMBRE_DEL_REPO.git
   cd NOMBRE_DEL_REPO
   ```

2. Instalar las dependencias:

   ```
   python -m pip install pandas matplotlib
   ```

3. Descargar el dataset desde Kaggle y copiar los CSV en la carpeta `csv/`.

4. Ejecutar un script desde la raíz del proyecto:

   ```
   python codigo/NOMBRE_DEL_SCRIPT.py
   ```

## Tecnologías

- Python 3
- pandas
- matplotlib

## Posibles mejoras

- Segmentación de clientes con RFM (recencia, frecuencia y valor monetario).
- Modelo simple para predecir si un pedido se entregará tarde.
- Dashboard interactivo con Streamlit.
- Cargar los datos en una base SQL y hacer las consultas con SQL antes de pasar a pandas.

## Autor

**Valentín** · Estudiante de Analista en Sistemas

[GitHub](https://github.com/Valentin-Justel5/Proyecto-Analisis-de-datos)
