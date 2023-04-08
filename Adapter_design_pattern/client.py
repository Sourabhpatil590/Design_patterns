from calendly import Calendly

if __name__ == '__main__':
    calendly = Calendly()
    calendly.select_platform()
    calendly.platform.createmeetinglink()
    calendly.platform.add_participants()
    calendly.platform.schedule()