# Ryan Ge
# November 10, 2016
# test the trip class


def main():
    '''
    main function
    :return:
    '''
    import trip

    # fetch data
    my_trip = trip.Trip('Sandy Spring, MD', 'New York, NY')

    # print the results
    print('Distance: ' + my_trip.distance('driving') + 'm ')
    print('Duration: ' + my_trip.duration())
    print(my_trip)

main()
