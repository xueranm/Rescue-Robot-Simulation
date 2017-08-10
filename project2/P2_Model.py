#===============================================================================
# P2_Model.py
# Created by Anthony Hornof - 4-8-2016
# Modified by < Xueran Ma > - < 4-24-2016 >
# Version 0.2
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
        #Initialize the attributes
        self.__world_size = None
        self.__humans = []


    #===========================================================================
    def __str__(self):
        #The describe of world size
        result =  "The world is of size "+ str(self.__world_size)
        #For human objects, add the describe of each human to result
        if self.__humans != []:
            for human in self.__humans:
                result += '\n' + human.__str__()
        return result




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
        #arg1 is tuple, arg2=None
        if arg1 != None and arg2 == None:
            # check if the first one is a 2-digit tuple
            if isinstance(arg1, tuple) and len(arg1) == 2:
                #check if the things in tuple are int
                if isinstance(arg1[0], int) and isinstance(arg1[1], int):
                    #check if the location is inside the world
                    if arg1[0] >=0 and arg1[0]<= self.__world_size() and arg1[1]>=0 and arg1[1] <= self.__world_size:
                        return (arg1[0], arg1[1])

                elif isinstance(arg1[0], str) and isinstance(arg1[1], str):
                    #check if the str includes digits
                    if arg1[0].isdigit() and arg1[1].isdigit():
                        #check if the location is inside the world
                        if arg1[0] >= 0 and arg1[0] <= self.__world_size and arg1[1] >= 0 and arg1[1] <= self.__world_size:
                            return (int(arg1[0]), int(arg1[1]))
        #another situation: arg1 and arg2 are a str or int
        elif arg1 != None and arg2 != None:
            #differ the 2 situation: both are str or both are int
            if isinstance(arg1, int) and isinstance(arg2, int):
                #check if location is inside the world
                if arg1 >= 0 and arg1 <= self.__world_size and arg2 >= 0 and arg2 <= self.__world_size:
                    return (int(arg1), int(arg2))
            elif isinstance(arg1, str) and isinstance(arg2, str):
                #check if the str includes digits
                if arg1.isdigit() and arg2.isdigit():
                    #check if location is inside the world
                    if int(arg1) >= 0 and int(arg1) <= self.__world_size and int(arg2) >= 0 and int(arg2) <= self.__world_size:
                        return (int(arg1), int(arg2))
        #others are errors and report and return it
        print("Error: Invalid location.")
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
        #change the name of arg_list just for convenience
        line = arg_list
        command = ['world','human']
        #check the format of the 'create' command
        if line[0] in command:
            # 'create world' command
            #the length should be 2
            if len(line) == 2 and line[0] == 'world':
                #the world should have not extisted
                if self.__world_size == None:
                    #world size should be a digit
                    if line[1].isdigit():
                        #the range of world size and report it
                        if int(line[1])>= MIN_WORLD_SIZE and int(line[1])<= MAX_WORLD_SIZE:
                            #assign it to __world_size
                            self.__world_size = int(line[1])
                            print("Creating world of size %d"%int(line[1]))
                        else:
                            print("Error: World size is out of range.")
                            return True
                    else:
                        print("Unrecognized command:", line)
                        return True
                else:
                    print("Error: World already exists.")
                    return True
            #'create human' command
            elif len(line) == 4 and line[0] == 'human':
                # before a human is created there must be a world created, otherwise report error
                if self.__world_size != None:
                    #human name must have only digits or letters, otherwise report error
                    if line[1].isalnum():
                        #check if the name has extisted before, otherwise report error
                        if self.get_human(line[1]) == None:
                            #check if the location is valid, otherwise report it in get_valid_location function
                            if self.get_valid_location(line[2],line[3]) != None:
                                #all are cleared and add the human to __humans list and report it
                                self.__humans.append(Human(line[1],self.get_valid_location(line[2],line[3])))
                                print("Creating human %s at location "%line[1], self.get_valid_location(line[2],line[3]) )
                        else:
                            print("Error: Human already exists with that name.")
                            return True


                    else:
                        print("Error: Name must be alphanumeric.")
                        return True
                else:
                    print("Error: A world must be created before any other objects.")
            else:
                print('Unrecognized command: %s'% line)
                return True
        else:
            print('Unrecognized command: %s' % line)
            return True
        return False






    #===========================================================================
    def get_human(self, name):
        '''
        # Takes a name string.  Looks for a human with that name.  If one exists,
        #   returns that human.  If one does not, returns None.

        Parameters: name, a string
        Returns:    Either a pointer to a human object, or None
        '''
        #check if the name existed in the humans list before
        for person in self.__humans:
            #call get_name from human class to get the name in humans list
            if name == person.get_name():
                #if the name existed, return the pointer
                return person
        # the name didn't exist in humans list
        return None


    #===========================================================================
    def describe_all(self):
        '''
        Each of the simulation objects describes itself in text.
        ( ) -> None
        '''
        #when stutas, call the describe_all function
        result = ('The contents of the world are as follows: ')
        print(result)
        #when world is created, print the information of it
        if self.__world_size != None:
            print(self.__str__())



#===============================================================================
class Human:
    '''
    A human in the simulation.
    '''
    #initialize the human's name and location
    def __init__(self, name, location):
        self.__name = name.lower()
        self.__location = location

    #str will be called in Model class's str, shows on the status command
    def __str__(self):
        return ("Human %s at location" % self.__name + str(self.__location))

    # get the name of the human
    def get_name(self):
        return self.__name

    # change the location of the human
    def move_to(self, location):
        self.__location = location
        return self.__location


