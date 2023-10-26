from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from routes.user_routes import user_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route("/home")
def home():
    return "Welcome"

app.register_blueprint(user_bp)
if __name__ == "__main__":
    app.run(debug=True)
