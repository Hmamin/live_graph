import dash
import dash_auth

def extract_creds(file='hist_auth.txt'):
    with open(file, 'r') as f:
        return [f.read().split(',')]
    
creds = extract_creds()
app = dash.Dash('auth')
auth = dash_auth.BasicAuth(app, creds)

server = app.server
app.config.suppress_callback_exceptions = True