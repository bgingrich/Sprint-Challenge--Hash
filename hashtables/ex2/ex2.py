#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    
    """
    YOUR CODE HERE
    """
    flight_dict = dict()
    for flight in tickets:
        flight_dict[flight.source] = flight.destination

    route = []
    current_destination = flight_dict["NONE"]

    while current_destination != "NONE":
        route.append(current_destination)
        current_destination = flight_dict[current_destination]
    route.append("NONE")

    return route
