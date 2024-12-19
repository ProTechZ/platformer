import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

class HandDetector:
    def __init__(self, detection_confidence=0.8, num_hands=1):
        self.model = mp_hands.Hands(max_num_hands=num_hands, min_detection_confidence=detection_confidence)

        self.cap = cv2.VideoCapture(0)
        self.last_pos = None

    def stop(self):
        self.cap.release()
        cv2.destroyAllWindows()

    def detect_hand_movement(self, hand_landmarks):    
        landmarks = hand_landmarks.landmark

        # getting avg of all the landmarks
        curr_pos = round(sum([landmark.x for landmark in landmarks]) / len(landmarks), 3)

        if self.last_pos is not None:

            # moving left means the pos value decreases so the cur_pos would be smaller
            if (self.last_pos - curr_pos) >= 0.01:
                print("Moving left")

            # moving right means the pos value increases so the cur_pos would be greater
            elif (curr_pos - self.last_pos) >= 0.01:
                print("Moving right")

        self.last_pos = curr_pos

    def run(self):
        success, frame = self.cap.read()

        if not success or cv2.waitKey(1) == ord('q'):
            return None

        # flipping the frame returns how the pic should look in real life, as the webcam will show a flipped video
        reg_frame = cv2.flip(frame, 1)
        frame_rgb = cv2.cvtColor(reg_frame, cv2.COLOR_BGR2RGB)
        results = self.model.process(frame_rgb)

        if results.multi_hand_landmarks:  
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(reg_frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                self.detect_hand_movement(hand_landmarks)

        return frame
        