import datetime
class momentary:
    def __init__(self):
        # // representations of the time to prevent repeated conversions 
        self.string_rep = None
        self.list_rep = None
        self.dt_rep = None
        self.iso_rep = None
        self.json_rep = None

        # // named, non-numerical units
        self.dayname = None
        self.monthname = None
        
        # // numerical units

        # no limit
        self.year = None
        
        #max 12
        self.month = None
        # max 31
        self.day = None
        # max 24
        self.hour = None
        # max 60
        self.second = None
        # max 1000
        self.milisecond = None

    #get difference in times
    def compare(self, t):
        pass

    #load from datetime object
    def parse_dt(self, dt_t):
        pass
    
    #load from string
    def parse_string(self, str_t):
        pass

    #fuzzy load
    def parse_fuzzy_string(self, str_t):
        pass

class slice:
    def __init__(self):
        # // representations of the time to prevent repeated conversions 
        self.string_rep = None
        self.list_rep = None
        self.dt_rep = None
        self.iso_rep = None
        self.json_rep = None
