import datetime
import time

from django.db.models import Count
from django.shortcuts import render

# Create your views here.

from .models import Instance
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
import threading
import time

lock = threading.Lock()

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

def get_frame(self):
    return self.frame


def update(self):
    while True:
        time.sleep(0.05)
        with lock:
            (self.grabbed, self.frame) = self.video.read()


def gen(camera):
    global lock

    while True:
        # time.sleep(0.05)
        with lock:
            frame = camera.get_frame()

            if frame is None:
                continue

            flag, frame = cv2.imencode(".jpg", frame)

            if not flag:
                continue

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + bytearray(frame) + b'\r\n')


@gzip.gzip_page
def livefeed(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:  # This is bad! replace it with proper handling
        pass


def index(request):
    """View function for home page of site."""
    midnight_today = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

    # # Generate counts of some of the main objects
    num_instances_today = Instance.objects.filter(time__lte=datetime.datetime.now(), time__gt=midnight_today).count()
    num_instances = Instance.objects.all().count()


    context = {
        'today':num_instances_today,
        'alltime':num_instances,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'home.html', context=context)



