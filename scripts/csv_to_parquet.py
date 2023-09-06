import pandas as pd

csv_file = '../data/austin_weather.csv'
parquet_file = '../data/austin_weather.parquet'

csv_stream = pd.read_csv(csv_file, sep=',', low_memory=False)
selected_columns = csv_stream[['DATE', 'HourlyDryBulbTemperature']].copy()
selected_columns.columns = ['date', 'temperature']
selected_columns['date'] = pd.to_datetime(selected_columns['date'], format='%Y-%m-%dT%H:%M:%S')
selected_columns.dropna().to_parquet(parquet_file)
