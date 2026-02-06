
## Face Detection using OpenCV (Python)

### 📌 Project Overview

This project is one of my earlier works, developed to understand the basics of **computer vision and face detection** using Python. The application uses the **OpenCV library** to detect human faces in images and real-time video streams.

Although it is a simple project, it helped me gain practical knowledge of how face detection works internally and how classifiers are used in real-world applications.

---

### 🛠️ Technologies Used

* **Python**
* **OpenCV (cv2)**
* **Haar Cascade Classifier**

---

### 📂 Project Structure

```
FaceDetection/
│
├── app.py      # Face detection using a reference image
├── face.py     # Real-time face detection with bounding boxes
├── haarcascade_frontalface_default.xml
└── README.md
```

---

### ⚙️ How It Works

* The project uses a **Haar Cascade classifier** to identify facial features.
* `app.py` detects faces from a given image.
* `face.py` detects faces in real time using a webcam and draws **colored rectangles** around detected faces.
* The classifier is imported and applied to grayscale images for accurate detection.

---

### ▶️ How to Run the Project

1. Clone the repository:

```bash
git clone [https://github.com/your-username/FaceDetection.git]
```

2. Install required dependencies:

```bash
pip install opencv-python
```

3. Run the image-based face detection:

```bash
python app.py
```

4. Run real-time face detection:

```bash
python face.py
```

---

### 🎯 Learning Outcome

* Understood the basics of **OpenCV**
* Learned how **Haar Cascade classifiers** work
* Gained hands-on experience with **image processing and face detection**
* Built confidence in working with Python-based computer vision projects

---

### 🚀 Future Improvements

* Improve detection accuracy
* Add support for multiple faces
* Implement deep learning-based face detection (CNN)
* Add face recognition features

---

### 👤 Author

**Haritha Netha**
This project was created as part of my learning journey in Python and computer vision.

