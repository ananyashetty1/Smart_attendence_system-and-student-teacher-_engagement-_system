# Minimal local shim for gaze_tracking.GazeTracking
# This is a lightweight replacement so the application can run without
# the external `gaze-tracking` package. It's intentionally simple and
# not suitable for production gaze detection — install the real package
# later for accurate results.

import cv2

class GazeTracking:
    def __init__(self):
        self.frame = None

    def refresh(self, frame):
        # Store the last frame (the real package would analyze it)
        self.frame = frame

    def annotated_frame(self):
        # Return a copy of the stored frame with a small overlay
        if self.frame is None:
            return None
        out = self.frame.copy()
        h, w = out.shape[:2]
        # Draw a simple center marker
        cv2.circle(out, (w//2, h//2), 10, (255, 0, 0), 2)
        return out

    def is_right(self):
        return False

    def is_left(self):
        return False

    def is_center(self):
        return True
