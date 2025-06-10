import pandas as pd
import numpy as np

# Crear datos de ejemplo
np.random.seed(42)
data = {
    'Fecha': pd.date_range(start='2023-01-01', periods=100),
    'Producto': np.random.choice(['Camiseta', 'Pantalón', 'Zapatos', 'Sombrero', 'Bufanda'], 100),
    'Cantidad': np.random.randint(1, 20, 100),
    'Precio_Unitario': np.round(np.random.uniform(10, 100, 100), 2),
    'Region': np.random.choice(['Norte', 'Sur', 'Este', 'Oeste'], 100),
    'Cliente': ['Cliente_' + str(i) for i in range(100)]
}

# Crear DataFrame
df = pd.DataFrame(data)

# Calcular venta total
df['Venta_Total'] = df['Cantidad'] * df['Precio_Unitario']

# Guardar como CSV
df.to_csv('datos_ventas.csv', index=False)

print("Archivo CSV generado exitosamente: datos_ventas.csv")



  