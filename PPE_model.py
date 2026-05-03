import cv2
from ultralytics import YOLO

# Load model
model = YOLO("best.pt")

# Video input
cap = cv2.VideoCapture("video9.mp4")  # or 0 for webcam
cv2.namedWindow("PPE Detection", cv2.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()
    if not ret:
        print("📴 Video ended or error.")
        break

    # Run detection
    results = model(frame)[0]

    # ✅ YOLOv8’s default drawing (clean and colored)
    annotated_frame = results.plot()
    

    # Resize to fit screen
    annotated_frame = cv2.resize(annotated_frame, (960, 540))

    # Show result
    cv2.imshow("PPE Detection", annotated_frame)

    # Alerts
    for box in results.boxes:
        cls_name = model.names[int(box.cls[0])]
        if cls_name in ['no-helmet', 'no-vest']:
            print(f"🚨 ALERT: {cls_name.upper()} detected!")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("🛑 Exited by user.")
        break

cap.release()
cv2.destroyAllWindows()
