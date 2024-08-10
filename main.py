# Package imports
import pandas as pd                

def IQR(column): 
    q25, q75 = column.quantile([0.25, 0.75])
    return q75-q25

# Load the data from London Bridge
lb = pd.read_csv('data/10-11_London_Bridge.txt') # Comma-separated .txt file

# Take only the first three columns
df = lb.iloc[:, :3]

# Rename columns
df.columns = ['datetime', 'water_level', 'is_high_tide']

# Convert to datetime
df['datetime'] = pd.to_datetime(df['datetime'])

# Convert to float
df['water_level'] = df.water_level.astype(float)

# Create extra month and year columns for easy access
df['month'] = df['datetime'].dt.month
df['year'] = df['datetime'].dt.year

# Filter df for high and low tide
tide_high = df[df['is_high_tide'] == 1]
tide_low = df[df['is_high_tide'] == 0]

# Create summary statistics
high_statistics = tide_high['water_level'].agg(['mean', 'median', IQR])
low_statistics = tide_low['water_level'].agg(['mean', 'median', IQR])

# Calculate ratio of high tide days
all_high_days = tide_high.groupby('year')['water_level'].count()
very_high_days = tide_high[tide_high['water_level'] > tide_high['water_level'].quantile(0.90)].groupby('year')['water_level'].count()
very_high_ratio = (very_high_days/all_high_days).reset_index()

# Calculate ratio of low tide days
all_low_days = tide_low.groupby('year')['water_level'].count()
very_low_days = tide_low[tide_low['water_level'] < tide_low['water_level'].quantile(0.10)].groupby('year')['water_level'].count()
very_low_ratio = (very_low_days/all_low_days).reset_index()

solution = {'high_statistics': high_statistics, 'low_statistics': low_statistics, 'very_high_ratio': very_high_ratio, 'very_low_ratio':very_low_ratio}
print(solution)
