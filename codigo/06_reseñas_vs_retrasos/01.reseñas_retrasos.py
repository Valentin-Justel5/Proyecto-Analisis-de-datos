import pandas as pd


# ¿Los retrasos en la entrega afectan la puntuación de las reseñas?
# Tablas: orders (fechas) + order_reviews (puntaje), unidas por order_id

orders = pd.read_csv(
    'csv/olist_orders_dataset.csv',
    parse_dates=['order_delivered_customer_date', 'order_estimated_delivery_date'],
)
reviews = pd.read_csv(
    'csv/olist_order_reviews_dataset.csv',
    parse_dates=['review_answer_timestamp'],
)

# --- 1. Exploración ---
print("=== PUNTAJES ===")
print(reviews['review_score'].value_counts().sort_index())
print("\n=== PEDIDOS CON MÁS DE UNA RESEÑA ===")
print(reviews['order_id'].duplicated().sum())

# --- 2. Limpieza ---
# Algunos pedidos tienen varias reseñas: me quedo con la última de cada uno
reviews = (
    reviews.sort_values('review_answer_timestamp')
    .drop_duplicates(subset='order_id', keep='last')
)

# Solo pedidos que ya llegaron al cliente (sin fecha de entrega no hay retraso que medir)
entregados = orders.dropna(subset=['order_delivered_customer_date']).copy()

# --- 3. Calcular el desvío en días y clasificar ---
entregados['desvio_dias'] = (
    entregados['order_delivered_customer_date'] - entregados['order_estimated_delivery_date']
).dt.total_seconds() / 86400

entregados['llego_tarde'] = entregados['desvio_dias'] > 0

entregados['tramo'] = pd.cut(
    entregados['desvio_dias'],
    bins=[-float('inf'), 0, 3, 7, float('inf')],
    labels=['A tiempo o antes', 'Tarde hasta 3 días', 'Tarde 3 a 7 días', 'Tarde más de 7 días'],
)

# --- 4. Unir con las reseñas ---
df = entregados.merge(reviews[['order_id', 'review_score']], on='order_id', how='inner')
print(f"\nPedidos entregados con reseña: {len(df)}")

# --- 5. Resultados ---
print("\n=== PUNTAJE PROMEDIO: TARDE VS A TIEMPO ===")
print(df.groupby('llego_tarde')['review_score'].agg(pedidos='count', puntaje_promedio='mean').round(2))

por_tramo = df.groupby('tramo', observed=True)['review_score'].agg(
    pedidos='count',
    puntaje_promedio='mean',
)
print("\n=== PUNTAJE PROMEDIO POR TRAMO DE RETRASO ===")
print(por_tramo.round(2))

dist = pd.crosstab(df['tramo'], df['review_score'], normalize='index') * 100
print("\n=== DISTRIBUCIÓN DE PUNTAJES POR TRAMO (%) ===")
print(dist.round(1))

corr = df['desvio_dias'].rank().corr(df['review_score'].rank())
print(f"\nCorrelación (Spearman) entre desvío y puntaje: {corr:.2f}")
