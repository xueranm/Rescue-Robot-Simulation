#===============================================================================
# P3_View.py
# Created by Xueran Ma - 5-10-2016
# Version 3.0
# Implementation for Spring 2016 CIS 211 Project 3
# Derived in part from Dave Kieras' design and implementation of EECS 381 Proj 4
#===============================================================================

class View:
    '''
    The View object, in this project, displays a grid-like map view of all of the simulation objects.
    '''

    def __init__(self):
        #initial all the variables
        self.__size = 0
        self.obj__list = {}
        self.way__list = {}

    def create(self, world_size):
        #create the world size
        #Called by the Model object
        # after the users issues the “create world <n>” command.
        # Sets a “private” member variable that keeps track of the view size.
        self.__size = world_size

    def update_object(self, name, location):
        # Called by the model to add or move a SimObject (other than Waypoints) on the map.
        # Takes as arguments:
        # a lowercase string that is the name of a non-Waypoint object;
        # a tuple that is a valid map location.
        # Calls the view’s __update( ) method to add or modify the View object’s collection of non-Waypoint SimObjects.
        self.obj__list[name] = location

    def add_landmark(self, name, location):
        '''Behaves exactly the same as update_object( )
        but is used to add Waypoints to a separate collection of Waypoint SimObjects.
        These two separate collections are needed in order to place the Waypoints (the landmarks) in different map positions
        than the other SimObjects.
        '''
        self.way__list[name] = location

    def draw(self):
        # Draws the map grid as specified in the “Map View” section above.
        for i in range(self.__size, -1, -1):
            #find the line which need a mark such as 00 05 and print them
            if i % 5 == 0:
                #number with 2 digits
                if i >= 10:
                    print(i, end="")
                #number 0 and 5 which are 1 digit
                else:
                    if i == 5:
                        print("05", end="")
                    elif i == 0:
                        print("00", end="")
                #print each one stars or letters in the same line
                for j in range(self.__size + 1):
                    #put the waypoints' location together to find if it is inside the world
                    loc_list = []
                    for each in self.way__list:
                        loc_list.append(self.way__list[each])
                    if (j, i) in loc_list:
                        for key, value in self.way__list.items():
                            #if the location is inside the world, print the waypoint
                            if value == (j, i):
                                print(" %s" % key.upper(), end="")
                    #if there is no waypoint, print a star
                    else:
                        print(" .", end="")
                    #put the objects in the same position together
                    objects = []
                    for each in self.obj__list:
                        if self.obj__list[each][0] == j and self.obj__list[each][1] == i:
                            objects.append(each)
                    #if there is no object, print blank
                    if len(objects) == 0:
                        print("  ", end="")
                    #if there is one object, print it first letter
                    elif len(objects) == 1:
                        mark = objects[0][0].upper()
                        print("%s " % mark, end="")
                    #if there are more than one objects at the same position, print a star
                    else:
                        print("* ", end="")
            #those following are the lines which do not need marks
            else:
                print("  ",end="")
                # print each one stars or letters in the same line
                for j in range(self.__size + 1):
                    # put the waypoints' location together to find if it is inside the world
                    loc_list = []
                    for each in self.way__list:
                        loc_list.append(self.way__list[each])
                    if (j, i) in loc_list:
                        for key, value in self.way__list.items():
                            # if the location is inside the world, print the waypoint
                            if value == (j, i):
                                print(" %s" % key.upper(), end="")
                    # if there is no waypoint, print a star
                    else:
                        print(" .", end="")
                    # put the objects in the same position together
                    objects = []
                    for each in self.obj__list:
                        if self.obj__list[each][0] == j and self.obj__list[each][1] == i:
                            objects.append(each)
                    # if there is no object, print blank
                    if len(objects) == 0:
                        print("  ", end="")
                    # if there is one object, print it first letter
                    elif len(objects) == 1:
                        mark = objects[0][0].upper()
                        print("%s " % mark, end="")
                    # if there are more than one objects at the same position, print a star
                    else:
                        print("* ", end="")
            print()
        #print the colomn mark such as 00 05 10
        for q in range(self.__size + 1):
            if q % 5 == 0:
                if q == 0:
                    p = "00"
                elif q == 5:
                    p = "05"
                else:
                    p = q
                print("  ", p, "              ",end="")







