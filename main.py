# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 12:07:09 2021

@author: anaka
"""

import connection as conn
import queries as sql
import pandas as pd
import dash
import json
import numpy as np
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
from dash.dependencies import Input, Output
from plotly.subplots import make_subplots

conn = conn.Connection()  # datos para la conexión

# estilo de bootstrap
external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]

# instancia de Dash
app = dash.Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)

# Total de ingresos por cultivo
conn.openConnection()
query = pd.read_sql_query(sql.getbyGender(), conn.connection)
conn.closeConnection()



query['name_event'] = query['name_event'].apply(lambda x: x.replace('\'','').replace('s','').split(' ')[0]) #str.split(' ')[0]

obj1 = query[query['name_event'] == "Men"]['name_discipline']
obj2 = query[query['name_event'] == "Men"]['number_of_events']

obj3 = query[query['name_event'] == "Women"]['name_discipline']
obj4 = query[query['name_event'] == "Women"]['number_of_events']


figBarIncome1 = go.Figure(
    data=[
        go.Bar(name='Male', x=obj1,
               y= obj2, yaxis='y', offsetgroup=1),
        go.Bar(name='Female', x= obj3,
               y= obj4, yaxis='y', offsetgroup=2)

    ],
    layout={
        'yaxis': {'title': 'Number of Events'},
        'yaxis2': {'title': 'Number of Events', 'overlaying': 'y', 'side': 'right'}
    }
)
conn.openConnection()
query1 = pd.read_sql_query(sql.getMedalsby(), conn.connection)
conn.closeConnection()

figBarIncome2 = go.Figure(
    data=[
        go.Bar(name='Medallas', x=query1['name_country'],
               y= query1['medals_total'], yaxis='y', offsetgroup=1),
        go.Bar(name='Atletas', x=query1['name_country'],
               y=query1['number_of_athletes'], yaxis='y', offsetgroup=2)

    ],
    layout={
        'yaxis': {'title': 'Number of Medals/Number of Athletes'},
        'yaxis2': {'title': 'Number of Medals/Number of Athletes', 'overlaying': 'y', 'side': 'right'}
    }
)

ratio = list(query1['medals_total']/query1['number_of_athletes'])
p = 1/11.16
medals = [p*np.exp(-i*p) for i in query1['medals_total']]
print(sum(ratio)/len(ratio))
  
figBarIncome3 = px.imshow([ratio,medals],x=list(query1['name_country']),y=['ratio','m'])

conn.openConnection()
query2 = pd.read_sql_query(sql.getCoachesandMedals(), conn.connection)
conn.closeConnection()

figBarIncome4 = go.Figure(
    data=[
        go.Bar(name='Medallas', x=query2['name_country'],
               y= query2['medals_total'], yaxis='y', offsetgroup=1),
        go.Bar(name='Coaches', x=query2['name_country'],
               y=query2['number_of_coaches'], yaxis='y', offsetgroup=2)

    ],
    layout={
        'yaxis': {'title': 'Number of Medals/Number of Coaches'},
        'yaxis2': {'title': 'Number of Medals/Number of Coaches', 'overlaying': 'y', 'side': 'right'}
    }
)

conn.openConnection()
query3 = pd.read_sql_query(sql.getEventsbyDis(), conn.connection)
conn.closeConnection()

figBarIncome5 = go.Figure(
    data=[
        go.Bar(name='Eventor por disciplina', x=query3['name_discipline'], 
                y=query3['number_of_events'])
                ], 
         
         layout={'yaxis': {'title' : 'Eventos por disciplina'}})
                          

conn.openConnection()
query4 = pd.read_sql_query(sql.getSuccessRate(), conn.connection)
conn.closeConnection()

query4['SuccesR']= query1['medals_total']*100/(query1['number_of_athletes']*query2['number_of_coaches']*0.5)

dfCases = pd.DataFrame(query4, columns=['name_country','SuccesR'])
figBarCases = px.bar(query4, x=query4['name_country'], y=query4['SuccesR'])
figMapCases = px.choropleth(dfCases, locations='name_country' ,
 locationmode= 'country names',
 color='SuccesR',

 hover_name='name_country',
 color_continuous_scale=["#99ccff", "#ff3333"])





app.layout = html.Div(children=[
    
    

    html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("JUEGOS OLIMPICOS TOKYO 2020"), className="text-center")
        ]),
        dbc.Row([
            dbc.Col(html.H6(children='Visualización y analisis de los diferentes datos recolectados durante la competencia.'), className="text-center")
        ]),

        dbc.Row([
            dbc.Col(dbc.Card(html.H3(children='Graficas',
                                     className="text-center text-light bg-dark"), body=True, color="dark")
                    , className="mb-4")
        ])
        ])
        ])
        ,

   

    html.Div([
              dbc.Card([
              dbc.CardBody([dbc.Col(dbc.Card(html.H3(children='Igualdad de genero en Tokyo 2020',
                                     className="text-center text-light bg-dark")), 
                                    className="card-title"),html.P("Se parte de la hipotesis y creencia mundialmente conocida en la que "
                                                                   "las mujeres a lo largo de la historia han tenido una menor representación "
                                                                   "en escenarios deportivos que su contraparte masculina. A partir de esta hipotesis, se busco "
                                                                   "analizar los datos respecto a la participación y la adquisición de medallas por parte de ambos generos"),                                                                           
                                                                  
                                                            html.P("En términos prácticos, fomentar el deporte con equidad de género implica la adopción de "
                                                           "algunas (pocas) medidas macrosociales combinadas con un buen número "  
                                                           "de acciones microsociales, frecuentemente independientes."),
                                                                       
                  ])
              ])
         ]),
     dcc.Graph(
        id='f-graph',
        figure=figBarIncome1
    ),


    html.Div([
              dbc.Card([
              dbc.CardBody(dbc.Row
                           ([

                            dbc.Col(dbc.Card(html.H3(children='Medallas obtenidas por país frente a cantidad de atletas y entrenadores',
                                     className="text-center text-light bg-dark"), body=True, color="dark")
                                    , className="mb-4"), html.P("Los resultados permiten hacer un analisis detallado de que tantas medallas "
                                                                   "puede llegar a obtener un país "
                                                                   "si el numero de atletas es mayor o menor "
                                                                   "al igual que si el numero de entrenadores es mayor o menor."),                                                                           
                                                                  

                            ] ) )
                           ] )
              ] )
               
                                        
         ,

    dcc.Graph(
        id='f2-graph',
        figure=figBarIncome2
    ),

    dcc.Graph(
        id='f3-graph',
        figure=figBarIncome3
    ),

    

     dcc.Graph(
        id='f4-graph',
        figure=figBarIncome4
    ),

     html.Div([
              dbc.Card([
              dbc.CardBody(dbc.Row
                           ([

                            dbc.Col(dbc.Card(html.H3(children='Probabilidad de exito por país respecto al numero de atletas',
                                     className="text-center text-light bg-dark"), body=True, color="dark")
                                    , className="mb-4"), html.P("Por medio de una función de probabilidad y el analisis de los datos "
                                                                "se estima la probabilidad que tiene cada país de que uno "
                                                                "de sus atletas gane una medalla."),                                                                           
                                                                  

                            ] ) )
                           ] )
              ] ),


      dcc.Graph(
     id='barCasesByCountry',
     figure=figBarCases
     ),
     dcc.Graph(
     id='mapCasesByCountry',
     figure=figMapCases
     ),

     html.Div([
              dbc.Card([
              dbc.CardBody(dbc.Row
                           ([

                            dbc.Col(dbc.Card(html.H3(children='Cantidad de eventos realizados por cada disciplina',
                                     className="text-center text-light bg-dark"), body=True, color="dark")
                                    , className="mb-4")                                                                          
                                                                  

                            ] ) )
                           ] )
              ] ),

     dcc.Graph(
     id='fig5',
     figure=figBarIncome5
     ),
    
    ])
        






if __name__ == '__main__':
    app.run_server(debug=True)