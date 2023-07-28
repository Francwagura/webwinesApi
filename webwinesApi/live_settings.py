import os
import dj_database_url

DEBUG = bool(os.environ.get("DEBUG", "0"))
DATABASES = dict(
    default=dj_database_url.config(
        default=os.environ.get("HEROKU_POSTGRESQL_CHARCOAL_URL")
    )
)
