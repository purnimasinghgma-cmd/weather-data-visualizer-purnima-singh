import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/alokranjansingh/Downloads/weather_data.csv")

df.fillna(method='ffill', inplace=True)

df['Date'] = pd.to_datetime(df['Date'])

data = df[['Date', 'Temperature', 'Rainfall', 'Humidity']]

daily_stats = data.groupby('Date').agg({
    'Temperature': ['mean', 'min', 'max', 'std'],
    'Rainfall': ['sum'],
    'Humidity': ['mean']
})

monthly_stats = data.set_index('Date').resample('M').agg({
    'Temperature': ['mean', 'min', 'max', 'std'],
    'Rainfall': ['sum'],
    'Humidity': ['mean']
})

plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.plot(data['Date'], data['Temperature'], label='Daily Temp')
plt.title('Daily Temperature Trend')
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.legend()

plt.subplot(2, 2, 3)
plt.bar(monthly_stats.index, monthly_stats[('Rainfall', 'sum')])
plt.title('Monthly Rainfall Total')
plt.xlabel('Month')
plt.ylabel('Rainfall')

plt.subplot(2, 2, 4)
plt.scatter(data['Humidity'], data['Temperature'], alpha=0.5)
plt.title('Humidity vs Temperature')
plt.xlabel('Humidity')
plt.ylabel('Temperature')

plt.tight_layout()
plt.savefig("weather_visualizations.png")

data['Month'] = data['Date'].dt.month
monthly_grouped = data.groupby('Month').agg({
    'Temperature': ['mean', 'max', 'min'],
    'Rainfall': 'sum',
    'Humidity': 'mean'
})

data.to_csv("cleaned_weather_data.csv", index=False)

plt.show()
