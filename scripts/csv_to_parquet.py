import pandas as pd

csv_file = '../data/austin_weather.csv'
parquet_file = '../data/austin_weather.parquet'

csv_stream = pd.read_csv(csv_file, sep=',', low_memory=False)
selected_columns = csv_stream[['DATE', 'HourlyDryBulbTemperature']].copy()
selected_columns.columns = ['date', 'temperature']
selected_columns['date'] = pd.to_datetime(selected_columns['date'], format='%Y-%m-%dT%H:%M:%S')
selected_columns['time'] = selected_columns['date'].dt.time
selected_columns['temperature'] = pd.to_numeric(selected_columns['temperature'], errors='coerce')
selected_columns['location'] = 'Austin'
selected_columns.dropna().to_parquet(parquet_file)
selected_columns.dropna().to_csv(parquet_file + ".csv")