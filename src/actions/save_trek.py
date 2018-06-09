from src.dao.dbConnection import MyMongoDB
from src.utility.get_logger import MyLogger

logger = MyLogger.logger


def save_trek(top_no=10):
	"""
	To save trek
	:return: bool
	"""
	db_trek = MyMongoDB("Treks")
	resp = db_trek.insert_one(dummy_trek)
	return resp


if __name__ == '__main__':
	dummy_trek = {
		"images": ["/home/ayush/Desktop/pyCharm/Trek-o-hunt/data/images/img1.jpg"],
		"created_by": "Garag",
		"polyline": "dsfjnk34268s",
		"rating": "9",
		"price": "500",
		"about": "A very good trek",
		"difficulty_level": "6",
		"static_map": "ajdb0932",
		"coordinates": "123 432",
		"elevation": "987.6",
		"transport_means": "walk",
		"hunt_images": ["/home/ayush/Desktop/pyCharm/Trek-o-hunt/data/images/img1.jpg"],
	}
	logger.info(save_trek())
