import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv(r"C:\Users\kuche\OneDrive\Desktop\CAMPAIGN_DATA.csv")

# Create channel summary
channel_summary = df.groupby('Channel').agg({
    'Impressions': 'sum',
    'Clicks': 'sum',
    'Conversions': 'sum',
    'Spend': 'sum'
})

channel_summary['CTR'] = (channel_summary['Clicks'] / channel_summary['Impressions']) * 100
channel_summary['CVR'] = (channel_summary['Conversions'] / channel_summary['Clicks']) * 100
channel_summary['CPC'] = channel_summary['Spend'] / channel_summary['Clicks']
channel_summary['CPA'] = channel_summary['Spend'] / channel_summary['Conversions']
channel_summary['ROAS'] = (channel_summary['Conversions'] * 100) / channel_summary['Spend']


channel_summary['CTR'].plot(kind='bar')

plt.title('CTR by Channel')
plt.ylabel('CTR (%)')
plt.xlabel('Channel')
plt.show()

channel_summary['CVR'].plot(kind='bar')

plt.title('CVR by Channel')
plt.ylabel('CVR (%)')
plt.xlabel('Channel')
plt.show()

channel_summary['CPA'].plot(kind='bar')

plt.title('CPA by Channel')
plt.ylabel('CPA')
plt.xlabel('Channel')
plt.show()

channel_summary['ROAS'].plot(kind='bar')

plt.title('ROAS by Channel')
plt.ylabel('ROAS')
plt.xlabel('Channel')
plt.show()

daily_clicks = df.groupby('Date')['Clicks'].sum()

daily_clicks.plot(kind='line', marker='o')

plt.title('Daily Click Trend')
plt.ylabel('Clicks')
plt.xlabel('Date')
plt.xticks(rotation=45)
plt.show()

daily_conversions = df.groupby('Date')['Conversions'].sum()

daily_conversions.plot(kind='line', marker='o')

plt.title('Daily Conversion Trend')
plt.ylabel('Conversions')
plt.xlabel('Date')
plt.xticks(rotation=45)
plt.show()

daily_spend = df.groupby('Date')['Spend'].sum()

daily_spend.plot(kind='line', marker='o')

plt.title('Daily Spend Trend')
plt.ylabel('Spend')
plt.xlabel('Date')
plt.xticks(rotation=45)
plt.show()

channel_summary[['Clicks', 'Conversions']].plot(kind='bar')

plt.title('Clicks vs Conversions by Channel')
plt.ylabel('Count')
plt.xlabel('Channel')
plt.xticks(rotation=0)
plt.show()