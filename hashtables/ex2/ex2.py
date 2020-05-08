#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    
    flight_libary = dict() # Make dict
    
    for ticket in tickets:
        flight_libary[ticket.source] = ticket.destination

    print(flight_libary)

    route = []
    curr_destination = flight_libary["NONE"]
    print(curr_destination)

    while curr_destination != "NONE": # As long as curr_destination is not NONE  
        route.append(curr_destination) # adds curr_destination to route 
        curr_destination = flight_libary[curr_destination]
    route.append("NONE")
    return route