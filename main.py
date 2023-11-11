from flask import Flask
from coredb.init import startDb
from routes.user import user_bp
from routes.worker import worker_bp

app = Flask(__name__)
app.register_blueprint(user_bp)
app.register_blueprint(worker_bp)

if __name__ == '__main__':
    startDb()
    app.run(debug=False, port=5000)