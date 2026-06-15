import pandas as pd

#Load dataset
df = pd.read_csv(r"C:\Users\kuche\OneDrive\Desktop\CAMPAIGN_DATA.csv")
print(df.head(5))

# Check dataset information
print("\nDataset Info:")
print(df.info())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Calculate KPIs
df['CTR'] = (df['Clicks'] / df['Impressions']) * 100
df['CVR'] = (df['Conversions'] / df['Clicks']) * 100
df['CPC'] = df['Spend'] / df['Clicks']
df['CPA'] = df['Spend'] / df['Conversions']
df['ROAS'] = (df['Conversions'] * 100) / df['Spend']

# Display KPI results
print("\nCampaign KPI Analysis:")
print(df[['Date', 'Channel', 'CTR', 'CVR', 'CPC', 'CPA', 'ROAS']])

# Summary statistics
print("\nKPI Summary:")
print(df[['CTR', 'CVR', 'CPC', 'CPA', 'ROAS']].describe())

# Funnel analysis
funnel = df.groupby("Channel")[["Impressions", "Clicks", "Conversions"]].sum()

print("\n--- Funnel View ---")
print(funnel)

# Channel-wise KPI Summary

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

print("\nChannel Performance:")
print(channel_summary.round(2))

# Save output
df.to_csv(r"C:\Users\kuche\OneDrive\Desktop\Campaign_KPI_Report.csv", index=False)

print("\nAnalysis completed successfully!")
