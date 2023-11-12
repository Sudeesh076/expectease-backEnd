from flask import Flask
from coredb.init import startDb
from coredb.sample import sampleData
from routes.service import service_bp
from routes.user import user_bp
from routes.worker import worker_bp

app = Flask(__name__)
app.register_blueprint(user_bp)
app.register_blueprint(worker_bp)
app.register_blueprint(service_bp)

if __name__ == '__main__':
    startDb()
    sampleData()
    app.run(debug=False, port=5000)
