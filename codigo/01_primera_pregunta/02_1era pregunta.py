import pandas as pd

orders = pd.read_csv('csv/olist_orders_dataset.csv', parse_dates=['order_purchase_timestamp'])
items = pd.read_csv('csv/olist_order_items_dataset.csv')

orders = orders[~orders['order_status'].isin(['canceled', 'unavailable'])]
print(orders['order_status'].value_counts())

df = orders.merge(items, on='order_id', how='inner')


