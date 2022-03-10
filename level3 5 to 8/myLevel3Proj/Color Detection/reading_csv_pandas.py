import pandas as pd
df=pd.read_csv("NSE.csv")
# print(df)
# print("---------------------------------------------------------")
# print(df.head())
# print("---------------------------------------------------------")
# print(df.tail())
# print("---------------------------------------------------------")
# print(df.head(10))#going to give you 10 rows of data

largeVolume=df[    (  df['Volume (lacs)']>200  )   ]

# print(len(largeVolume))

print(df['Volume (lacs)'])
# largeVolume.to_csv("largeVolume_nse.csv")