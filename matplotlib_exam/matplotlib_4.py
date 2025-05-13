import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import oracledb as db
#emp=pd.read_csv('c:/pydata/EMP.csv')
"""
result=emp.groupby('DEPTNO')['SAL'].mean().reset_index()
print(result)
result.plot.bar(x='DEPTNO',figsize=(8,5))
# margin-top margin-left
plt.show()
"""
"""
print(emp)
emp['HIREDATE']=emp['HIREDATE'].str[:4]
print(emp['HIREDATE']) 
# 1981/01/08
"""
conn=db.connect('hr/happy@localhost:1521/xe')
cur=conn.cursor()
sql="""
      SELECT empno,ename,job,mgr,TO_CHAR(hiredate,'YYYY'),
      sal,comm,deptno FROM emp
    """
cur.execute(sql)

emp=cur.fetchall()
cur.close()
conn.close()
print(emp)
columns=['empno','ename','job','mgr','hiredate','sal','comm','deptno']
emp_df=pd.DataFrame(emp,columns=columns)
print(emp_df)
print(emp_df['hiredate'])
sns.barplot(x='deptno',y='sal',hue='hiredate',data=emp_df)
plt.show()