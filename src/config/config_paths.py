from src.utility.common_functions import get_dir_path, read_property_file

parent_dir = get_dir_path()
configs = read_property_file(parent_dir + '/properties/config.properties')
input_data_dir = configs["input_data_dir"]
output_data_dir = '/home/atibhi/Desktop/Coworks/Trek-o-hunt/src/web'
port_no = int(configs["port_no"])
level = configs["level"]

log_op_path = parent_dir + '/logs'

log_config_path = parent_dir + '/src/config/logging.conf'

templates_path = parent_dir + '/webContent/templates'

images_path = output_data_dir + '/images'
