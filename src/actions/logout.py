from src.utility.get_logger import MyLogger

logger = MyLogger.logger


def logout(**kwargs):
	return {
		'status': 200,
		'message': "Logged out successfully!",
	}
