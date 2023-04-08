from adapters.adapter_interface import AdapterInterface
from platforms.googlemeet import Googlemeet

class GooglemeetAdapter(AdapterInterface):
    def __init__(self):
        self.obj = Googlemeet()

    def createmeetinglink(self):
        return self.obj.creategooglelink()

    def add_participants(self):
        return self.obj.add_participants_google()

    def schedule(self):
        return self.obj.schedule_google()