import cv2


class HUD:

    @staticmethod
    def draw_text(
        frame,
        text,
        position,
        color=(255, 255, 255),
        scale=1
    ):

        cv2.putText(
            frame,
            text,
            position,
            cv2.FONT_HERSHEY_SIMPLEX,
            scale,
            color,
            2
        )