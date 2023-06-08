# import unittest

# from lib import config, lib

# from lib.models import Users, Tasks,Products
# from datetime import datetime
# from lib.database import Base, engine

# class UserTestCase(unittest.TestCase):
# 	def setUp(self):
# 		lib.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
# 		Base.create_all()
# 		lib.init_app()
# with lib.app.app_context():
#             Base.metadata.create_all(bind=engine)

# @classmethod
# def tearDown(self):
# 		Base.session.remove()
# 		Base.drop_all()
		
# def setUp(self):
#         self.app = lib.app.test_client()

# def test_password(self):
# 		u = Users(username='Mary')
# 		u.set_password('gimmegimme')
# 		self.assertFalse(u.check_password('notgimme'))
# 		self.assertTrue(u.check_password('gimmegimme'))

# def test_check_name(self):
# 		u = Products(project_name='Mary')
# 		self.assertFalse(u.if_name_is_empty())
# 		self.assertTrue(u.if_name_is_valid())

# def test_task_date(self):
# 		t = Tasks(task_name='Idont know unittest',date=datetime.utcnow())
# 		self.assertFalse(t.date_time_now())

# if __name__ == '__main__':
# 	unittest.main(verbosity=2)
	