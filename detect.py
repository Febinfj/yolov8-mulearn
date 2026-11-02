from ultralytics import YOLO

def main():
    # 1. Load a pre-trained YOLOv8 nano model
    print("Loading YOLOv8 nano model (yolov8n.pt)...")
    model = YOLO("yolov8n.pt")

    # 2. Image source to perform detection on
    image_source = "https://ultralytics.com/images/bus.jpg"
    print(f"Running object detection on: {image_source}")

    # 3. Perform object detection
    results = model(image_source)

    # 4. Save the resulting image with bounding boxes drawn
    for result in results:
        output_filename = "results.jpg"
        result.save(filename=output_filename)
        print(f"Successfully saved detection output to '{output_filename}'.")

if __name__ == "__main__":
    main()
