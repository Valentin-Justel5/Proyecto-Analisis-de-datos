import pandas as pd

df = pd.read_csv('csv/olist_orders_dataset.csv')

# --- Exploración ---
print("=== SHAPE ===")
print(df.shape)
print("\n=== DTYPES ===")
print(df.dtypes)
print("\n=== NULOS ===")
print(df.isna().sum())
print("\n=== ESTADOS ===")
print(df['order_status'].value_counts())

# --- Convertir fechas ---
columnas_fecha = [
    'order_purchase_timestamp',
    'order_approved_at',
    'order_delivered_carrier_date',
    'order_delivered_customer_date',
    'order_estimated_delivery_date',
]
for col in columnas_fecha:
    df[col] = pd.to_datetime(df[col])

# --- Quedarse con pedidos que tienen fecha de entrega ---
entregados = df.dropna(subset=['order_delivered_customer_date']).copy()
print(f"\nPedidos con fecha de entrega: {len(entregados)} de {len(df)}")

# --- Cálculos en días ---
entregados['dias_entrega'] = (
    entregados['order_delivered_customer_date'] - entregados['order_purchase_timestamp']
).dt.total_seconds() / 86400

entregados['desvio_dias'] = (
    entregados['order_delivered_customer_date'] - entregados['order_estimated_delivery_date']
).dt.total_seconds() / 86400

# --- Resultados ---
print("\n=== TIEMPO DE ENTREGA (compra -> entrega) ===")
print(f"Promedio: {entregados['dias_entrega'].mean():.1f} días")
print(f"Mediana:  {entregados['dias_entrega'].median():.1f} días")

print("\n=== DESVÍO RESPECTO A LA FECHA ESTIMADA ===")
print(f"Promedio: {entregados['desvio_dias'].mean():.1f} días (negativo = llegó antes)")
print(f"Mediana:  {entregados['desvio_dias'].median():.1f} días")
print(f"Pedidos que llegaron tarde: {(entregados['desvio_dias'] > 0).mean() * 100:.1f}%")