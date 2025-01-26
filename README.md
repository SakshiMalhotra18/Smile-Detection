😀 Smile Detection Using OpenCV

Welcome to the Smile Detection project! 🎉 This project applies computer vision techniques using OpenCV to detect faces and smiles in real-time via webcam.

📌 Project Overview

🎯 Goal: Detect faces and smiles in real-time using OpenCV.

📂 Dataset: Pre-trained Haar Cascade models from OpenCV.

🛠 Tech Stack: Python, OpenCV, NumPy

📊 Dataset Information

haarcascade_frontalface_default.xml → Pre-trained Haar Cascade for face detection.

haarcascade_smile.xml → Pre-trained Haar Cascade for smile detection.

🚀 How to Run This Project

1️⃣ Clone this repository:

git clone https://github.com/SakshiMalhotra18/smile-detection.git

2️⃣ Navigate to the project directory:

cd smile-detection

3️⃣ Install dependencies:

pip install opencv-python

4️⃣ Run the script:

python face.py

🖼️ How It Works

The script captures video from the webcam.

It converts the frames to grayscale for better detection.

Faces are detected and highlighted using bounding boxes.

Inside detected faces, smiles are detected and highlighted.

If a smile is detected, a "Smiling" label appears!

📸 Demo

Run the script and smile at the camera to see the detection in action!

📝 License

This project uses OpenCV’s Haar Cascade models, which are freely available under the OpenCV license.

⭐ Contribute

Feel free to fork the repository and contribute improvements! 🚀
