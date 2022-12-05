import cv2
import mediapipe as mp

from model.Finger import Finger
from model.Hand import Hand
from model.Note import Note
from model.Piano import Piano
from HandsMotionTracking import HandsMotionTracking

mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

hand_right = Hand(Hand.RIGHT, [
    Finger(Finger.THUMB, 'C', Hand.RIGHT),
    Finger(Finger.INDEX, 'D', Hand.RIGHT),
    Finger(Finger.MIDDLE, 'E', Hand.RIGHT),
    Finger(Finger.RING, 'F', Hand.RIGHT),
    Finger(Finger.PINKY, 'G', Hand.RIGHT)
])

hand_left = Hand(Hand.LEFT, [
    Finger(Finger.THUMB, 'A', Hand.LEFT),
    Finger(Finger.INDEX, 'B', Hand.LEFT)
])

hands_motion_tracking = HandsMotionTracking(hand_right, hand_left)

piano = Piano([
    Note(Note.C, hand_right.get_finger(Finger.THUMB), './sounds/c.wav'),
    Note(Note.D, hand_right.get_finger(Finger.INDEX), './sounds/d.wav'),
    Note(Note.E, hand_right.get_finger(Finger.MIDDLE), './sounds/e.wav'),
    Note(Note.F, hand_right.get_finger(Finger.RING), './sounds/f.wav'),
    Note(Note.G, hand_right.get_finger(Finger.PINKY), './sounds/g.wav'),
    Note(Note.A, hand_left.get_finger(Finger.THUMB), './sounds/a.wav'),
    Note(Note.B, hand_left.get_finger(Finger.INDEX), './sounds/b.wav'),
])

hands_motion_tracking.add_listener(piano.on_key_pressed)


def main():

    with mp_hands.Hands(
            max_num_hands=2,
            min_detection_confidence=0.5) as hands:
        while cap.isOpened():
            ret, frame = cap.read()
            frame = cv2.flip(frame, 1)

            hands_motion_tracking.track(frame, hands)

            piano.draw(frame)

            cv2.imshow('Vision Artificial 2022 - Piano - Daniel Grosso', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
