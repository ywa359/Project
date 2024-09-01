import logging

from flask import Blueprint, request, jsonify

from data_model.user_project import UserProject
from utils.db_session import db_session
from data_model.http_response import *

user_project_routes = Blueprint('user_project_routes', __name__)


# logging.basicConfig(filename='log/app.log',
#                     level=logging.DEBUG,
#                     format='%(asctime)s - %(levelname)s - %(message)s')


@user_project_routes.route('/get_projects_info', methods=['GET'])
def get_projects():
    user_id = request.args.get('user_id')

    # Query the projects for the given user_id
    try:
        results = db_session.query(UserProject).filter(
            UserProject.user_id == user_id).all()
    except Exception as e:
        print(e)
        return jsonify([])  # Return an empty list if no projects are found

    if not results or len(results) == 0:
        return jsonify([])  # Return an empty list if no results found

    # Format the results as a list of dictionaries
    result = [
        {
            "title": r.title,
            "description": r.description,
            "start_time": r.start_time.strftime('%Y-%m-%d %H:%M:%S'),
            "end_time": r.end_time.strftime('%Y-%m-%d %H:%M:%S'),
            "git_link": r.git_link,
            "online_service": r.online_service,
            "skills": r.skills
        }
        for r in results
    ]
    return jsonify(result)


@user_project_routes.route('/add_project', methods=['POST'])
def add_project():
    try:
        data = request.json
        user_project = UserProject.from_json(data)
        db_session.add(user_project)
        db_session.commit()
        return jsonify(SuccessResponse(
            "Add success.").to_dict())
    except Exception as e:
        print(e)
        return jsonify(SuccessResponse(
            "Error in Server").to_dict())
