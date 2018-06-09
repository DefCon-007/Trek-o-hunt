from src.utility.get_logger import MyLogger

logger = MyLogger.logger


class User:
	def __init__(self, **kwargs):
		self.username = kwargs['username']
		self.email = kwargs['email']
		self.phone = kwargs['phone']
		self.user_id = kwargs['user_id']
		self.rating = kwargs['rating']
		self.treks_created = kwargs['treks_created']
		self.treks_bought = kwargs['treks_bought']


