#Task 1: Import Libraries, Modules and Files
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import dash
from dash import html
from dash import dcc
from dash import dash_table
from dash.dependencies import Input, Output
import preprocess


#Task 4: Load the dataset
df = pd.read_csv('playstore-analysis.csv')


#Task 5b: Store the preprocessed dataset
df = preprocess.run(df)

#Task 8a: Create a non-interactive plot
temp = df.groupby('Category').agg( {"Installs":"sum"}).reset_index()
temp.sort_values(by=['Installs'], inplace=True, ascending=False)
temp = temp.head(15)
pieplotfig = go.Figure()
pieplotfig.add_trace(go.Pie(
                    labels=temp.Category, 
                    values=temp.Installs, 
                    textinfo='label+percent', 
                    insidetextorientation='radial', 
                    pull = 0.05
  ))
pieplotfig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 40},bargap=0.05, autosize=True)


#Task 2a: Create Dash class instance
app = dash.Dash()

#Task 3: Initialize Layout of application
#All HTML components stay inside the layout
# Task 8b, 9a, 10a, 11a 
app.layout = html.Div([
    html.Div([
        html.H3('Data-Centric Dashboard', style={'textAlign': 'center'})], 
        style={'width': '100%', 'display': 'inline-block'}),

    html.Div([dcc.Graph(figure=pieplotfig)],
        style={'width': '99%', 'display': 'inline-block', 'border-style': 'solid', 'border-width': '0.1%', 'margin-left': '0%', 'margin-right': '0'}),
    html.Hr(),

    html.Div([
        html.H3('Versions', style={'textAlign': 'center'}),
        html.Div([dcc.Graph(id='version-graphic')],
            style={'width': '99%', 'display': 'inline-block', 'border-style': 'solid', 'border-width': '0.1%', 'margin-left': '0%', 'margin-right': '0'}),

        html.Div([dcc.Slider(1, 8, 1, value=1, id='version-slider'),], 
            style={'width': '100%', 'display': 'inline-block', 'text-align':'centre'})], 
        style={'width': '100%', 'display': 'inline-block'}),
    html.Hr(),

    html.Div([
        html.H3('Category Analyzer', style={'textAlign': 'center'}),
        html.Div([dcc.Dropdown(df['Category'].unique(), 'ART_AND_DESIGN', id='xaxis-column'),], 
            style={'width': '100%', 'display': 'inline-block', 'text-align':'centre'})],
        style={'width': '100%', 'display': 'inline-block'}),

    html.Div([dcc.Graph(id='indicator-graphic')],
        style={'width': '47%', 'display': 'inline-block', 'border-style': 'solid', 'border-width': '0.5%', 'margin-left': '0%', 'margin-right': '0'}),

    html.Div([dcc.Graph(id='installs-graphic')],
        style={'width': '47%', 'display': 'inline-block', 'border-style': 'solid', 'border-width': '0.1%', 'margin-left': '5%', 'margin-right': '0'}),
    html.Hr(),

    html.Div([
        html.H3('Correlation', style={'textAlign': 'center'}),
        html.Div([
            dcc.Dropdown(
                ['Category','Rating','Reviews','Size','Installs','Price','Content_Rating','Android_Ver'],
                'Category',
                 id='xaxis-var'),], 
        style={'width': '49.5%', 'display': 'inline-block', 'align-items': 'left', 'margin-left': '0%', 'margin-right': '0'}),

    html.Div([
        dcc.Dropdown(
            ['Category','Rating','Reviews','Size','Installs','Price','Content_Rating','Android_Ver'],
            'Category',
            id='yaxis-var'),],
    style={'width': '49.5%', 'display': 'inline-block', 'margin-left': '1%', 'margin-right': '0'}),

    html.Div([dcc.Graph(id='scatterplot_variable')],
        style={'width': '99%', 'display': 'inline-block', 'border style': 'solid', 'border-width': '0.1%', 'margin-left': '0%', 'margin-right': '0'}), ], style={'width': '100%', 'display': 'inline-block'}),

#End of application's layout
])

#Task 9b, 10b, 11b: All callbacks go here
@app.callback(    
Output(component_id='scatterplot_variable', 
    component_property='figure'),
Input(component_id='xaxis-var', 
    component_property='value'),
Input(component_id='yaxis-var', 
    component_property='value')
)
def update_graph(xaxis,yaxis):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df[xaxis], 
        y=df[yaxis], 
        mode='markers'
    ))
    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 40},bargap=0.05, autosize=True)
    fig.update_xaxes(title=xaxis)
    fig.update_yaxes(title=yaxis)
    return fig


#Task 2b: Run Server here. This should be at the last line of the file.
app.run(debug=True, host='0.0.0.0', port=8501)