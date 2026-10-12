import pandas as pd


# ¿Qué porcentaje de clientes compra más de una vez?
# Tablas: orders + customers (para customer_unique_id) + order_items (para los ingresos)

orders = pd.read_csv('csv/olist_orders_dataset.csv')
customers = pd.read_csv('csv/olist_customers_dataset.csv')
items = pd.read_csv('csv/olist_order_items_dataset.csv')

# --- 1. Exploración ---
print("=== ESTADOS ===")
print(orders['order_status'].value_counts())
print("\n=== customer_id vs customer_unique_id ===")
print(f"customer_id distintos:        {customers['customer_id'].nunique()}")
print(f"customer_unique_id distintos: {customers['customer_unique_id'].nunique()}")

# --- 2. Limpieza: sacar pedidos que no son ventas ---
orders = orders[~orders['order_status'].isin(['canceled', 'unavailable'])]

# --- 3. Unir para tener el cliente real (customer_unique_id) en cada pedido ---
df = orders.merge(customers[['customer_id', 'customer_unique_id']], on='customer_id')

# --- 4. Pedidos distintos por cliente ---
compras = df.groupby('customer_unique_id')['order_id'].nunique()

total_clientes = len(compras)
recurrentes = (compras > 1).sum()

print("\n=== RECOMPRA ===")
print(f"Clientes totales:     {total_clientes}")
print(f"Clientes recurrentes: {recurrentes}")
print(f"% que compró más de una vez: {recurrentes / total_clientes * 100:.2f}%")

dist = compras.clip(upper=4).value_counts().sort_index()
dist = dist.rename({1: '1 compra', 2: '2 compras', 3: '3 compras', 4: '4 o más'})
print("\n=== CLIENTES SEGÚN CANTIDAD DE COMPRAS ===")
print(pd.DataFrame({'clientes': dist, '%': (dist / total_clientes * 100).round(2)}))

# --- 5. Extra: ¿cuánto pesan los recurrentes en los ingresos? ---
ingreso_pedido = (
    items.groupby('order_id', as_index=False)['price'].sum()
    .rename(columns={'price': 'ingresos'})
)
df = df.merge(ingreso_pedido, on='order_id', how='left')

por_cliente = df.groupby('customer_unique_id').agg(
    compras=('order_id', 'nunique'),
    ingresos=('ingresos', 'sum'),
)
por_cliente['recurrente'] = por_cliente['compras'] > 1

peso = por_cliente.groupby('recurrente')['ingresos'].sum() / por_cliente['ingresos'].sum() * 100
print("\n=== % DE LOS INGRESOS SEGÚN TIPO DE CLIENTE ===")
print(peso.rename({False: 'Compró una vez', True: 'Recurrente'}).round(2))

ticket = por_cliente.groupby('recurrente')['ingresos'].mean()
print("\n=== GASTO TOTAL PROMEDIO POR CLIENTE (R$) ===")
print(ticket.rename({False: 'Compró una vez', True: 'Recurrente'}).round(2))
