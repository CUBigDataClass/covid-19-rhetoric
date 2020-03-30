'''
Data class that contains information to use with twitter_scraper.
Each state consists of a city and a radius that best fits the entire state. 

Big Radius Tool
http://www.statsamerica.org/radius/big.aspx

Radius Calculator
https://ezlocal.com/tools/map-radius/
'''

class US_States_Info():

    def __init__(self):
        self.state_abbreviations = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", 
                                    "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", 
                                    "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", 
                                    "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

        self.US_cities_with_radius = {
            "AL" :{
                "city": "Birmingham,AL",
                "radius": 125
            },
            "AK" :{
                "city": "Anchorage,AK",
                "radius": 125
            },
            "AR" :{
                "city": "Little Rock,AR",
                "radius": 125
            },
            "AZ" :{
                "city": "Phoenix,AZ",
                "radius": 175
            },
            "CA" :{
                "city": "Fresno,CA",
                "radius": 275
            }, 
            "CO" :{
                "city": "Denver,CO",
                "radius": 175
            },
            "CT" :{
                "city": "Wethersfield,CT",
                "radius": 50
            }, 
            "DE" :{
                "city": "Dover,DE",
                "radius": 35
            }, 
            "FL" :{
                "city": "Orlando,FL",
                "radius": 225
            },
            "GA" :{
                "city": "Macon,GA",
                "radius": 150
            },
            "HI" :{
                "city": "Lahaina,HI",
                "radius": 300
            },
            "ID" :{
                "city": "Sun Valley,ID",
                "radius": 150
            },
            "IL" :{
                "city": "Bloomington,IL",
                "radius": 140
            },
            "IN" :{
                "city": "Indianapolis,IN",
                "radius": 100
            }, 
            "IA" :{
                "city": "Des Moines,IA",
                "radius": 125
            },
            "KS" :{
                "city": "McPherson,KS",
                "radius": 150
            },
            "KY" :{
                "city": "Lexington,KY",
                "radius": 100
            },
            "LA" :{
                "city": "Alexandria,LA",
                "radius": 100
            }, 
            "ME" :{
                "city": "Bangor,ME",
                "radius": 120
            },
            "MD" :{
                "city": "Baltimore,MD",
                "radius": 45
            },
            "MA" :{
                "city": "Waltham,MA",
                "radius": 35
            },
            "MI" :{
                "city": "Lansing,MI",
                "radius": 100
            },
            "MN" :{
                "city": "St Cloud,MN",
                "radius": 155
            },
            "MS" :{
                "city": "Forest,MS",
                "radius": 100
            },
            "MO" :{
                "city": "Jefferson City,MO",
                "radius": 130
            },
            "MT" :{
                "city": "Lewistown,MT",
                "radius": 210
            },
            "NE" :{
                "city": "Columbus,NE",
                "radius": 100
            },
            "NV" :{
                "city": "Las Vegas,NV",
                "radius": 50
            },
            "NH" :{
                "city": "Concord,NH",
                "radius": 40
            },
            "NJ" :{
                "city": "Freehold,NJ",
                "radius": 30
            },
            "NM" :{
                "city": "Albuquerque,NM",
                "radius": 160
            },
            "NY" :{
                "city": "Syracuse,NY",
                "radius": 210
            },
            "NC" :{
                "city": "Raleigh,NC",
                "radius": 140
            },
            "ND" :{
                "city": "McClusky,ND",
                "radius": 180
            },
            "OH" :{
                "city": "Columbus,OH",
                "radius": 130
            },
            "OK" :{
                "city": "Oklahoma City,OK",
                "radius": 130
            },
            "OR" :{
                "city": "Bend,OR",
                "radius": 150
            },
            "PA" :{
                "city": "State College,PA",
                "radius": 160
            },
            "RI" :{
                "city": "Johnston,RI",
                "radius": 15
            },
            "SC" :{
                "city": "Columbia,SC",
                "radius": 100
            },
            "SD" :{
                "city": "Pierre,SD",
                "radius": 200
            },
            "TN" :{
                "city": "Nashville,TN",
                "radius": 70
            },
            "TX" :{
                "city": "Lampasas,TX",
                "radius": 270
            },
            "UT" :{
                "city": "Provo,UT",
                "radius": 150
            },
            "VT" :{
                "city": "Montpelier,VT",
                "radius": 50
            },
            "VA" :{
                "city": "Charlottesville,VA",
                "radius": 90
            },
            "WV" :{
                "city": "Burnsville,WV",
                "radius": 90
            },
            "WI" :{
                "city": "Stevens Point,WI",
                "radius": 155
            },
            "WY" :{
                "city": "Casper,WY",
                "radius": 155
            },
        }

    def get_US_cities_with_radius(self):
        """
        Gets information needed to bulid queries for twitter_scraper
            
            Parameters
            ----------
            None
            
            Returns
            -------
            US_cities_with_radius : dictionary object
                Conatins all states as abbreviations (key) with city name and radius as values
        """
        return self.US_cities_with_radius
    
    def get_state_abbreviations(self):
        """
        Gets python list of US state abbreaviations 
            
            Parameters
            ----------
            None
            
            Returns
            -------
            state_abbreviations : list object
                Conatins all states as abbreviations
        """
        return self.state_abbreviations
