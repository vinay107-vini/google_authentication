import os
from authlib.integrations.starlette_client import OAuth
from authlib.integrations.starlette_client import OAuthError
from fastapi import FastAPI
from fastapi import Request
from starlette.config import Config
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import HTMLResponse
from starlette.responses import RedirectResponse

app = FastAPI()
config = Config(".env")

config_data = {'GOOGLE_CLIENT_ID':config("GOOGLE_CLIENT_ID"),
                'GOOGLE_CLIENT_SECRET':config("GOOGLE_CLIENT_SECRET")
                }

starlette_config = Config(environ=config_data)

oauth = OAuth(starlette_config)

oauth.register(
    name='google',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={'scope':'https://www.googleapis.com/auth/userinfo.email'},
)

# Set up the middleware to read the request session
SECRET_KEY = config("GOOGLE_CLIENT_SECRET")
if SECRET_KEY is None:
    raise 'Missing SECRET_KEY'
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)


@app.get('/')
def public(request: Request):
    user = request.session.get('user')
    if user:
        print(user.get("email_verified"))
        return HTMLResponse("<p>Welcome to page</p><a href=/logout>Logout</a>")
    return HTMLResponse('<a href=/login>Login through google account</a>')


@app.route('/logout')
async def logout(request: Request):
    request.session.pop('user', None)
    return RedirectResponse(url='/')


@app.route('/login')
async def login(request: Request):
    redirect_uri = request.url_for('auth')  # This creates the url for our /auth endpoint
    print(redirect_uri)
    return await oauth.google.authorize_redirect(request, redirect_uri)
    

@app.route('/auth')
async def auth(request: Request):
    try:
        access_token = await oauth.google.authorize_access_token(request)
    except OAuthError:
        return RedirectResponse(url='/')
    user_data = await oauth.google.parse_id_token(request, access_token)
    request.session['user'] =user_data
    return RedirectResponse(url='/')

if __name__ == '__main__':
    uvicorn.google(app, port=7000)





