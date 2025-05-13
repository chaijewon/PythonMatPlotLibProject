import numpy as np
import pandas as pd
data=[['사과',3000],
      ['배',5000],
      ['딸기',4000],
      ['귤',5000],
      ['사과',3000],
      ['배',5000]
     ]
f=[x[0] for x in data]
p=[x[1] for x in data]
print(f)
print(p)
df=pd.DataFrame({
    "과일":f,
    "가격":p
})
print(df)
new_df=df.drop_duplicates()
print(new_df)
df['순서']=range(len(f))
print(df.drop_duplicates())
print(df.drop_duplicates(['가격']))
