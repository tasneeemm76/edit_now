Image Editing Web App
Welcome to my Image Editing Web App, a simple and responsive web application that allows users to upload images and apply editing features like blurring and sharpening. It provides a user-friendly interface for selecting specific areas of an image and applying various effects, making it perfect for anyone looking to edit images quickly and easily.

Live Demo: You can try out the live version of the app here: https://edit-now.onrender.com

Features: Upload and Edit Images:

1. Upload an image to the platform.
2. Choose between various editing options (blur or sharpen).
3. Selective Blur:

Main Feature: Select a specific area on the uploaded image and apply a blur effect to that area. This allows users to focus on specific parts of the image while blurring the rest.
Ideal for privacy purposes or to enhance certain portions of an image while keeping other details discreet.

Sharpen Image: Sharpen the entire image with a simple click for a clearer, crisper look.

Download Processed Image: Once the image has been processed (blurred or sharpened), you can easily download the modified image directly from the application.

Technologies Used:
Backend: Python (Flask) – Lightweight backend to handle image processing and routing.
Frontend: HTML, CSS, JavaScript – Provides a clean, user-friendly interface.
Image Processing: Python libraries such as Pillow and OpenCV for image manipulation.
Hosting: Render – Deployed on Render for easy access to the app from anywhere.

Setup Instructions:
To run the project locally, follow these steps:

Clone the repository:
git clone https://github.com/yourusername/yourrepositoryname.git
cd yourrepositoryname

Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate  # For Windows use: venv\Scripts\activate

Install the required dependencies:
pip install -r requirements.txt

Run the application:
python app.py
Visit http://127.0.0.1:5000/ on your browser to start using the app.

Contributions:
If you'd like to contribute to this project, feel free to reach out at https://www.linkedin.com/in/tasneem-bawaji-a82412282/
I'm always open to suggestions and ideas for improvements! Feel free to open an issue or sharing feedback

Note:
The image processing features are designed to be simple but effective for basic image editing tasks. Future improvements may include adding more filters, adjusting brightness/contrast, and more!
