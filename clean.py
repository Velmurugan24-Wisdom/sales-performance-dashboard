import pandas as pd

df = pd.read_csv(r'C:\Users\velmu\Downloads\SalesAnalysis.csv')
df = df.dropna()
df = df[df['Order ID'] != 'Order ID']
df['Quantity Ordered'] = pd.to_numeric(df['Quantity Ordered'], errors='coerce')
df['Price Each'] = pd.to_numeric(df['Price Each'], errors='coerce')
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%y %H:%M')
df['Revenue'] = df['Quantity Ordered'] * df['Price Each']
df['Month_Num'] = df['Order Date'].dt.month
df['Month_Name'] = df['Order Date'].dt.strftime('%b')
df['City'] = df['Purchase Address'].str.extract(r', ([^,]+),')
df = df.dropna(subset=['Revenue'])

df.to_csv(r'C:\Users\velmu\Downloads\clean_sales.csv', index=False)
print('Done! Rows exported:', len(df))
print(df[['Order ID', 'Revenue', 'Month_Num', 'Month_Name', 'City']].head())
