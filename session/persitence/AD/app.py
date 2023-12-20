from flask import Flask, render_template, redirect, url_for, session
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.secret_key = 'your_secret_key'

oauth = OAuth(app)

# Azure AD configuration
oauth.register(
    name='azure',
    client_id='f5ab0427-d46e-4970-9f48-3677b4e8df11',
    client_secret='xRW8Q~uGlUtvR2nqC8JAdafy00na~4ak.s3C_cqh',  # Add your client secret here
    authorize_url='https://login.microsoftonline.com/e17c97bf-dd74-41a7-a534-79e65f044dc9/oauth2/v2.0/authorize',
    authorize_params=None,
    access_token_url='https://login.microsoftonline.com/e17c97bf-dd74-41a7-a534-79e65f044dc9/oauth2/v2.0/token',
    access_token_params=None,
    refresh_token_url=None,
    redirect_uri='https://lucky-bugs-watch.loca.lt/login/authorized',
    client_kwargs={'scope': 'openid email profile'},
)

@app.route('/')
def home():
    return 'Welcome to the Flask Authlib Azure AD Login App!'

@app.route('/login')
def login():
    return oauth.azure.authorize_redirect(redirect_uri=url_for('authorized', _external=True))

@app.route('/logout')
def logout():
    session.pop('token', None)
    return 'Logged out!'

@app.route('/login/authorized')
def authorized():
    token = oauth.azure.authorize_access_token()
    session['token'] = token

    # Fetch user details from the Azure AD userinfo endpoint
    user = oauth.azure.parse_id_token(token)
    email = user['email']
    given_name = user.get('given_name', '')
    family_name = user.get('family_name', '')

    # Perform additional logic based on user information if needed

    return render_template('dashboard.html', email=email, given_name=given_name, family_name=family_name)

if __name__ == '__main__':
    app.run(debug=True)
