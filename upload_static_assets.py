"""Use this to upload static content to S3."""

import flask_s3
from docs.factory import create_web_app

app = create_web_app()
with app.app_context():
    flask_s3.create_all(app)
