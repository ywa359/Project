import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

from data_model.user_skill import UserSkill


# Assuming the previous code for UserSkill and UserSkillModel is already defined

class TestUserSkill(unittest.TestCase):

    # def setUp(self):
    #     # Setup in-memory SQLite database
    #     self.engine = create_engine('sqlite:///:memory:')
    #     Base.metadata.create_all(self.engine)
    #     Session = sessionmaker(bind=self.engine)
    #     self.session = Session()
    #
    # def tearDown(self):
    #     # Cleanup database
    #     Base.metadata.drop_all(self.engine)
    #     self.session.close()

    def test_from_json(self):
        # Given JSON data
        json_data = {
            "user_id": 1,
            "skill_name": "Python",
            "rate": 5
        }

        # When converting JSON to SQLAlchemy object
        user_skill = UserSkill.from_json(json_data)

        # Then check that the fields are correctly populated
        self.assertEqual(user_skill.user_id, 1)
        self.assertEqual(user_skill.skill_name, "Python")
        self.assertEqual(user_skill.rate, 5)

        # # Check that it can be added to the database
        # self.session.add(user_skill)
        # self.session.commit()
        #
        # # Retrieve and check if it's correctly inserted
        # retrieved_skill = self.session.query(UserSkill).filter_by(user_id=1).first()
        # self.assertIsNotNone(retrieved_skill)
        # self.assertEqual(retrieved_skill.skill_name, "Python")
        # self.assertEqual(retrieved_skill.rate, 5)

if __name__ == '__main__':
    unittest.main()
