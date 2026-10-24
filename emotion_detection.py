
import cv2
from deepface import DeepFace

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Camera not open")
    raise SystemExit

print("FaceMood started! press q to close.")

while True:
    success, frame = camera.read()

    if not success:
        print("Camera se video nahi mil rahi!")
        break

    try:
        result = DeepFace.analyze(
            img_path=frame,
            actions=["emotion"],
            detector_backend="opencv",
            enforce_detection=False,
            silent=True
        )

        if result:
            emotion = result[0]["dominant_emotion"]
            region = result[0]["region"]

            x = region["x"]
            y = region["y"]
            w = region["w"]
            h = region["h"]

            if w > 0 and h > 0:
                cv2.rectangle(
                    frame,
                    (x, y),
                    (x + w, y + h),
                    (0, 255, 0),
                    2
                )

                cv2.putText(
                    frame,
                    emotion.upper(),
                    (x, max(y - 10, 25)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 0),
                    2
                )

    except Exception as error:
        print("Detection error:", error)

    cv2.imshow("FaceMood - Emotion Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
