import cv2, numpy as np, sys, time

# ANSI codes for background colors
COLORS = {
    'happy':   '\033[42m',   # green
    'neutral': '\033[47m',   # white
    'sad':     '\033[44m',   # blue
    'angry':   '\033[41m',   # red
    'surprise':'\033[45m',   # magenta
    'reset':   '\033[0m'
}

# Load pre‑trained Haar cascades
face_cascade   = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade    = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
smile_cascade  = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

def get_mood(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(60, 60))
    if not faces:
        return 'neutral'
    # work with the largest detected face
    x, y, w, h = max(faces, key=lambda r: r[2] * r[3])
    roi_gray = gray[y:y + h, x:x + w]

    # mouth (smile) detection → happy
    smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20, minSize=(25, 25))
    if len(smiles) > 0:
        return 'happy'

    # eye detection → neutral (simple fallback)
    eyes = eye_cascade.detectMultiScale(roi_gray)
    if len(eyes) >= 2:
        return 'neutral'

    return 'neutral'

def set_color(mood):
    sys.stdout.write(COLORS.get(mood, COLORS['neutral']) + f'Mood: {mood}{COLORS["reset"]}\n')
    sys.stdout.flush()

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print('Webcam not available')
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        mood = get_mood(frame)
        set_color(mood)

        cv2.imshow('Webcam', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        time.sleep(1)   # limit output rate

    cap.release()
    cv2.destroyAllWindows()
    sys.stdout.write(COLORS['reset'])

if __name__ == '__main__':
    main()