from flask import Blueprint, request, jsonify, render_template
from data_model.user_info import UserInfo
from utils.db_session import db_session

user_info_routes = Blueprint('user_info_routes', __name__)


@user_info_routes.route('/get_user_info', methods=['GET'])
def get_user_info():
    user_id = request.args.get('user_id')
    info = db_session.query(UserInfo).filter(
        UserInfo.user_id == user_id).first()

    if info:
        return jsonify(
            {
                "name": info.name,  # 使用属性名称访问字段
                "gender": info.gender,  # 使用属性名称访问字段
                "email": info.email_address,  # 使用属性名称访问字段
                "student_id": info.student_id,
                "github": info.github,
                "gitlab": info.gitlab
            }
        )
    else:
        return jsonify({'error': 'User not found'}), 404


@user_info_routes.route('/update_user_info', methods=['POST'])
def update_user_info():
    data = request.get_json()
    name = data.get('name')
    gender = data.get('gender')
    email_address = data.get('email')
    student_id = data.get('student_id')
    github = data.get('github')
    gitlab = data.get('gitlab')
    user_id = data.get('user_id')
    info = db_session.query(UserInfo).filter(UserInfo.user_id == user_id).first()
    if info:
        # Update the user information if found
        info.name = name
        info.gender = gender
        info.email_address = email_address
        info.student_id = student_id
        info.github = github
        info.gitlab = gitlab

        # Commit the changes to the database
        db_session.commit()
    else:
        new_user_info = UserInfo(
            user_id=user_id,
            name=name,
            gender=gender,
            email_address=email_address,
            student_id=student_id,
            github=github,
            gitlab=gitlab
        )

        # Add the new user to the session and commit the transaction
        db_session.add(new_user_info)
        db_session.commit()
    return render_template('resume.html')
