firstname = "Aliyu"    #get new values from the web form 
surname = "Alege"

class driver:
    def __init__(self, name, tag, vehicle_type, plate_number,
                 v_number, v_colour, empty_seats, location,
                 route, min_fee, max_fee):
        self.name = name
        self.tag = tag
        self.vehicle_type = vehicle_type
        self.plate_number = plate_number
        self.v_number = v_number #Vehicle's serial number
        self.v_colour = v_colour
        self.empty_seats = empty_seats #number of empty seats
        self.location = location #driver's current location
        self.route = route #the probable route of the driver
        self.min_fee = 0
        self.max_fee = max_fee

class client:
    def __init__(self, tag, name, current_location, destination):
        self.name = name
        self.tag = tag
        self.current_location = current_location
        self.destination = destination

def calculate_distance():
    distance = current_location + destination #output result in km (use google maps)
    return distance

def calculate_max_fee(distance):
    """
Calculate the maximum fee the driver is expected to take and store in db,
to be outputed to the client! distance is claculated from the client's side
by getting the info from thier current location to thier final destination
"""
    max_fee = distance * 33.33
    return max_fee

def generate_tag(name):
    from random import randrange, seed
    seed(1000)
    tag = name[0]+name[1]+str(randrange(1, 9000))
    return tag

def get_name(surname, firstname):
    name = surname + firstname
    return name

def get_location():
    #get location auto, show on the map 
    return location

def get_current_location():
    #get current location auto, show on the map
    return current_location

def get_destination():
    #get destination from user input, show on the map 
    return destination



    

    

    
    
