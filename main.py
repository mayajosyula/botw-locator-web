from flask import Flask, flash, render_template, request, redirect
from PIL import Image
import base64
import io
from predict import *

app = Flask(__name__) 

@app.route("/",  methods=["GET", "POST"])
def home():
    return render_template("webtest.html")

@app.route("/upload", methods=["GET", "POST"])
def classify():
    if 'file' in request.files:
        file = request.files['file']
        if file.filename == '':
            flash('No file selected')
            return redirect(request.url)
        result = get_prediction(file)
        img = Image.open(file)
        data = io.BytesIO()
        img.save(data, "JPEG")
        encoded_img = base64.b64encode(data.getvalue())
        decoded_img = encoded_img.decode('utf-8')
        img_data = f"data:image/jpeg;base64,{decoded_img}"
        return render_template("upload.html", result=result, image=img_data)
    return "File not processed"



if __name__ == "__main__":
    app.run(debug=True)