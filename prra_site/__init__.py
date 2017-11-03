from flask import Flask, render_template
from flask_control import FlaskController

# 404 handling
app = Flask(__name__)
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# registering the blueprints
from prra_site.views import general

app.register_blueprint(general.mod)

# providing a stop mechanism
def start():
    fc = FlaskController(app, True)
    fc.start()
    request_data = fc.next()
    fc.stop()
    fc.await()

if __name__ == '__main__':
    start()
