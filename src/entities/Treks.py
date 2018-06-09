from src.utility.get_logger import MyLogger

logger = MyLogger.logger


class Treks:
	def __init__(self, **kwargs):
		self.images = kwargs['images']
		self.created_by = kwargs['created_by']
		self.polyline = kwargs['polyline']
		self.rating = kwargs['rating']
		self.price = kwargs['price']
		self.hunt_images = kwargs['hunt_images']

