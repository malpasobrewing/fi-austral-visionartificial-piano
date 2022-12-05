from HandsMotionTracking import HandsMotionTracking
from sounds.SoundPlayer import SoundPlayer


class Piano:
    def __init__(self, notes):
        self.notes = notes
        self.show = False
        self.player = SoundPlayer()

    def on_key_pressed(self, hand, finger, hands_motion_event):

        if hands_motion_event == HandsMotionTracking.NO_HANDS:
            for note in self.notes:
                note.finger.reset()
        else:
            note = self.get_note(hand, finger)
            if note is not None:
                if hands_motion_event == HandsMotionTracking.FINGER_CLOSE_EVENT:
                    note.playing = False
                elif hands_motion_event == HandsMotionTracking.FINGER_OPEN_EVENT:
                    if note.playing is False:
                        note.play(self.player)

    def get_note(self, hand, finger):
        for note in self.notes:
            if note.finger.hand_id == hand.id and note.finger.id == finger.id:
                return note
        return None

    def draw(self, frame):
        for note in self.notes:
            note.draw(frame)
