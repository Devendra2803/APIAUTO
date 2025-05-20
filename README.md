🧠 Auto Labeler (FastAPI + YOLOv8)

This project is a lightweight image annotation system that automatically labels objects in images using polygon-based detection and exposes FastAPI endpoints to trigger labeling and view outputs.

____________________________________________________________________________________________

🚀 Features

🖼️ Automatically detects and labels objects in images inside `data/images/`.

🧠 Uses YOLOv8 (or compatible model) for polygon-based object detection.

📤 Saves labeled data into a CSV file at `output/labels_output.csv`.

⚡ FastAPI integration with clean, interactive API docs at `/docs`.

____________________________________________________________________________________________

📁 Project Structure

```
.
├── train.py                 # FastAPI app and labeling logic
├── data/
│   └── images/              # Folder containing input images
├── output/
│   └── labels_output.csv    # Generated labels saved here
├── requirements.txt         # Required Python packages
└── README.md
```

____________________________________________________________________________________________

⚙️ Setup Instructions

1. ✅ Clone the repository

```bash
git clone https://github.com/Amol027/auto-labeler.git
cd auto-labeler
```

2. 📦 Install dependencies

```bash
pip install -r requirements.txt
```

3. 📂 Add input images

Place your images inside the `data/images/` folder. Make sure they are in `.jpg`, `.png`, etc. format.

_______________________________________________________________________________________________

▶️ Running the App

### 🔌 Start the FastAPI server

```bash
uvicorn train:app --reload
```

This will launch the server at:

📍 `http://127.0.0.1:8000`

____________________________________________________________________________________________

📌 Endpoints

✅ 1. Visit `/label-images` to auto-label your dataset  
🔗 Open:

```
http://127.0.0.1:8000/label-images
```

This will:

- Scan the images in `data/images/`
- Run YOLOv8-based object detection
- Generate and save labeled results to `output/labels_output.csv`
- Return a message confirming completion

✅ 2. Visit `/docs` for Swagger UI  
🔗 Open:

```
http://127.0.0.1:8000/docs
```

Here you can:

- Test the `/label-images` endpoint
- View API schema and interact with it easily

________________________________________________________________________________________

📝 Output Format

`output/labels_output.csv` contains the labeled data.

Example row format:

```
filename,x1,y1,x2,y2,...,label
image1.jpg,34,45,67,89,...,"cat"
```

Each polygon may be saved as a set of coordinates, along with the class label.

🙌 Acknowledgements

- FastAPI
- Ultralytics YOLOv8
- OpenCV / NumPy

