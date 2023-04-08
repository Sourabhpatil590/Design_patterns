from adapters.adapter_interface import AdapterInterface
from platforms.teams import Teams

class TeamsAdapter(AdapterInterface):
    def __init__(self):
        self.obj = Teams()

    def createmeetinglink(self):
        return self.obj.create_link_teams()

    def add_participants(self):
        return self.obj.add_participants_teams()

    def schedule(self):
        return self.obj.schedule_teams()