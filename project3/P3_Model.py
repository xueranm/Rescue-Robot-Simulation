#===============================================================================
# P3_Model.py
# Created by Xueran Ma - 5-11-2016
# Credit: P2, as the basis, is from professor's code
# Version 3.0
# Implementation for Spring 2016 CIS 211 Project 2
# Derived in part from Dave Kieras' design and implementation of EECS 381 Proj 4
#===============================================================================


class Model:
    '''
    The Model object keeps track of everything in the simulated world.
    Only one Model should be created in each run of the simulation.
    '''

    #===========================================================================
    def __init__(self):
        self.__world_size = None
        self.__humans = []
        self.__robots = []
        self.__objects = []
        self.__waypoints = []
        self.__view = None # initial the view

    #===========================================================================
    def __str__(self):
        return "The world is of size " + str(self.__size)

    #===========================================================================
    def get_world_size(self):
        return self.__world_size

    #===========================================================================
    def get_valid_location(self, arg1, arg2=None):
        '''
        Determine if a location is in the world.  If yes, returns a tuple of ints.
        This function is made polymorphic by using "switch on type".

        Parameters: arg1 and arg2 are ints, OR
                    arg1 and arg2 are strings, OR
                    arg1 is a tuple of two ints, and no arg2 is provided, OR
                    arg1 is a tuple of two strings, and no arg2 is provided
        Returns:    a tuple of ints if the location is in the world
                    None otherwise.

        Examples of use if the world is of size 30:
        self.get_valid_location(10, 20) -> (10, 20)
        self.get_valid_location('10', '20') -> (10, 20)
        self.get_valid_location((10, 20)) -> (10, 20)
        self.get_valid_location('a', '20') -> None
        self.get_valid_location(1.0, 20) -> None
        '''

        # Switch on type.  If arguments are...

        # (int, int)
        if type(arg1) == type(arg2) == int:
            x = arg1
            y = arg2

        # (str, str)
        elif type(arg1) == type(arg2) == str and arg1.isdigit() and arg2.isdigit():
            x = int(arg1)
            y = int(arg2)

        # (tuple of two ints)
        elif (arg2 == None and type(arg1) == tuple and len(arg1)==2 and
                type(arg1[0])==int and type(arg1[1])==int):
            x = arg1[0]
            y = arg1[1]

        # (tuple of two strings which can convert into digits)
        elif (arg2 == None and type(arg1) == tuple and len(arg1)==2 and
                type(arg1[0])==str and type(arg1[1])==str and
                arg1[0].isdigit() and arg1[1].isdigit()):
            x = int(arg1[0])
            y = int(arg1[1])

        # Arguments not handled, or invalid location.
        else:
            # print("Error: Model.get_valid_location() arguments not handled.")
            return None # The provided arguments are not handled.

        # If the location is in the world, return True.
        if (x >= 0 and y >= 0 and
                x <= self.__world_size and y <= self.__world_size):
            return (x, y)
        else:
            return None

    #===========================================================================
    def create_sim_object(self, arg_list):
        '''
        Create a simulation object based on the contents of the arg_list.
        Parameters: arg_list, list of strings entered after "create" command
        Returns:    True for if the line cannot be parsed, False if it can be.

        The only assumption that can be made about the arg_list when entering
        this function is that there was at least one string in the command line
        after "create".
        '''

        MIN_WORLD_SIZE = 10
        MAX_WORLD_SIZE = 30

        # Continue here checking for all of the different objects that "create"
        # could be called to build.  For each, after checking for the string
        # that appeared after "create", make sure that any additional arguments
        # on the line are all permissable given the project specification.


        #=======================================================================
        # World
        kinds = ['human', 'fire','robot','waypoint']
        if arg_list[0]=='world':
            # Else return error.

            # Verify that there is one additional argument and it is an integer.
            if len(arg_list) == 2 and arg_list[1].isdigit():
                size = int(arg_list[1])
                self.__view.create(size)
            else:
                return True

            # If a world has aleady been created
            if (self.__world_size):
                # Then return an error.
                print("Error: World already exists.")
                return False  # Error was reported, so no need to return an error flag.

            # Verify size is in range.
            if size < MIN_WORLD_SIZE or size > MAX_WORLD_SIZE:
                print ("Error: World size is out of range.")
            else:
                # Else create the world.
                print('Creating world of size ', size, '.', sep='')
                self.__world_size = size

        #=======================================================================
        # Make sure a world exists.
        # If there is no world yet, then there can be no waypoints.
        elif not self.get_world_size():
            print ("Error: A world must be created before any other objects.")
            return False  # Error was reported, so no need to return an error flag.

        #=======================================================================
        # Human
        elif arg_list[0] in kinds:

            # If the number of arguments is wrong
            if len(arg_list) != 4:
                return True # Return an error code.
            # If the name is not alphanumeric
            elif not arg_list[1].isalnum():
                print("Error: Name must be alphanumeric.")
                return False
            elif self.get_human(arg_list[1]) or self.get_robot(arg_list[1]) or self.get_object(arg_list[1]) or self.get_waypoint_location(arg_list[1]):
                print("Error: %s already exists with that name."%arg_list[1].capitalize())
                return False
            # If <x> <y> is not a valid location
            elif not self.get_valid_location(arg_list[2], arg_list[3]):
                print("Error: Invalid location.")
                return False
            # Else this appears to be a valid input, and so
            #   create a human at the location.
            else:
                if arg_list[0] == "human":
                    new_location = self.get_valid_location(arg_list[2], arg_list[3])
                    print("Creating human ", arg_list[1].capitalize(), " at location ", new_location,".", sep='')
                    self.__humans.append(Human(arg_list[1].lower(), new_location))
                    self.__view.update_object(arg_list[1],new_location)
                elif arg_list[0] == "waypoint":
                    new_location = self.get_valid_location(arg_list[2], arg_list[3])
                    print("Creating waypoint ", arg_list[1].capitalize(), " at location ", new_location, ".", sep='')
                    self.__waypoints.append(Waypoint(arg_list[1].lower(), new_location))
                    self.__view.add_landmark(arg_list[1], new_location)
                elif arg_list[0] == "fire":
                    new_location = self.get_valid_location(arg_list[2], arg_list[3])
                    print("Creating fire ", arg_list[1].capitalize(), " at location ", new_location, ".", sep='')
                    self.__objects.append(Fire(arg_list[1].lower(), new_location))
                    self.__view.update_object(arg_list[1], new_location)
                elif arg_list[0] == 'robot':
                    new_location = self.get_valid_location(arg_list[2], arg_list[3])
                    print("Creating robot ", arg_list[1].capitalize(), " at location ", new_location, ".", sep='')
                    self.__robots.append(Robot(arg_list[1].lower(), new_location))
                    self.__view.update_object(arg_list[1], new_location)


            # self.__humans/robots/fires/waypoints.append

        #=======================================================================
        # Invalid create command.
        else:
            # print(invalid_create_command_string)
            return True # Return Error flag

    #===========================================================================
    def get_human(self, name):
        '''
        # Takes a name string.  Looks for a human with that name.  If one exists,
        #   returns that human.  If one does not, returns None.

        Parameters: name, a string
        Returns:    Either a pointer to a human object, or False
        '''
        for i in self.__humans:
            if i.get_name() == name:
                return i
        else:
            return None
    #===========================================================================
    def get_waypoint_location(self,name):
        '''Takes a name string. Looks for a waypoint with that name.
        If one exists, returns its location. If one does not exist, returns None.'''
        for i in self.__waypoints:
            if i.get_name() == name:
                return i.get_location()
        else:
            return None


    #===========================================================================
    def get_robot(self, name):
        for i in self.__robots:
            if i.get_name() == name:
                return i
        else:
            return None
    #===========================================================================
    def get_object(self, name):
        for i in self.__objects:
            if i.get_name() == name:
                return i
        else:
            return None
    #===========================================================================
    def notify_location(self,name,location):
        self.__view.update_object(name,location)




    #===========================================================================
    def attach_view(self,v):
        '''Attaches a View object v to the Model.'''
        self.__view= v

    #===========================================================================
    def describe_all(self):
        '''
        Each of the simulation objects describes itself in text.

        ( ) -> None
        '''
        print("The contents of the world are as follows:")
        if self.get_world_size():
            print ("The world is of size ", self.get_world_size(), ".", sep='')
        for i in self.__waypoints:
            print(i)
        for i in self.__humans:
            print (i)
        for i in self.__robots:
            print(i)
        for i in self.__objects:
            print(i)

#===============================================================================
#===============================================================================
class SimObject:
    def __init__(self,name,location):
        self._name = name.lower()
        self._location = location

    def __str__(self):
        return ("{} at location {}".format(self._name.capitalize(),self._location))

    def get_name(self):
        return self._name

    def get_class_name(self):
        '''Returns the object’s class name, such as “Human”.'''
        return type(self).__name__

    def get_location(self):
        return self._location

#===============================================================================
class Waypoint(SimObject):
    def __str__(self):
        return "Waypoint " + super().__str__()


#===============================================================================
class Traveler(SimObject):

    def move_to(self,location, the_model):
        if type(location) == tuple:
            self._location = location
            print("%s %s moved to location "%(str(self.get_class_name()),self._name.capitalize()),self._location)
            the_model.notify_location(self._name, self._location)
        elif type(location) == str and the_model.get_waypoint_location(location):
            self._location = the_model.get_waypoint_location(location)
            print("%s %s moved to location " % (str(self.get_class_name()), self._name.capitalize()), self._location)
            the_model.notify_location(self._name, self._location)


#===============================================================================
class Robot(Traveler):
    def __str__(self):
        return "Robot " + super().__str__()


#==============================================================================
class Fire(SimObject):
    def __str__(self):
        return "Fire " + super().__str__()


#===============================================================================
class Human(Traveler):
    '''
    A human in the simulation.
    '''

    def __str__(self):
        return "Human " +super().__str__()








