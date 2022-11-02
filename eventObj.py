
class event:
    def __init__(self):

        #task; can occur @ any time(s) X before time y
        #event; occurs @ time x for time y regardless
        self.type = None

        self.arrival = None
        self.deadline = None

        self.time_to_complete = None

        self.time_completed = None

        #actively being completed
        self.active = False 

        #time since deadline
        self.late_by = None

        #ignore this
        self.link = None


    #function to return time until deadline
    def time_to_deadline(self, t):
        return(0)
    
    #function to return time since arrival
    def time_since_arrival(self, t):
        return(0)

    #return time to complete of time left until deadline
    def haste(self, t):
        return(0)

    #update values if marked active etc etc
    def update(self, t):
        return(0)