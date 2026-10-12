import pandas as pd

customers = pd.read_csv('csv/olist_customers_dataset.csv')
orders = pd.read_csv('csv/olist_orders_dataset.csv')
items = pd.read_csv('csv/olist_order_items_dataset.csv')

# --- 1. Explorar antes de tocar nada ---
print(customers.columns)
print(customers.isna().sum())
print(orders['order_status'].value_counts())

# --- 2. Filtrar pedidos que no son ventas reales ---
orders = orders[~orders['order_status'].isin(['canceled', 'unavailable'])]

# --- 3. Unir: orders -> customers -> items ---
df = orders.merge(customers, on='customer_id')
print(f'En clientes Filas: {df.shape}, Columnas: {df.shape}')                     # chequeo: ¿se perdieron o duplicaron filas?
df = df.merge(items, on='order_id')
print(f' En items Filas: {df.shape}, Columnas: {df.shape}')


# --- 4. Normalizar ciudades (solo si vas a usar ciudades) ---
df['customer_city'] = df['customer_city'].str.strip().str.lower()

# --- 5. Resumen por estado ---
por_estado = df.groupby('customer_state').agg(
    clientes=('customer_unique_id', 'nunique'),       # ojo: customer_unique_id, no customer_id
    ingresos=('price', 'sum'),
)

por_estado['%_clientes'] = por_estado['clientes'] / por_estado['clientes'].sum() * 100
por_estado['%_ingresos'] = por_estado['ingresos'] / por_estado['ingresos'].sum() * 100
por_estado = por_estado.sort_values('ingresos', ascending=False)
print('==== RESUMEN POR ESTADO =====')
print()
print(por_estado.round(2))

# --- 6. Top 10 ciudades (opcional) ---
por_ciudad = df.groupby('customer_city').agg(
    clientes=('customer_unique_id', 'nunique'),
    ingresos=('price', 'sum'),
).sort_values('ingresos', ascending=False).head(10)
print('===== TOP 10 CIUDADES =====')
print()
print(por_ciudad.round(2))

'''==== RESUMEN POR ESTADO =====

                clientes    ingresos  %_clientes  %_ingresos
customer_state                                              
SP                 39747  5163867.22       41.83       38.27
RJ                 12241  1811623.42       12.88       13.43
MG                 11134  1573508.20       11.72       11.66
RS                  5233   742559.78        5.51        5.50
PR                  4824   676883.06        5.08        5.02
SC                  3501   518578.28        3.68        3.84
BA                  3244   507108.83        3.41        3.76
DF                  2057   300886.45        2.16        2.23
GO                  1934   287870.46        2.04        2.13
ES                  1950   273532.13        2.05        2.03
PE                  1600   261739.94        1.68        1.94
CE                  1301   226264.06        1.37        1.68
PA                   944   178821.12        0.99        1.33
MT                   872   156313.53        0.92        1.16
MA                   715   119291.62        0.75        0.88
MS                   687   116754.65        0.72        0.87
PB                   516   114874.10        0.54        0.85
PI                   478    86660.09        0.50        0.64
RN                   471    83034.98        0.50        0.62
AL                   399    80314.81        0.42        0.60
SE                   338    58920.85        0.36        0.44
TO                   271    49407.99        0.29        0.37
RO                   234    46031.64        0.25        0.34
AM                   142    22356.84        0.15        0.17
AC                    77    15982.95        0.08        0.12
AP                    67    13474.30        0.07        0.10
RR                    44     7739.44        0.05        0.06
===== TOP 10 CIUDADES =====

                clientes    ingresos
customer_city                       
sao paulo          14761  1897019.80
rio de janeiro      6545   986528.05
belo horizonte      2641   350760.93
brasilia            2051   300202.76
curitiba            1447   208008.66
campinas            1379   186925.85
porto alegre        1317   186788.31
salvador            1199   180735.72
guarulhos           1133   142578.38
niteroi              804   117487.43'''