# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 16:20:27 2018

@author: hmamin
"""

import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, Event
import plotly.graph_objs as go
from collections import deque
from app import app

# Create deques for live graphs
max_len = 25
perf_x = deque([0], maxlen=max_len)
perf_y = deque([np.random.randint(0,10)], maxlen=max_len)

graph_names = ['Site Performance', 'Downtime', '% Operational']
dropdown_options = [{'label': name, 'value': name} for name in graph_names]

# Create app layout
layout = html.Div([
    html.H3('Live Metrics'),
    dcc.Dropdown(id='graph_dropdown', options=dropdown_options, multi=True,\
                 value=['Site Performance']),
    html.Div(id='performance', className='top_margin'),
    dcc.Interval(id='update_interval', interval=1000)
])


@app.callback(Output('performance', 'children'),
              [Input('graph_dropdown', 'value')],
              events = [Event('update_interval', 'interval')])
def update_perf_graph(dropdown_vals):
    
    # Add new data point
    perf_x.append(perf_x[-1] + 1)
    perf_y.append(perf_y[-1] + np.random.randint(-10,11))
    graphs = []
    #for selection in dropdown_vals:
       
    # Create line plot
    trace0 = go.Scatter(
            x=list(perf_x),
            y=list(perf_y),
            mode='lines',
            fill='tozeroy',
            line={'width': 3, 'color': 'rgb(109, 148, 157)'}
            )
    layout0 = go.Layout(
            title='Site Performance',
            xaxis={'title': 'Sample #', 'range': [min(perf_x), max(perf_x)]},
            yaxis={'title': 'Rating', 'range': [min(perf_y)-1, max(perf_y)+1]},
            width='75vw',
            height=500,
            #paper_bgcolor='#2D3E5A'                                    
            )
    g = dcc.Graph(
            id='live_line_chart',
            figure=go.Figure(
                    data = [trace0],
                    layout = layout0
                    ),
            animate=True
            )
    graphs.append(g)
    return g, str(dropdown_vals)

