# thanks shanelynne  from https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/
import pandas as pd
import dateutil

# Load data from csv file
data = pd.DataFrame.from_csv('phone_data.csv')
# Convert date from string to date times
data['date'] = data['date'].apply(dateutil.parser.parse, dayfirst=True)