import sys
import pip

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

try:
    from google.transit import gtfs_realtime_pb2
except ImportError:
    install('gtfs-realtime-bindings')
    from google.transit import gtfs_realtime_pb2

feed = gtfs_realtime_pb2.FeedMessage()
try:
    with open('A.pb', 'rb') as f:
        feed.ParseFromString(f.read())
    print("Sukces!, entities:", len(feed.entity))
except Exception as e:
    print("Błąd:", e)
