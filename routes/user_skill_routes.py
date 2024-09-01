import logging

from flask import Blueprint, request, jsonify
from sqlalchemy import delete
from data_model.user_skill import UserSkill
from utils.db_session import db_session
from data_model.http_response import *

user_skill_routes = Blueprint('user_skill_routes', __name__)


# logging.basicConfig(filename='log/app.log',
#                     level=logging.DEBUG,
#                     format='%(asctime)s - %(levelname)s - %(message)s')


@user_skill_routes.route('/get_skills_info', methods=['GET'])
def get_skills():
    user_id = request.args.get('user_id')

    # Query the projects for the given user_id
    try:
        results = db_session.query(UserSkill).filter(
            UserSkill.user_id == user_id).all()
    except Exception as e:
        print(e)
        return jsonify([])  # Return an empty list if no projects are found

    if not results or len(results) == 0:
        return jsonify([])  # Return an empty list if no results found

    # Format the results as a list of dictionaries
    result = [
        {
            "skill_name": r.skill_name,
            "rate": r.rate,
        }
        for r in results
    ]
    return jsonify(result)


@user_skill_routes.route('/add_skill', methods=['POST'])
def add_skill():
    try:
        data = request.json
        user_skill = UserSkill.from_json(data)
        db_session.add(user_skill)
        db_session.commit()
        return jsonify(SuccessResponse(
            "Add success.").to_dict())
    except Exception as e:
        print(e)
        return jsonify(SuccessResponse(
            "Error in Server").to_dict())


@user_skill_routes.route('/add_skills', methods=['POST'])
def add_skills():
    try:
        data = request.json
        query = delete(UserSkill).where(UserSkill.user_id == data['user_id'])
        db_session.execute(query)
        db_session.commit()
        new_skills = []
        for skill in data['skills']:
            skill['user_id'] = int(data['user_id'])
            new_skill = UserSkill.from_json(skill)
            new_skills.append(new_skill)
        db_session.add_all(new_skills)
        db_session.commit()
        return jsonify(SuccessResponse(
            "Add success.").to_dict())
    except Exception as e:
        print(e)
        return jsonify(SuccessResponse(
            "Error in Server").to_dict())
