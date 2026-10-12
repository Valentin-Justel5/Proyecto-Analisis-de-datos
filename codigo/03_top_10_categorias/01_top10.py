import pandas as pd


orders = pd.read_csv('csv/olist_orders_dataset.csv')
items = pd.read_csv('csv/olist_order_items_dataset.csv')
products = pd.read_csv('csv/olist_products_dataset.csv')

# 1. Quedarse con los pedidos que no están cancelados ni no disponibles
orders = orders[orders['order_status'].isin(['canceled', 'unavailable'])]

# 2. Unir: orders -> items -> products
df = orders.merge(items, on='order_id')
df = df.merge(products[['product_id', 'product_category_name']], on='product_id')

# 3. Tratar categorías nulas
df['product_category_name'] = df['product_category_name'].fillna('sin_categoria')

# 4. Sumar price por categoría y quedarse con las 10 mayores
top10 = df.groupby('product_category_name')['price'].sum().sort_values(ascending=False).head(10)
print('=== TOP 10 CATEGORIAS CON MAS VENTAS ===')
print(top10)

'''=== TOP 10 CATEGORIAS CON MAS VENTAS ===
product_category_name
cool_stuff                14520.36
esporte_lazer              8308.05
informatica_acessorios     7632.30
relogios_presentes         6820.47
automotivo                 6134.38
utilidades_domesticas      5422.86
ferramentas_jardim         4246.52
brinquedos                 4138.06
instrumentos_musicais      3710.44
eletronicos                3167.20'''