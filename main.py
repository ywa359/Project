from flask import Flask, render_template, request, jsonify
from routes.auth_routes import auth_routes
from routes.user_info_routes import user_info_routes
from routes.user_project_routes import user_project_routes
from routes.user_skill_routes import user_skill_routes
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# Register Blueprints
app.register_blueprint(auth_routes, url_prefix='/auth')
app.register_blueprint(user_info_routes, url_prefix='/user_info')
app.register_blueprint(user_project_routes, url_prefix='/user_project')
app.register_blueprint(user_skill_routes, url_prefix='/user_skill')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/resume.html')
def resume_new():
    return render_template('resume.html')


if __name__ == '__main__':
    app.run(debug=True)
