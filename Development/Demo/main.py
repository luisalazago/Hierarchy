import os
from dummyTest import readImage
from flask import Flask, render_template, url_for, request, flash, redirect, send_from_directory
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "images"
msg = None

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.add_url_rule("/uploads/<name>", endpoint="download_file", build_only=True)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if "file" not in request.files:
            flash("No file part :c")
            return redirect(request.url)
        
        file = request.files["file"]
        
        if file.filename == "":
            flash("No file detected")
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            return redirect(url_for("download_file", name=filename))
    return render_template("index.html", msg="", text="")

@app.route("/uploads/<name>")
def download_file(name):
    global msg
    msg = "The file was uploaded successfully!"
    send_from_directory(app.config["UPLOAD_FOLDER"], name)
    return redirect(url_for("show_text", name=name))

@app.route("/<name>", methods=["GET", "POST"])
def show_text(name):
    global msg
    display_msg = ""
    text = ""
    if request.method == "GET":
        if msg != None:
            display_msg = msg
            msg = None
        text = readImage(name, 1)
    return render_template("index.html", msg=display_msg, text=text)

if __name__ == "__main__":
    app.run(debug=True)