# 😊 Smile Detection using OpenCV

This project implements real-time smile detection using OpenCV's Haar Cascade Classifiers. It captures video from a webcam, detects faces and smiles, and highlights them with bounding boxes.

## 📁 Project Structure

```
Smile-Detection--
├── smile_detection.py       # Main script for real-time smile detection
├── haarcascade_frontalface_default.xml
├── haarcascade_smile.xml
├── README.md                # Project overview and instructions
└── requirements.txt         # Python dependencies
```

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- OpenCV

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/SakshiMalhotra18/Smile-Detection--.git
   cd Smile-Detection--
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the smile detection script:

   ```bash
   python smile_detection.py
   ```

## 🧠 How It Works

- Utilizes OpenCV's Haar Cascade Classifiers to detect faces and smiles.
- Processes video frames from the webcam in real-time.
- Draws rectangles around detected faces and smiles.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙌 Acknowledgments

- OpenCV library for providing the Haar Cascade Classifiers.
