from src.dao.dbConnection import MyMongoDB


def get_local_treks(trek_coordinate=100, radius=100):
	"""
	To get the local treks within (radius) circle of the trek coordinate
	:return:
	Array of all treks within the circle
	"""
	db_treks = MyMongoDB("Treks")
	local_treks = [trek for trek in db_treks.find({})]
	return local_treks
