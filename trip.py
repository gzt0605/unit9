# Ryan Ge
# November 10, 2016
# Design own class that will interact with the Google Map API

import urllib.request

class Trip:

    def __init__(self, origin, destination):
        '''
        obtain parameters and process them for url
        :param origin: origin string
        :param destination: destination string
        :return: returns nothing
        '''
        self.origin_common = origin
        self.destination_common = destination

        # split the origin string into separate fragments
        origin_list = origin.split(',')
        self.origin = origin_list[0] + origin_list[1]
        origin_list = self.origin.split(' ')
        self.origin = origin_list[0]

        # join them with plus signs
        for i in origin_list[1:]:
            self.origin = self.origin + '+' + i

        # operate the same process for destination
        destination_list = destination.split(',')
        self.destination = destination_list[0] + destination_list[1]
        destination_list = self.destination.split(' ')
        self.destination = destination_list[0]
        for i in destination_list[1:]:
            self.destination = self.destination + '+' + i

    def distance(self, method):
        '''
        open the url and read the distance from it
        :param method: type of transportation, walking, driving, or bicycling
        :return: the distance value
        '''

        # put together the url
        self.url = 'http://maps.googleapis.com/maps/api/distancematrix/json?origins=' + self.origin + '&destinations=' + self.destination + '&mode=' + method + '&sensor=false'
        print(self.url)

        # access and read the page

        self.page = urllib.request.urlopen(self.url)
        self.page_content = str(self.page.read())
        self.page.close()
        print(self.page_content)

        # get starting and ending index for the distance value
        self.index_start = self.page_content.find('value') + 9
        self.index_end = self.page_content.find('"', self.index_start) - 2

        # read the part of distance
        self.dist = self.page_content[self.index_start:self.index_end]
        return self.dist

    def duration(self):
        '''
        read the duration value
        :return: duration value
        '''

        # get starting and ending index for the string
        self.index_start = self.page_content.find('text', self.index_end) + 9
        self.index_end = self.page_content.find('"', self.index_start)

        # read the duration
        self.duration = self.page_content[self.index_start:self.index_end]
        return self.duration

    def __str__(self):
        '''
        give the value for the instance
        :return: value of instance
        '''
        return 'Origin: ' + self.origin_common + '. Destination: ' + self.destination_common


