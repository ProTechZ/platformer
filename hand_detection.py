import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

model = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.8)
cap = cv2.VideoCapture(0)

last_pos = None

def hand_movement(hand_landmarks):
    global last_pos
    
    landmarks = hand_landmarks.landmark
    avg_pos = round(sum([landmark.x for landmark in landmarks]) / len(landmarks), 2)
    
    if last_pos is not None:
        if avg_pos < last_pos:
            print("Moving left")
        elif avg_pos > last_pos:
            print("Moving right")
    
    last_pos = avg_pos

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # flipping the frame returns how the pic should look in real life, as the webcam will show a flipped video
    reg_frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(reg_frame, cv2.COLOR_BGR2RGB)
    
    results = model.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(reg_frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            hand_movement(hand_landmarks)

    cv2.imshow('Platformer', reg_frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()