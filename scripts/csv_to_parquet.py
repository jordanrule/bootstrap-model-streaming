import pandas as pd

csv_file = '../data/austin_weather.csv'
parquet_file = '../data/austin_weather.parquet'

csv_stream = pd.read_csv(csv_file, sep=',', low_memory=False)
csv_stream.to_parquet(parquet_file)
