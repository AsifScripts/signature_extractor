Signature Extraction using Connected Component Analysis
A lightweight web application for extracting overlapped handwritten signatures from scanned documents using Connected Component Analysis (CCA) with OpenCV and scikit-image in Python.
This project provides a basic yet effective solution for signature segmentation from scanned documents and is designed with scalability for future enhancements like recognition, spoofing detection, and more.

live :- https://document-signature-extractor.onrender.com (wait for 1 minute and refresh brower)

📝 Project Overview
Input: Scanned document image (JPG, PNG, PDF)
Output: Extracted signatures saved & served from media/ folder.
The core functionality is built upon:
Connected Component Analysis (CCA) for segmentation.
Pixel-based filtering to differentiate between text, lines & signatures.
Django for handling uploads, processing & serving results.

🛠️ Features

✅ Web interface for document upload

✅ Signature extraction using OpenCV + scikit-image

✅ Automatic file storage under media/

✅ Render deployment ready

🔍 How It Works (Pipeline)

Grayscale conversion & binary thresholding.

Connected component labeling using scikit-image.

Filtering components based on pixel area thresholds.

Saving the masked signature image.

Large connected components (usually signatures) are kept, small noisy components are discarded.

🏗️ TODO (Planned Improvements)

 Advanced Outlier Removal to boost accuracy.
 
 CNN-based Signature Recognition.
 
 Spoof Detection module for forged signatures.
 
 Bounding Box Signature Detector & counter.
 
 Benchmark on SigSA Dataset.
 
 Frontend enhancements (signature overlays, download option).


🚀 Deployment (Render.com)

Make sure the following are configured:

Add gunicorn in requirements.txt:

gunicorn

Set Start Command in Render Dashboard:

gunicorn <your_project_name>.wsgi:application


Add env variables (optional):

DEBUG=False

ALLOWED_HOSTS=your_render_url

DATABASE_URL (if using DB later)


🖥️ Installation (Local Setup)

Clone repo & create virtual env:

git clone https://github.com/AsifScripts/signature_extractor.git

cd signature_extractor

python3 -m venv venv

source venv/bin/activate


Install dependencies:

pip install -r requirements.txt


Run server locally:
python manage.py runserver

📊 Sample Results

Input Document	

![Screenshot 2025-05-17 164703](https://github.com/user-attachments/assets/55c8927b-eaa6-4f9b-bd7e-2ea63477ca8b)


Extracted Signature

![Screenshot 2025-05-17 164629](https://github.com/user-attachments/assets/208f7dbb-68b1-44fe-a5b4-91509f2ab7d0)


🧠 Theory: Connected Component Analysis

Connected Component Analysis (CCA) is an algorithm that detects groups of connected pixels (components) having the same pixel intensity. For signature extraction:
Big components = likely signatures.
Small components = noise, text, or lines.
By tuning the component size thresholds, we can effectively isolate signatures from background noise.

📦 Dependencies

Python 3.8+
Django 4.x
OpenCV
scikit-image
gunicorn (for production)

Install with:
pip install django opencv-python scikit-image gunicorn

📄 License
This project is licensed under the MIT License.

👨‍💻 Author
Developed by asifScripts.
