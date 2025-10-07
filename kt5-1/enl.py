import pandas as pd
from hdfs import InsecureClient

# Настройка HDFS клиента
client = InsecureClient('http://localhost:9870', user='root')

# Чтение CSV
df = pd.read_csv('yellow_tripdata_small_2015-01.csv')

# Очистка: удаляем пустые строки и дубликаты
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# Сохраняем очищенный файл
df.to_csv('cleaned.csv', index=False)

# Загрузка в HDFS
client.upload('/cleaned.csv', 'cleaned.csv', overwrite=True, namenoderpcaddress='localhost:9000')

print("Файл загружен в HDFS")
