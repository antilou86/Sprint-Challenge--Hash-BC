#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

tickets = [
  Ticket("PIT", "ORD"),
  Ticket("XNA", "CID"),
  Ticket("SFO", "BHM"),
  Ticket("FLG", "XNA"),
  Ticket("NONE", "LAX"),
  Ticket("LAX", "SFO"),
  Ticket("CID", "SLC"),
  Ticket("ORD", "NONE"),
  Ticket("SLC", "PIT"),
  Ticket("BHM", "FLG")
]

def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    #keep track of current index
    i = 0

    #loop through tickets array, and insert into table. sources are the keys, destinations are the value.
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)
        
        #special handler for the first ticket. this will always be the first index
        if ticket.source=='NONE':
            route[i]=ticket.destination
            i += 1
    
    #fill up the route dynamicArray with the next destination by retrieving the previously stored desitation.
    while i < length:
        route[i] = hash_table_retrieve(hashtable, route[i-1])
        i += 1
        
    return route
