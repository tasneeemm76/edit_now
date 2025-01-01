import base64
from flask import Flask, render_template, request, send_file
import numpy as np
import cv2
from werkzeug.utils import secure_filename
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']
    process_type = request.form.get('process_type', 'blur')  # Determine processing type
    intensity = int(request.form.get('intensity', 15))  # Default intensity

    if file.filename == '':
        return "No selected file", 400

    if file:
        filename = secure_filename(file.filename)
        np_img = np.frombuffer(file.read(), np.uint8)
        img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

        # Convert the original image to base64
        _, buffer_original = cv2.imencode('.jpg', img)
        original_base64 = base64.b64encode(buffer_original).decode('utf-8')

        if process_type == 'blur':
            # Apply GaussianBlur
            ksize = intensity if intensity % 2 == 1 else intensity + 1  # Kernel size must be odd
            processed_img = cv2.GaussianBlur(img, (ksize, ksize), 0)
        elif process_type == 'sharpen':
            # Apply Sharpening
            kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
            processed_img = cv2.filter2D(img, -1, kernel)
        else:
            return "Invalid process type", 400

        # Convert the processed image to base64
        _, buffer_processed = cv2.imencode('.jpg', processed_img)
        processed_base64 = base64.b64encode(buffer_processed).decode('utf-8')

        return render_template(
            'result.html',
            original_image=original_base64,
            processed_image=processed_base64,
            process_type=process_type,
            filename=filename
        )

@app.route('/download', methods=['POST'])
def download_file():
    image_data = request.form['image_data']  # Get the base64 image data from the form
    filename = request.form['filename']  # Get the filename

    # Decode the base64 string to binary data
    image_binary = base64.b64decode(image_data)

    # Create a BytesIO object to send the image as a file
    img_io = io.BytesIO(image_binary)
    img_io.seek(0)

    # Send the image as a downloadable file
    return send_file(img_io, mimetype='image/jpeg', as_attachment=True, download_name=filename)

if __name__ == '__main__':
    app.run(debug=True)

import os
app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
