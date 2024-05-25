from flask import Flask, render_template, request, jsonify
import http_response
from sql import user_sql, user_info_sql

app = Flask(__name__)

# 用于存储个人信息的字典，包含多个用户的信息
personal_info = {
    'JohnDoe': {
        'name': 'John Doe',
        'email': 'john@example.com',
        'location': 'New York City'
    },
    'JaneDoe': {
        'name': 'Jane Doe',
        'email': 'jane@example.com',
        'location': 'San Francisco'
    }
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/resume_show.html')
def resume_show():
    return render_template('resume_show.html')


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    exist_flag, user_id = user_sql.exist(username, password)
    if exist_flag:
        return jsonify(http_response.HTTPResponse(200, "Welcome Back %s" % (username), user_id).to_dict())
    else:
        return jsonify(http_response.NotFoundResponse('failure').to_dict())


@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if user_sql.duplicate(username):
        return jsonify(http_response.SuccessResponse("This account already exists, please turn to 'login'").to_dict())
    else:
        user_sql.insert(username, password)
        return jsonify(http_response.NotFoundResponse('Register success').to_dict())


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
        user_info_sql.insert(user_id, name, gender, email_address, student_id, github, gitlab)
    return render_template('resume_show.html')


@app.route('/resume_edit.html')
def edit():
    return render_template('resume_edit.html')


@app.route('/get_personal_info', methods = ['GET'])
def get_personal_info():
    print(request.args)
    user_id = request.args.get('user_id')
    result = user_info_sql.search(user_id)
    if result is not None:
        return jsonify({"name":result[2], "gender":result[3], "email":result[4], "student_id":result[5], "github":result[6], "gitlab":result[7]})

    else:
        return jsonify({'error': 'Name not found'}), 404



if __name__ == '__main__':
    app.run(debug=True)
