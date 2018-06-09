import sys
import os
parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)).replace('\\', '/'))
sys.path.append(parent_dir)
from src.web.app import start_app
from src.utility.common_functions import does_dir_exist, create_dir
import src.config.config_paths as config_paths


if __name__ == "__main__":
	if not does_dir_exist(config_paths.log_op_path):
		create_dir(config_paths.log_op_path)
	start_app(host="0.0.0.0")
