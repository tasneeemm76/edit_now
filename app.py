from flask import Flask, render_template, request, send_file
import cv2
import numpy as np
from werkzeug.utils import secure_filename
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    if file:
        # Process the image
        filename = secure_filename(file.filename)
        np_img = np.frombuffer(file.read(), np.uint8)
        img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

        # Apply GaussianBlur
        blurred_img = cv2.GaussianBlur(img, (15, 15), 0)

        # Save to a BytesIO object for download
        is_success, buffer = cv2.imencode(".jpg", blurred_img)
        io_buf = BytesIO(buffer)

        return send_file(io_buf, mimetype='image/jpeg', as_attachment=True, download_name=f"blurred_{filename}")

if __name__ == '__main__':
    app.run(debug=True)

import os
app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
