from flask import Flask, render_template, jsonify, request
from werkzeug.utils import secure_filename
import time

from scraper import scrape_google
from augment import flip, left_translation, right_translation, up_translation

app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = 'my-secret-key'
app.config['SESSION_TYPE'] = 'filesystem'

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/scrape", methods=['GET', 'POST'])
def scrape():

    if request.method == "GET":
        return render_template("scrape.html")

    if request.method == "POST":

        bname = request.form['bname']

        scrape_google(bname)

        return jsonify({"status": "Complete!"})

@app.route("/augment", methods=['GET', 'POST'])
def augment():

    if request.method == "GET":
        return render_template("augment.html")

    if request.method == "POST":

        image = request.files['image']

        filename = secure_filename(image.filename)
        filename_original = filename
        filename = filename.split(".")[0] + str(int(time.time())) + "." + filename.split(".")[1]

        image.save("static/images/" + filename)

        flipped_img = flip("static/images/" + filename, filename)
        left_translation_img = left_translation("static/images/" + filename, filename)
        right_translation_img = right_translation("static/images/" + filename, filename)
        up_translation_img = up_translation("static/images/" + filename, filename)

        return jsonify({"status": "Augmentation complete!", "flipped_img": flipped_img, "left_translation_img": left_translation_img,
                        "right_translation_img": right_translation_img, "up_translation_img": up_translation_img})
