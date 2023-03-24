import os
import urllib.parse


CLIENT_SECRET = 'CLIENT_SECRET'
CLIENT_ID = 'CLIENT_ID'
REDIRECT_URI = urllib.parse.quote_plus("http://localhost:8000/auth/get-token")
STATE = "STATE"