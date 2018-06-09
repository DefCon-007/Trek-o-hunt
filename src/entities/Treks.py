from src.utility.get_logger import MyLogger

logger = MyLogger.logger


class Treks:
	def __init__(self, **kwargs):
		self.images = kwargs['images']
		self.created_by = kwargs['created_by']
		self.polyline = kwargs['polyline']
		self.rating = kwargs['rating']
		self.price = kwargs['price']
		self.about = kwargs['about']
		self.difficulty_level = kwargs['difficulty_level']
		self.static_map = kwargs['static_map']
		self.coordinates = kwargs['coordinates']
		self.elevation = kwargs['elevation']
		self.transport_means = kwargs['transport_means']
		self.hunt_images = kwargs['hunt_images']

	def save_data_to_db(self):
		pass

