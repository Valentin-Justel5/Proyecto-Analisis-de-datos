import pandas as pd #importo pandas

#leo el csv
df = pd.read_csv('csv/olist_customers_dataset.csv')

# 1er paso 
# verificar cuantas filas y columnas tengo
#df.shape #  filas y columnas (99441, 5)
#print(f' Filas: {df.shape[0]} , Columnas: {df.shape[1]} ' )


# 2do paso 
# verifico si los tipos de datos son correctos
#print(df.dtypes)
#print()
#print('--INFO--')
#print(df.info()) 

# 3er paso 
# Verificar si hay datos nulos
#nulos = df.isna().sum()
#print(f'Nulos: {nulos}')
#print()

# 4to paso 
# Checkeamos que los rangos tengan sentido
#print(df.describe())

# 5to paso
# ¿cuánta variedad tiene cada columna?
#print(df.nunique())

# 6to paso
# mirar filas

print("Primeras filas:")
print(df.head())
print()
print("Muestra aleatoria (2 filas):")
print(df.sample(2, random_state=42))