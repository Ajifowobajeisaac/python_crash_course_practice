"""This demonstrates the ability of functions to take an abitratry number of
arguments"""

def trip_destination(*destinations):
    """This function takes a variable range of destinations and print the out"""
    print(f"Pack your bags, We are going to: ")
    print(destinations)

# Note that this returns a tuple, that because that is the data structure python
# uses to store the argument. It is immutable and efficient prventing the function
# from modifying the argument
trip_destination('Bali') 
trip_destination('Bali', 'Santorini', 'Dubai', 'Morocco') 



# Now we can create a copy of the function that loops through the arguments
def trip_destination_loop(*destinations):
    """This function loops through a range of destinations and print the out"""
    print(f"Pack your bags, We are going to: ")
    for destination in destinations: 
        print(f"{destination}")

trip_destination_loop('Bali') 
trip_destination_loop('Bali', 'Santorini', 'Dubai', 'Morocco')


