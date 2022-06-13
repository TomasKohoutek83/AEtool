import pandas as pd
import openpyxl

df = pd.read_excel('Duben.xlsx')
#print(df.columns)
#print(df['Unnamed: 1'])

print(df[['Order','Operation short text']])









