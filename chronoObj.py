
import distance
import datetime

class constants:
    def __init__(self):
        #ordered list of months
        self.month_names = ["JANUARY",
        "FEBRUARY",
        "MARCH",
        "APRIL",
        "MAY",
        "JUNE",
        "JULY",
        "AUGUST",
        "SEPTEMBER",
        "OCTOBER",
        "NOVEMBER",
        "DECEMBER"]
    #takes uppered monthstring, completed
    def getMonthNumber(self,mstring):
        if(mstring in self.month_names):
            for x in range(0, len(self.month_names)):
                if(self.month_names[x]== mstring.upper()):
                    return(x+1)
        return(None)
    def getMonthName(self, mint):
        return(self.month_names[mint+1])
    def expandMonthName(self, mstring):
        mstring=mstring.upper()
        closest_match_tri = ""
        closest_match_tri_full = ""
        cmtri_val = 1000000
        closest_match_total = ""
        cmtot_val = 1000000
        for x in range(0, len(self.month_names)):
            tot_cmr = distance.levenshtein(self.month_names[x], mstring)
            tri_cmr = distance.levenshtein(self.month_names[x][0:3], mstring)
            if(tri_cmr<cmtri_val):
                cmtri_val = tri_cmr
                closest_match_tri = self.month_names[x][0:3]
                closest_match_tri_full = self.month_names[x]
            if(tot_cmr<cmtot_val):
                cmtot_val = tot_cmr
                closest_match_total = self.month_names[x]
        return(closest_match_tri, closest_match_tri_full, closest_match_total)



class momentary:
    def __init__(self):
        self.time_lookups = constants()
        # // representations of the time to prevent repeated conversions 
        self.string_rep = None
        self.list_rep = None
        self.dt_rep = None
        self.iso_rep = None
        self.json_rep = None
        self.atf_rep = None

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
        self.minute = None

        self.second = None
        # max 1000
        self.milisecond = None

    #get difference in times
    def compare(self, t):
        pass
    
    def print_out(self):
        print("***** chronobj print out *****")
        print("---- DAY NUM    : "+ str(self.day))
        print("---- DAY NAME   : "+ str(self.dayname))
        print("---- MONTH NUM  : "+ str(self.month))
        print("---- MONTH NAME : "+ str(self.monthname))
        print("---- YEAR       : "+ str(self.year))
        print("---- HOUR       : "+ str(self.hour))
        print("---- MINUTE     : "+ str(self.minute))
        print("---- SECOND     : "+ str(self.second))
        print("---- mSECOND    : "+ str(self.milisecond))
        print("*****                    *****")
    #load from aidans time format
    # DDMMMYY
    # ex: 22NOV22
    def parse_atf(self, atf_t):
        day = int(atf_t[0:2])
        self.day = day
        month = (atf_t[2:5])
        self.monthname = self.time_lookups.expandMonthName(month)[1]
        self.month = int(self.time_lookups.getMonthNumber(self.monthname))
        year = int("20"+atf_t[5:7])
        self.year = year
        x = datetime.datetime(self.year, self.month, self.day)
        self.dayname = x.strftime('%A').upper()
        self.dt_rep = x
        self.atf_rep = atf_t
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
