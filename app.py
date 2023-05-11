#!/usr/bin/env python
from flask import Flask, render_template, Response
from mss import tools, mss
import win32gui
import sys
import time
app = Flask(__name__)

win_name = sys.argv[1]
"""import mss

with mss.mss() as sct:
    monitor_number = 1
    mon = sct.monitors[monitor_number]
    top, left, width, height = [19,116, 328, 210]
    print(mon)
    rect = {"top": top, "left": left, "width": width, "height": height, "mon": 1}
    sct = sct.grab(rect)
    mss.tools.to_png(sct.rgb, sct.size, output="output.png")


sys.exit()
"""
def fetch_screen(name):
    print(name)
    hwnd_parent = win32gui.GetDesktopWindow()
    hwnd = win32gui.FindWindowEx(hwnd_parent, None, None, name)
    if hwnd == 0:
        print(f"Window '{name}' not found.")
        return None

    win32gui.SetForegroundWindow(hwnd)
    top, left, right, bottom = win32gui.GetWindowRect(hwnd)
    width = right - top
    height = bottom - left
    print(left, top, right, bottom, width, height)
    return left, top, width, height


def get_screenshot(top, left, width, height):
    with mss() as sct:
        monitor_info = sct.monitors[1]  # Adjust index if necessary
        offset_left = monitor_info["left"]
        offset_top = monitor_info["top"]

        window_left = left - offset_left
        window_top = top - offset_top
        window_right = window_left + width
        window_bottom = window_top + height

        rect = {"top": window_top, "left": window_left, "width": width, "height": height}
        sct_img = sct.grab(rect)
        return tools.to_png(sct_img.rgb, sct_img.size)

@app.route("/")
def index():
    """Video streaming home page."""
    return render_template("index.html")


def gen():
    """Video streaming generator function."""
    rect = fetch_screen(win_name)
    print(rect)
    while True:
        frame = get_screenshot(*rect)
        yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")
    sock.close()


@app.route("/stream")
def stream():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(), mimetype="multipart/x-mixed-replace; boundary=frame")


if __name__ == "__main__":
    app.run(host="0.0.0.0", threaded=True)
