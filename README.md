# FastAPI and Google Login (OAuth)
This is an example following the tutorial on https://blog.hanchon.live/guides/google-login-with-fastapi/

## Requirements:
- Python3.6+

## How to run the example:
- Create a virtualenv `python3 -m venv .venv`
- Activate the virtualenv `. .venv/bin/activate`
- Install the requirements `pip install -r requirements.txt`
- Set up the env vars:
    - Create the following credentials from https://console.cloud.google.com
    - export GOOGLE_CLIENT_ID=...
    - export GOOGLE_CLIENT_SECRET=...
    - export SECRET_KEY=...
- Run the app: `python run.py`

##Run this in postman:

Followings fields are required to generate access token through the postman:-

1) Navigate to the authorization botton
2) select oauth 2.0
3) Create new token
4) Fill the field accordingly:-
    callback URL/Redirect url=
    auth url=https://accounts.google.com/o/oauth2/auth
    access token url=https://accounts.google.com/o/oauth2/token
    client ID=
    client secret=
    Scope=https://www.googleapis.com/auth/siteverification.verify_only
    scope can be changed according to the requirement for more info https://developers.google.com/identity/protocols/oauth2/scopes
    scope means what type of the information is accessing from third party website
5) Once access token is generated
6) Select the Bearer token and paste the access token and get the required information


