# Retic
from retic import App as app

"""Define all other apps"""
BACKEND_SENDFILES = {
    u"base_url": app.config.get('APP_BACKEND_SENDFILES'),
    u"photos": "/photos",
}

APP_BACKEND = {
    u"sendfiles": BACKEND_SENDFILES,
}

"""Add Backend apps"""
app.use(APP_BACKEND, "backend")
