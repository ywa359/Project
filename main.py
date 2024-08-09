from flask import Flask, render_template, request, jsonify
import http_response
from sql import user_sql, user_info_sql, user_project_sql

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/resume.html')
def resume_new():
    return render_template('resume.html')


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    exist_flag, user_id = user_sql.exist(username, password)
    if exist_flag:
        return jsonify(
            http_response.HTTPResponse(200, "Welcome Back %s" % (username),
                                       user_id).to_dict())
    else:
        return jsonify(http_response.NotFoundResponse('failure').to_dict())


@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if user_sql.duplicate(username):
        return jsonify(http_response.SuccessResponse(
            "This account already exists, please turn to 'login'").to_dict())
    else:
        user_sql.insert(username, password)
        return jsonify(
            http_response.NotFoundResponse('Register success').to_dict())


@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    name = data.get('name')
    gender = data.get('gender')
    email_address = data.get('email_address')
    student_id = data.get('student_id')
    github = data.get('github')
    gitlab = data.get('gitlab')
    user_id = data.get('user_id')
    if user_info_sql.search(user_id) is None:
        user_info_sql.insert(user_id, name, gender, email_address, student_id,
                             github, gitlab)
    return render_template('resume.html')


@app.route('/get_personal_info', methods=['GET'])
def get_personal_info():
    print(request.args)
    user_id = request.args.get('user_id')
    result = user_info_sql.search(user_id)
    if result is not None:
        return jsonify(
            {"name": result[2], "gender": result[3], "email": result[4],
             "student_id": result[5], "github": result[6], "gitlab": result[7]})

    else:
        return jsonify({'error': 'Name not found'}), 404


@app.route('/get_projects_info', methods=['GET'])
def get_projects():
    user_id = request.args.get('user_id')
    result = user_project_sql.search(user_id)
    if result is None or len(result) == 0:
        return jsonify({})
    result = [{"title": r[2], "description": r[3], "start_time": r[4],
               "end_time": r[5], "git_link": r[6], "online_service": r[7],
               "skills": r[8]} for r in result]
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
