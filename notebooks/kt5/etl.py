import pandas as pd
from hdfs import InsecureClient

# Настройки HDFS
hdfs_url = "http://namenode:9870"
hdfs_user = "jupiter"
hdfs_path = "/home/jovyan/kt5/data/cleaned_data.csv"

# Локальный CSV
local_csv = "file:///home/jovyan/kt5/data.csv"

# 1. Загрузка CSV
df = pd.read_csv(local_csv)

# 2. Очистка данных
df.dropna(inplace=True)        # Удаляем пустые строки
df.drop_duplicates(inplace=True)  # Удаляем дубликаты

# 3. Подключение к HDFS и загрузка
client = InsecureClient(hdfs_url, user=hdfs_user)
with client.write(hdfs_path, encoding='utf-8', overwrite=True) as writer:
    df.to_csv(writer, index=False)

print(f"Данные загружены в HDFS по пути {hdfs_path}")
