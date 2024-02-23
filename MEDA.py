import numpy as np 
import pandas as pd 
import plotly.express as px 

df = pd.read_csv('Sources/fifa_eda.csv')

df.dropna(inplace= True)
df.reset_index(inplace= True, drop= True)

df.columns = df.columns.str.strip().str.lower()
df.columns = df.columns.str.replace(' ', '_')

df_top_25_count = df.groupby('nationality')['id'].count().sort_values(ascending= False).reset_index().head(25)
df_top_25 = df[df.nationality.isin(df_top_25_count.nationality.unique())].reset_index(drop= True)

def best_10_players(col):
    df_top_10 = df_top_25.sort_values(by= col, ascending= False).head(10)
    fig = px.bar(df_top_10, x= 'name', y= col, color= col, color_continuous_scale= 'purp', \
                hover_data= ['club', 'nationality', 'preferred_foot', 'position'])
    fig.update_layout(title= {'text': f'Best 10 {col}', 'x': 0.5, 'y': 0.95})
    return fig