from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from ultralytics import YOLO
import cv2
import os
import pandas as pd
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

# Pydantic model for input data
class LabelRequest(BaseModel):
    image_folder: str
    output_folder: str

# Encapsulate logic inside a CamelCase class
class AutoLabeler:
    def __init__(self, confidence_threshold=0.25):
        self.model = YOLO('yolov8x.pt')  # Use your model path here
        self.confidence_threshold = confidence_threshold

    def label_images(self, image_folder: str, output_folder: str):
        if not os.path.exists(image_folder):
            raise FileNotFoundError(f"Image folder not found: {image_folder}")

        os.makedirs(output_folder, exist_ok=True)

        output_data = []

        for image_name in os.listdir(image_folder):
            if image_name.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(image_folder, image_name)
                original_image = cv2.imread(image_path)
                if original_image is None:
                    logger.warning(f"Failed to read image: {image_path}, skipping.")
                    continue

                height, width, _ = original_image.shape

                results = self.model(image_path, conf=self.confidence_threshold)

                for result in results:
                    boxes = result.boxes
                    for box in boxes:
                        class_id = int(box.cls)
                        label = self.model.names[class_id]
                        confidence = float(box.conf)
                        xyxy = box.xyxy[0].tolist()
                        xmin, ymin, xmax, ymax = map(int, xyxy)

                        if confidence >= self.confidence_threshold:
                            output_data.append({
                                'Image': image_name,
                                'Label': label,
                                'Confidence': round(confidence, 3),
                                'Xmin': xmin,
                                'Ymin': ymin,
                                'Xmax': xmax,
                                'Ymax': ymax
                            })

                            # Draw bounding box & label
                            color = (0, 255, 0)
                            thickness = 1
                            cv2.rectangle(original_image, (xmin, ymin), (xmax, ymax), color, thickness)

                            text = f'{label}: {confidence:.2f}'
                            font = cv2.FONT_HERSHEY_SIMPLEX
                            font_scale = 1
                            font_thickness = 1
                            text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
                            text_x = xmin
                            text_y = ymin - 6 if ymin - 6 > 6 else ymin + text_size[1] + 6

                            if text_x + text_size[0] > width:
                                text_x = width - text_size[0] - 5

                            cv2.rectangle(original_image, (text_x, text_y - text_size[1] - 2),
                                          (text_x + text_size[0], text_y + 2), color, -1)
                            cv2.putText(original_image, text, (text_x, text_y), font, font_scale,
                                        (0, 0, 0), font_thickness, cv2.LINE_AA)

                output_image_path = os.path.join(output_folder, f"labeled_{image_name}")
                cv2.imwrite(output_image_path, original_image)

        csv_path = os.path.join(output_folder, "labeled_output_with_boxes.csv")
        df = pd.DataFrame(output_data)
        df.to_csv(csv_path, index=False)

        logger.info(f"Labeled images saved to {output_folder}")
        logger.info(f"CSV saved to {csv_path}")

        return {
            "message": "Labeling completed successfully",
            "output_folder": output_folder,
            "csv_file": csv_path
        }


app = FastAPI()
auto_labeler = AutoLabeler()


@app.get("/")
async def home():
    return {"message": "Welcome to the Auto Labeler API. Use POST /auto-label to label your images."}


@app.post("/auto-label")
async def auto_label(req: LabelRequest):
    try:
        result = auto_labeler.label_images(req.image_folder, req.output_folder)
        return result
    except FileNotFoundError as e:
        logger.error(f"File not found error: {e}")
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error(f"Error during labeling: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error during labeling")
