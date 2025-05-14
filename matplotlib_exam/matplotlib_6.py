"""
  6~7  => 10중순 => 3
  사용기술

  BackEnd : Java , Python , JSP ,
            ThymeLeaf , Numpy , Pandas , Matplotlib
            MyBatis JPA
  FrontEnd : HTML5,JavaScript(ES6)
            Jquery , Ajax , VueJs , Vuex , Pinia
            React , React-Query , Redux , Next
            NodeJS

  Framework : Spring , Spring-Boot , Django
  database : oracle21c / mysql3 / sqlite3
  AWS , Docker , CI/CD

  => Spring-Boot : MySql , JPA
     => React , 타임리프 (CI/CD)
                ---------------
  => 희망부서
     SI/SM => Java웹개발
     -----------------
     솔루션
     프레임워크 : AI
     ----------------- SW개발
     Java웹개발/SW개발
     이력서용 / PPT
"""
import os
import sys
import urllib.request
import json
client_id = "OtKU74j2Bx_QN_K5YPck"
client_secret = "eyn6LY7L0j"
fd=input("검색어 입력:")
encText = urllib.parse.quote(fd)
url = "https://openapi.naver.com/v1/search/news.json?display=100&query=" + encText # JSON 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)

json_data=json.loads(response_body)
print(json_data)
for news in json_data['items']:
    print(news['description'])



