from src.dao.dbConnection import MyMongoDB
from src.utility.get_logger import MyLogger

logger = MyLogger.logger


def get_local_treks(trek_coordinate=100, radius=100):
	"""
	To get the local treks within (radius) circle of the trek coordinate
	:return:
	Array of all treks within the circle
	"""
	db_treks = MyMongoDB("Treks")
	local_treks = []
	for trek in db_treks.find({}):
		del trek['_id']
		local_treks.append(trek)
	return local_treks


if __name__ == '__main__':
	logger.info([i for i in get_local_treks()])
