from turtle import pd
import pandas as pd
import plotly.graph_objects as gp

df=pd.read_csv('C:/Users/w/Desktop/Python/csv/data2project.csv')

x=df.loc[df['student_id']=='TRL_abc'].groupby('level')['attempt'].mean()

print(x)
fig=gp.Figure(gp.Bar(x=x,y=['level1','level2','level3','level4'],orientation='h'))
fig.show()