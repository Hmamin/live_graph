from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from app import app
from apps import app1, app2

# white, light grey, turquoise, dark grey, navy
colors = ['#F1F4F6', '#9C9282', '#6D949D', '#756D68', '#2D3E5A']
external_css = 'https://codepen.io/hmamin_gcn/pen/Gxypzr.css'
app.css.append_css({'external_url': external_css})
app.layout = html.Div([
        dcc.Location(id='url', refresh=False),
        html.Div([
            dcc.Link('Live Metrics', href='/1', className='menu'),\
            dcc.Link('Hardware Issues', href='/2', className='menu')
            ], id='menu'),
        html.Div(id='main-content')
        ])


@app.callback(Output('main-content', 'children'),
              [Input('url', 'pathname')])
def change_page(url_path):
    if url_path == '/1':
        return app1.layout
    elif url_path == '/2':
        return app2.layout
    else:
        return '404'


if __name__ == '__main__':
    app.run_server(debug=True)