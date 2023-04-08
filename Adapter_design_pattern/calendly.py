from list_of_platforms.platformlist import Platformlist
from adapters.googlemeetadapter import GooglemeetAdapter
from adapters.teamsadapter import TeamsAdapter
from adapters.zoomadapter import ZoomAdapter

class Calendly:
    def __init__(self):
        self.platform = None

    def select_platform(self):
        self.platform = input('select the plaform ')
        self.return_obj(self.platform)
    
    def return_obj(self, type):
 
        if type == Platformlist.GOOGLEMEET.name:
            self.platform = GooglemeetAdapter()
        elif type == Platformlist.TEAMS.name:
            self.platform = TeamsAdapter()
        elif type == Platformlist.ZOOM.name:
            self.platform = ZoomAdapter()
        else:
            print('Invalid input')

    
