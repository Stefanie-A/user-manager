from routes.user_routes import user_bp
from flask import Flask, jsonify
from database import db
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def home():
    return jsonify ({"message": "Hello world"})

app.register_blueprint(user_bp)
if __name__ == "__main__":
    app.run(debug=True, port=8000, host="0.0.0.0")

