from src.dao.dbConnection import MyMongoDB
from src.utility.get_logger import MyLogger

logger = MyLogger.logger


def get_top_treks(top_no=10):
	"""
	To get the local treks within (radius) circle of the trek coordinate
	:return:
	Array of all top top_no treks
	"""
	db_treks = MyMongoDB("Treks")
	top_treks = [trek for trek in db_treks.find({})]
	return top_treks


if __name__ == '__main__':
	logger.info([i for i in get_top_treks()])
