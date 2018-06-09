import json
import src.config.config_paths as config_paths
from src.utility.common_functions import does_dir_exist, create_dir
from flask import Flask, render_template, request, Response
from src.actions.login import login as action_login
from src.actions.register import register as action_register
from src.utility.get_logger import MyLogger

logger = MyLogger.logger

app = Flask(__name__)


@app.route("/")
def main():
	return render_template('index.html')


@app.route("/trekohunt/login", methods=["POST"])
def login():
	if request.data.decode("utf-8") is not "":
		req_data = json.loads(request.data.decode("utf-8"))
	elif request.form.to_dict() != {}:
		req_data = request.form.to_dict()
	else:
		logger.info("No data received")
		return Response("Failure", status=100)

	try:
		ret = action_login(**req_data)
		return Response(json.dumps(ret), status=200, mimetype="application/json")
	except Exception as e:
		logger.exception(e)
		return Response("Failure",  status=100)


@app.route("/trekohunt/register", methods=["POST"])
def register():
	if request.data.decode("utf-8") is not "":
		req_data = json.loads(request.data.decode("utf-8"))
	elif request.form.to_dict() != {}:
		req_data = request.form.to_dict()
	else:
		logger.info("No data received")
		return Response("Failure", status=100)
	logger.info("Got request:")
	logger.info(req_data)
	try:
		ret = action_register(**req_data)
		return Response(json.dumps(ret), status=200, mimetype="application/json")
	except Exception as e:
		logger.exception(e)
		return Response("Failure",  status=100)


def start_app(host):
	app.logger.disabled = True
	app.run(port=config_paths.port_no, host=host)


if __name__ == "__main__":
	if not does_dir_exist(config_paths.log_op_path):
		create_dir(config_paths.log_op_path)
	start_app()
