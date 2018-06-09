import json
import src.config.config_paths as config_paths
from src.utility.common_functions import does_dir_exist, create_dir
from flask import Flask, render_template, request, Response, session
from src.actions.login import login as action_login
from src.actions.get_top_treks import get_top_treks as action_get_top_treks
from src.actions.get_local_treks import get_local_treks as action_get_local_treks
from src.actions.logout import logout as action_logout
from werkzeug.utils import secure_filename
from src.actions.register import register as action_register
from src.utility.get_logger import MyLogger

logger = MyLogger.logger

app = Flask(__name__)
app.secret_key = '102394873782491'


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
		logger.info("Sending back: {}".format(ret))
		session['username'] = req_data['username']
		return Response(json.dumps(ret), status=200, mimetype="application/json")
	except Exception as e:
		logger.exception(e)
		return Response("Failure",  status=100)


@app.route("/trekohunt/register", methods=["POST"])
def register():
	f = request.files['files']
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
		logger.info("Sending back: {}".format(ret))
		return Response(json.dumps(ret), status=200, mimetype="application/json")
	except Exception as e:
		logger.exception(e)
		return Response("Failure",  status=100)


@app.route("/trekohunt/logout", methods=["POST", "GET"])
def logout():
	try:
		ret = action_logout()
		session.pop('username', None)
		return Response(json.dumps(ret), status=200, mimetype="application/json")
	except Exception as e:
		logger.exception(e)
		return Response("Unable to logout!",  status=201)


@app.route("/trekohunt/save_images", methods=["POST"])
def save_images():
	if 'file' not in request.files:
		logger.info('No file part')
		return Response("No file part",  status=100)
	file = request.files['file']
	if file.filename == '':
		logger.info('No file selected!')
		return Response("No file selected!", status=100)
	if file:
		filename = secure_filename(file.filename)
		file.save(config_paths.images_path + "/" + filename)
		return Response("Successfully saved images", status=200)


@app.route("/trekohunt/get_images", methods=["GET"])
def get_images():
	if 'file' not in request.files:
		logger.info('No file part')
		return Response("No file part",  status=100)
	file = request.files['file']
	if file.filename == '':
		logger.info('No file selected!')
		return Response("No file selected!", status=100)
	if file:
		filename = secure_filename(file.filename)
		file.save(config_paths.images_path + "/" + filename)
		logger.info("Successfully saved images")
		return Response("Successfully saved images", status=200)


@app.route("/trekohunt/get_top_treks", methods=['GET'])
def get_top_treks():
	top_treks = action_get_top_treks()
	top_treks = {'status': 200, "top_treks":top_treks}
	if len(top_treks) > 0:
		logger.info("Sending back: {}".format(top_treks))
		return Response(json.dumps(top_treks), status=200, mimetype="application/json")
	else:
		logger.info("Length of top_treks is zero!")
		return Response("Unable to top fetch treks!", status=201)


@app.route("/trekohunt/get_local_treks", methods=['GET'])
def get_local_treks():
	local_treks = action_get_local_treks()
	local_treks = {'status': 200, "local_treks": local_treks}
	if len(local_treks) > 0:
		logger.info("Sending back: {}".format(local_treks))
		return Response(json.dumps(local_treks), status=200, mimetype="application/json")
	else:
		logger.info("Length of local_treks is zero!")
		return Response("Unable to local fetch treks!", status=201)


@app.route("/trekohunt/save_trek", methods=['GET'])
def save_trek():
	local_treks = action_get_local_treks()
	if len(local_treks) > 0:
		logger.info("Sending back: {}".format(local_treks))
		return Response(json.dumps({'status': 200, "local_treks": local_treks}), status=200, mimetype="application/json")
	else:
		logger.info("Length of local_treks is zero!")
		return Response("Unable to local fetch treks!", status=201)


def start_app(host):
	app.logger.disabled = True
	app.run(port=config_paths.port_no, host=host)


if __name__ == "__main__":
	host = "0.0.0.0"
	if not does_dir_exist(config_paths.log_op_path):
		create_dir(config_paths.log_op_path)
	start_app(host=host)
