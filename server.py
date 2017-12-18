from flask import Flask, request, send_file
import recognizer as r
from PIL import Image

app = Flask(__name__)

#INDEX PAGE
@app.route('/')
def index():
	return "Eyes for the blind..."


#LOGIN ENDPOINT
@app.route('/upload', methods=['POST'])
def upload():
	imagefile = Image.open(request.files['file'])
	imagefile.save("pic.jpg")
	r.recognize()
	filename = 'result.jpg'
	return send_file(filename, mimetype='image/jpg')


#MAIN
if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)