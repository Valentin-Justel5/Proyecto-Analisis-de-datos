import pandas as pd

# Dataset de suscriptores (simulado con errores reales)
df = pd.read_csv('csv/olist_order_payments_dataset.csv')


# --- Exploración ---
print("=== SHAPE ===")
print(df.shape)
print("\n=== DTYPES ===")
print(df.dtypes)
print("\n=== NULOS ===")
print(df.isna().sum())
print("\n=== DESCRIBE ===")
print(df.describe())
print("\n=== MEDIOS DE PAGO ===")
print(df['payment_type'].value_counts())

# --- Limpieza ---
df = df[df['payment_type'] != 'not_defined']   # medio de pago no real
df = df[df['payment_value'] > 0]               # pagos en cero


# --- Ticket por pedido y medio de pago ---
# Si un pedido se pagó en cuotas/partes, suma todas sus filas antes de promediar
por_pedido = df.groupby(['order_id', 'payment_type'], as_index=False)['payment_value'].sum()


    
resumen = df.groupby('payment_type').agg(
    pedidos=('order_id', 'nunique'),
    ticket_promedio  =('payment_value', 'mean')
    
).sort_values('pedidos', ascending=False)



