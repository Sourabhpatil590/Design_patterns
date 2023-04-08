from adapters.adapter_interface import AdapterInterface
from platforms.zoom import Zoom

class ZoomAdapter(AdapterInterface):
    def __init__(self):
        self.obj = Zoom()

    def create_link_(self):
        return self.obj.create_link_zoom()

    def add_participants(self):
        return self.obj.add_participants_zoom()

    def schedule(self):
        return self.obj.schedule_zoom()