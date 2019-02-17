from models import db
from flask import Flask, render_template

import config

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    app.SECRET_KEY = config.SECRET_KEY
    db.init_app(app)
    

    @app.before_first_request
    def init_db():
        db.create_all()

    @app.route("/")
    def home():
        user=models.create_user(email="robert@pythoncharmers.com",full_name="Robert Layton", password="swordfish")
        return render_template("index.html",user=user)

     #from users import user_blueprint
     #app.register_blueprint(user_blueprint, url_prefix="/users")

    return app


if __name__ == "__main__":
    import os
    app = create_app()
    app.run(port=int(os.getenv("PORT",8080)), host=os.getenv("IP", "127.0.0.1"), debug=True)        
