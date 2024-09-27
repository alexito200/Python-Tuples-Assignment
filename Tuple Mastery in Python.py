# Task 1: Formatting Flight Itineraries

# slice the tuples, name them and print them out individually
# use enumerate() to list out the strings
# use formatted string to print
# the itinerary should be sequentially ascending

my_tuples_list = [("Alex", "New York", "Okinawa"), ("Vitoria", "Middletown", "Sydney")]


def itinerary_list(my_tuples_list):

    name, origin, destination = my_tuples_list[0]
    name2, origin2, destination2 = my_tuples_list[1]


    print(f' itinerary 1: {name} will be flying from {origin} to {destination}')
    print(f' itinerary 2: {name2} will be flying from {origin2} to {destination2}')

itinerary_list(my_tuples_list)










