from src.dao.dbConnection import MyMongoDB
from src.utility.get_logger import MyLogger

logger = MyLogger.logger


def register(**kwargs):
	db_user = MyMongoDB('Users')
	user_query_resp = db_user.find({"username": kwargs['username'], "password": kwargs['password']})
	user_query_resp = [i for i in user_query_resp]
	logger.info("Got data from db: {}".format(user_query_resp))
	if len(user_query_resp) > 0:
		ret = {
			"staus_code": 203,
			"message": "User already registered!"
		}
	else:
		user_query_resp = db_user.insert_one(kwargs)
		logger.info(user_query_resp)
		ret = {
			"staus_code": 200,
			"message": "Registered Successfully!"
		}
	return ret
