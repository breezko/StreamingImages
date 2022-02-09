#!/usr/bin/env python
from flask import Flask, render_template, Response
from mss import tools, mss


app = Flask(__name__)


def get_screenshot(top=0, left=0, width=400, height=500):
    """Generate screenshot from region

    Args:
        top (int, optional): [description]. Defaults to 0.
        left (int, optional): [description]. Defaults to 0.
        width (int, optional): [description]. Defaults to 400.
        height (int, optional): [description]. Defaults to 500.

    Returns:
        [bytes]: [bytes of screenshot region]
    """
    with mss() as sct:
        rect = {"top": 0, "left": 0, "width": width, "height": height}
        sct_img = sct.grab(rect)
        return tools.to_png(sct_img.rgb, sct_img.size)


@app.route("/")
def index():
    """Video streaming home page."""
    return render_template("index.html")


def gen():
    """Video streaming generator function."""
    while True:
        frame = get_screenshot()
        yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")
    sock.close()


@app.route("/stream")
def stream():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(), mimetype="multipart/x-mixed-replace; boundary=frame")


if __name__ == "__main__":
    app.run(host="0.0.0.0", threaded=True)
