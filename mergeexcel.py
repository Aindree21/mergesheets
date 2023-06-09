import pandas as pd

excel1 = 'workbook1.xlsx'
excel2 = 'workbook2.xlsx'

df1 = pd.read_excel(excel1)
df2 = pd.read_excel(excel2)

print(df1)
print(df2)

values1 = df1[['Name','Team Name','User ID']]
values2 = df2[['name','uid','total_statements','total_reasons']]

dataframes = [values1,values2]

join = pd.concat(dataframes)

join.to_excel("output.xlsx")