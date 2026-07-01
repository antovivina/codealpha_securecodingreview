from flask import Flask, render_template, request
from analyzer import analyze_file
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route("/", methods=["GET", "POST"])
def home():

    findings = []
    filename = None

    if request.method == "POST":

        file = request.files["file"]

        if file:

            filename = file.filename

            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)

            findings = analyze_file(filepath)

    return render_template(
        "index.html",
        findings=findings,
        filename=filename
    )


if __name__ == "__main__":
    app.run(debug=True)