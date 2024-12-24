import eventlet
from eventlet import wsgi

from website import *
from dotenv import load_dotenv
load_dotenv()

import threading, os

app = create_app()

if __name__ == '__main__':
    app.run("0.0.0.0", 8080, True) # Debug
    # wsgi.server(eventlet.listen(("0.0.0.0", os.getenv("PORT", default=8080))), app) # Stable run


