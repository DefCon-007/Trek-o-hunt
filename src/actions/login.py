from src.dao.dbConnection import MyMongoDB
from src.utility.get_logger import MyLogger

logger = MyLogger.logger


def login(**kwargs):
	db_user = MyMongoDB('Users')
	username = kwargs['username']
	password = kwargs["password"]
	user_query_resp = db_user.find({"username": username, "password": password})
	user_query_resp = [i for i in user_query_resp]
	logger.info("Got data from db: {}".format(user_query_resp))
	if len(user_query_resp) == 1:
		return {
			'status': 200,
			'message': "Successfully fetched data",
			'name': user_query_resp[0]['name'],
			'phone': user_query_resp[0]['phone'],
			'user_id': user_query_resp[0]['_id']
		}
	elif len(user_query_resp) == 0:
		return {
			'status': 201,
			'message': "Wrong username or password OR user not registered!",
		}
	else:
		return {
			'status': 205,
			'message': "Please contact admin",
		}
