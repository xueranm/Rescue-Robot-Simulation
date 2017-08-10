#===============================================================================
# P4_Model.py
# Created by Anthony Hornof - 4-28-2016
# Modified by < Xueran Ma > - < 5/23/2016 >
# Version 0.2
# Credit: P4 is from the implementation for Spring 2016 CIS 211 Project 3
# Derived in part from Dave Kieras' design and implementation of EECS 381 Proj 4
#===============================================================================

# import P3_View
from P4_Utility import *

# global constants. (You must define them as global if you intend to re-assign.)
WORLD_STRING = 'world'
WAYPOINT_STRING = 'waypoint'
HUMAN_STRING = 'human'
ROBOT_STRING = 'robot'
FIRE_STRING = 'fire'


class Model:
    '''
    The Model object keeps track of everything in the simulated world.
    Only one Model should be created in each run of the simulation.
    '''

    #===========================================================================
    # Initializer and other Special Functions
    #===========================================================================
    def __init__(self):
        self.__world_size = None
        self.__sim_objects = []  # all SimObjects but the Waypoints
        self.__waypoints = []
        self.__humans = []
        self.__robots = []
        self.__fires = []
        #Add a pseudo-private member variable that
        # maintains an integer representation of the current simulated time. Initialize to 0.
        self._time = 0

        global the_model
        the_model = self

        # A pointer to the view in the MVC design. If there were
        # more than one view, this would be a list of all views.
        self.__view = None

    #===========================================================================
    def describe_all(self):
        '''
        Each of the simulation objects describes itself in text.
        ( ) -> None
        '''
        print("The contents of the world are as follows:")
        if self.__world_size:
            print ("The world is of size ", self.__world_size, ".", sep='')
        for i in self.__waypoints:
            print (i)
        for i in self.__humans:
            print (i)
        for i in self.__robots:
            print (i)
        for i in self.__fires:
            print (i)

    #===========================================================================
    # Model-View-Controller coordination methods
    #===========================================================================
    def attach_view(self, v):
        self.__view = v

    #===========================================================================
    def notify_location(self, name, location):
        '''
        The model has been notified, probably by a SimObject, that a SimObject's
        location may have changed.  Broadcast this information to the View.
        '''
        self.__view.update_object(name, location)


    #===========================================================================
    # Creation Methods
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

        MIN_WORLD_SIZE = 5
        MAX_WORLD_SIZE = 30

        # Continue here checking for all of the different objects that "create"
        # could be called to build.  For each, after checking for the string
        # that appeared after "create", make sure that any additional arguments
        # on the line are all permissable given the project specification.


        #=======================================================================
        # World
        if arg_list[0] == WORLD_STRING:
            # Else return error.

            # Verify that there is one additional argument and it is an integer.
            if len(arg_list) == 2 and arg_list[1].isdigit():
                size = int(arg_list[1])
            else:
                raise BadLineError()
                return True

            # If a world has aleady been created
            if (self.__world_size):
                # Then return an error.
                raise BadMsgError("Error: World already exists.")
                return False
                # raise the error

            # Verify size is in range.
            if size < MIN_WORLD_SIZE or size > MAX_WORLD_SIZE:
                raise BadMsgError("Error: World size is out of range.")
                return False
            else:
                # Else create world, and notify all views that the world is
                #   being created."

                print('Creating world of size ', size, '.', sep='')
                # Set the World size member variable.
                self.__world_size = size

                # Update the View object(s) world size.
                self.__view.create(size)

        #=======================================================================
        # Make sure a world exists.
        # If there is no world yet, then there can be no waypoints.
        elif not self.__world_size:
            raise BadMsgError("Error: A world must be created before any other objects.")
            return False
            # Raise the error

        #=======================================================================
        # Waypoint, human, robot, or fire
        # Verify the number and type of arguments, and location.
        elif arg_list[0] in (WAYPOINT_STRING, HUMAN_STRING, ROBOT_STRING, FIRE_STRING):

            # Verify that there are two arguments, two integers each of which
            #   is <= world_size.

            # If there are NOT three more arguments, the second and third being ints...
            if not (len(arg_list) == 4 and arg_list[2].isdigit() and
                        arg_list[3].isdigit()):
                # Then return error flag.
                raise BadLineError()
                return True

            # Convert the two integer arguments into a tuple of integers.
            location = (int(arg_list[2]), int(arg_list[3]))

            # Get the name for all subsequent operations. Store all names as lowercase.
            name = arg_list[1].lower()

            #===================================================================
            # Waypoint

            if arg_list[0] == WAYPOINT_STRING:

                # If the waypoint name is not a single letter
                if not name.isalpha() or not len(name) == 1:
                    raise BadMsgError('Error: Waypoint names must be single letters.')
                    return False


                # If a waypoint already exists with that name or at that location, report error.
                for w in self.__waypoints:
                    if name == w.get_name() or location == w.get_location():
                        raise BadMsgError("Error: Waypoint {} already exists at location {}.".format(w.get_name().upper(), w.get_location()))
                        return True# Error was reported.

                # Okay, there is NO Waypoint at that location.
                else:

                    # If the location is invalid, return an error.
                    if not the_model.get_valid_location(location):
                        raise BadMsgError("Error: Invalid location.")
                        return False


                    else:
                        # Create the waypoint! All of the parameters checked out.
                        print("Creating waypoint", name.upper(), "at location", location)
                        # Create the new waypoint, and add it to the list of Waypoints
                        self.__waypoints.append( Waypoint(name, location) )
                        # Update the view with the new waypoint
                        self.__view.add_landmark(name, location)


            #=======================================================================
            # Human, Robot, or Fire
            elif arg_list[0] in (HUMAN_STRING, ROBOT_STRING, FIRE_STRING):

                # If the name is not alphanumeric
                if not arg_list[1].isalnum():
                    raise BadMsgError("Error: Name must be alphanumeric.")

                # If an object already exists with that name.
                if self.get_object(arg_list[1]):

                    # Get a nice pritable class name using __class__.__name__
                    raise BadMsgError("Error: {} already exists with that name.".format(self.get_object(arg_list[1]).get_class_name()))


                # If the location is invalid, return an error.
                if not the_model.get_valid_location(location):
                    raise BadMsgError("Error: Invalid location.")


                # If we got this far, it seems to be a valid input,  so
                #   create an object at the location.
                location = self.get_valid_location(arg_list[2], arg_list[3])
                name = arg_list[1]
                print("Creating ", arg_list[0]," ", name.capitalize(), " at location ", location,".", sep='')

                # For each type of sim object, create the object and add it to its list.
                if arg_list[0] == HUMAN_STRING:
                    # Create the Human
                    new_sim_obj = Human(name, location)
                    # Add the human to the list of Humans.
                    self.__humans.append(new_sim_obj)
                elif arg_list[0] == ROBOT_STRING:
                    # Create the Robot
                    new_sim_obj = Robot(name, location)
                    # Add the robot to the list of SimObjects.
                    self.__robots.append(new_sim_obj)
                else: # arg_list[0] == FIRE_STRING:
                    # Create the Robot
                    new_sim_obj = Fire(name, location)
                    # Add the robot to the list of SimObjects.
                    self.__fires.append(new_sim_obj)

                # Also add the new sim object to the list of all SimObjects as well.
                self.__sim_objects.append(new_sim_obj)

                # Update the view with the new Sim Object
                self.__view.update_object(name, location)

            else:
                raise BadLineError() # Error

        else:
            raise BadLineError() # Error

    #===========================================================================
    # More Complex Accessor Methods
    #===========================================================================
    def get_time(self):
        '''A “getter” for the time variable. Returns an int.'''
        return int(self._time)
    #===========================================================================
    def fire_at_location(self, location):
        '''Returns a Fire object at that location if one exists. Otherwise returns None. '''
        for fire in self.__fires:
            if fire.get_location() == location:
                return fire
        else:
            return None

    #===========================================================================
    def get_waypoint_location(self, name):
        '''
        # Takes a name string.  Looks for a waypoint with that name.  If one exists,
        #   returns its location.  If one does not, returns None.

        Parameters: name, a string
        Returns:    Either a location of a Waypoint, or False
        '''

        for i in self.__waypoints:
            if i.get_name() == name:
                return i.get_location()
        else:
            return None

    #===========================================================================
    def get_human(self, name):
        '''
        Takes a name string.  Looks for a human with that name.  If one exists,
            returns that human.  If one does not, returns None.
        '''
        for i in self.__humans:
            if i.get_name() == name:
                return i
        else:
            return None
    #===========================================================================
    def get_fire(self, name):
        for i in self.__fires:
            if i.get_name() == name:
                return i
        else:
            return False




    #===========================================================================
    def get_robot(self, name):
        '''
        Takes a name string.  Looks for a robot with that name.  If one exists,
            returns that robot.  If one does not, returns None.
        '''
        for i in self.__robots:
            if i.get_name() == name:
                return i
        else:
            return False

    #===========================================================================
    def get_object(self, name):
        '''
        Takes a name string.  Looks for any sim object with that name.  If one
            exists, returns that sim object.  If one does not, returns None.
        '''
        for i in self.__sim_objects:
            if i.get_name() == name:
                return i
        else:
            return False
    #===========================================================================
    def delete_fire(self, name):
        '''Delete from the Model and the View a fire with the passed-in name.'''
        for robot in self.__robots:
            robot.stop_fighting_fire(self.get_fire(name))
        self.__fires.remove(self.get_fire(name))
        self.__view.update_object(name)
    #===========================================================================
    def update(self):
        '''Update all simulation objects in the order in which they were created. Advance time by a minute.'''
        for object in self.__sim_objects:
            object.update()
        self._time += 1

    #===========================================================================
    def get_valid_location(self, arg1, arg2=None):
        # Possibly change to get_location() and have it always return a tuple of
        # two ints
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
            return None # The provided arguments are not handled.

        # If the location is in the world, return True.
        if (x >= 0 and y >= 0 and
                x <= self.__world_size and y <= self.__world_size):
            return (x, y)
        else:
            return None


#===============================================================================
# OTHER CLASSES
#===============================================================================

#===============================================================================
class SimObject:

    def __init__(self, name, location):
        # Private member variables.
        self._name = name.lower()
        self._location = location  # a tuple of integers

    def __str__(self):
        return self._name.capitalize() + " at location " + str(self._location)

    def get_name(self):
        return self._name

    def get_class_name(self):
        ''' Returns 'Human', 'Robot', or 'Fire' as appropriate.'''
        return self.__class__.__name__

    def get_location(self):
        return self._location

#===============================================================================
class Waypoint (SimObject):
    '''
    A Waypoint in the simulation.
    '''

    def __str__(self):
        return "Waypoint " + super().__str__()

#===============================================================================
class Fire (SimObject):
    '''
    A Waypoint in the simulation.
    '''

    def __init__(self, name, location):
        # Private member variables.
        self._strength = 5
        super().__init__(name, location)

    def __str__(self):
        return "Fire " + super().__str__() +" of strength {}".format(self.get_strength())

    def update(self):
        pass

    def get_strength(self):
        return self._strength

    def __del__(self):
        '''Outputs to the console “Fire <name> has disappeared from the simulation.” <name> is the fire name.'''
        print("Fire {} has disappeared from the simulation.".format(self._name.capitalize()))

    def reduce_strength(self):
        '''
        Decrement _strength by 1.
        If _strength reaches 0, remove fire from the simulation, both from the model and the view.
        '''
        self._strength -= 1
        if self._strength == 0:
            the_model.delete_fire(self._name)




#===============================================================================
class Traveler (SimObject):

    def __init__(self, name, location):
        '''
        _destination_list - a list of locations discussed below in move_to( ).
        _moving - Boolean. Indicates whether the traveler is currently moving. The traveler’s “moving status”.
        '''
        self._destination_list = []
        self._moving = False
        super().__init__(name, location)

        # Update the view

    def set_moving(self):
        ''' Sets the Traveler object’s status to moving.'''
        self._moving = True

    def journey_to(self, destination_list):
        '''check for the destination_list and set traveler to move.'''
        #change the str list into a tuple list
        new_destination_list = []
        for item in destination_list:
            if item.isalpha():
                new_destination_list.append(the_model.get_waypoint_location(item))
            elif ',' in item:
                index = item.find(',')
                left = item[:index]
                right = item[index+1:]
                new_destination_list.append((int(left),int(right)))
            else:
                raise BadMsgError("Error: '{}' is not an valid location for this 'move'.".format(item))
        #check if they are valid in the world
        for t in range(len(new_destination_list)):
            if the_model.get_valid_location(new_destination_list[t]) == None:
                raise BadMsgError("Error: '{}' is not an valid location for this 'move'.".format(destination_list[t]))
        #check if this traveler can move from its current location directly or from the previous location
        # in destination_list to this new location with a horizontal or vertical movement.
        for i in range(len(new_destination_list)):
            #for the first location in destination_list
            if i == 0:
                if not (self._location[0]== new_destination_list[i][0] or self._location[1]==new_destination_list[i][1]):
                    raise BadMsgError("Error: '{}' is not an valid location for this 'move'.".format(destination_list[i]))
            else:
                if not (new_destination_list[i-1][0] == new_destination_list[i][0] or new_destination_list[i-1][1] == new_destination_list[i][1]):
                    raise BadMsgError("Error: '{}' is not an valid location for this 'move'.".format(destination_list[i]))
        self._destination_list= new_destination_list





    def get_next_moving_location(self):
        '''
        If the traveler is currently moving, this function returns the location (as a tuple of two integers) that
        the traveler would move to if it were to move one grid unit closer to the next location in its destination list.
        '''
        if self._moving == True:
            if self._destination_list[0][0] == self._location[0]:
                if self._destination_list[0][1] > self._location[1]:
                    return (int(self._location[0]),int(self._location[1])+1)
                else:
                    return (int(self._location[0]),int(self._location[1])-1)
            elif self._destination_list[0][1]== self._location[1]:
                if self._destination_list[0][0] > self._location[0]:
                    return (int(self._location[0])+1, int(self._location[1]))
                else:
                    return (int(self._location[0])-1, int(self._location[1]))




    def move_to(self, location):

        #print( self.get_class_name(), " " , self.get_name().capitalize(), " moved to location ",
        #       location, '.', sep='')

        # Change the object's location
        self._location = location
        the_model.notify_location(self._name, location) # a tuple of integers
        if self._location == self._destination_list[0]:
            self._destination_list.remove(self._destination_list[0])

        if len(self._destination_list)==0:
            self._moving = False
            print("{} {} arrived at location {}.".format(self.get_class_name(),self.get_name().capitalize(),location))


        # Notify the Model that an object of this name now has this location.


    def stop(self):
        '''If the object is moving, stop it.'''
        self._moving = False



#===============================================================================
class Human (Traveler):
    '''
    A human in the simulation.
    '''

    def __str__(self):
        if self._moving == False:
            return "Human " + super().__str__()
        else:
            new_str = "{}".format(self._destination_list[0])
            for i in range(1,len(self._destination_list),1):
                new_str = new_str +  ', ' + str(self._destination_list[i])
            return "Human " + super().__str__()+ " moving to {}".format(new_str)

    def update(self):
        '''
        If the object’s moving status is True, use superclass and Model methods to determine
        if the human is about to step into a location with a fire.
        If not, move the human to that location using a superclass method.
        If yes, change the human’s status to stopped and output the following message to the console:
        “<human> stopping short of fire <fire>.” in which <human> is the name of the human and <fire> is the name of the fire.
        '''
        if self._moving == True:
            if the_model.fire_at_location(self.get_next_moving_location()) != None:
                self._moving = False
                print("{} stopping short of fire {}.".format(self.get_name(),the_model.fire_at_location(self.get_next_moving_location())))
            else:
                self.move_to(self.get_next_moving_location())



#===============================================================================
class Robot (Traveler):
    '''
    A robot in the simulation.
    '''
    def __init__(self, name, location):
        # Private member variables.
        self._extinguishing_fire = None
        #Points either to None or to a fire object that the robot is currently extinguishing.
        super().__init__(name, location)

    def fight_fire(self,fire_object):
        '''Set up the robot to extinguish the fire_object.'''
        self._extinguishing_fire = fire_object
        print(self)

    def __str__(self):
        if self._moving == False and self._extinguishing_fire == None:
            return "Robot " + super().__str__()
        elif self._extinguishing_fire != None:
            return "Robot " + super().__str__() + " extinguishing fire {}".format(self._extinguishing_fire.get_name().capitalize())
        else:
            new_str = "{}".format(self._destination_list[0])
            for i in range(1, len(self._destination_list), 1):
                new_str = new_str + ', ' + str(self._destination_list[i])
            return "Robot " + super().__str__() + " moving to {}".format(new_str)
    def stop_fighting_fire(self,fire_object):
        '''If the Robot is currently fighting this fire, stop fighting it. Else do nothing.'''
        if self._extinguishing_fire == fire_object:
            self._extinguishing_fire = None

    def set_moving(self):
        self._extinguishing_fire = None
        super().set_moving()
    def update(self):
        '''
        If the robot is moving, move the robot one grid unit.
        If it is extinguishing a fire, reduce that fire object’s “fire strength” by one unit.
        '''

        if self._extinguishing_fire != None:
            self._extinguishing_fire.reduce_strength()
            self._moving = False
        elif self._moving == True:
            self.move_to(self.get_next_moving_location())


