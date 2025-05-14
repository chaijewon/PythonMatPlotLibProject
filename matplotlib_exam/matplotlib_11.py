import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import oracledb as db


fno=int(input("맛집 번호 입력:"))
conn=db.connect("hr/happy@localhost:1521/xe")
cur=conn.cursor()
sql=f"""
      SELECT content FROM project_food
      WHERE fno={fno}
    """
cur.execute(sql)
food=cur.fetchone()
#CLOB => Java(CLOB=>String) BLOB/BFILE=>InputStream
content=''.join(food[0].read())
cur.close()
conn.close()
print(content)
font_path="c:/pydata/NanumGothic.ttf"
wc=WordCloud(max_font_size=200,
        background_color="white",
        width=800,height=800,
        font_path=font_path)
wc.generate(content)
plt.figure(figsize=(10,8))
plt.imshow(wc)
plt.tight_layout(pad=0)
plt.axis('off')
plt.show()
# 이미지화 => 한개의 이미지 (속도가 느리다)
"""
   JSP / Spring Framework 
   -----------------------
   파이썬 / ElasticSearch => 가볍게 
   개인 프로젝트 : 단순하게 
      => 목록 / 페이징 / 쿠키 / 세션 
      => CRUD 
"""



