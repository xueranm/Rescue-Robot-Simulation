#===============================================================================
# P4_View.py
# Created by Anthony Hornof - 4-28-2016
# Modified by < Xueran Ma > - < 5/23/2016 >
# Version 0.2
# Credit: P4 is from the implementation for Spring 2016 CIS 211 Project 3
# Derived in part from Dave Kieras' design and implementation of EECS 381 Proj 4
#===============================================================================
from P4_Utility import *
class View:
    '''
    The View object presents a way to see the simulated world.
    '''

    #===========================================================================
    def __init__(self):

        # A list of all of the humans, robots, and fires in the plot.
        # self.objects_in_plot = []

        # Initialize view_size to None
        self.__view_size = None

        # The map grid cells.
        self.__cells = []       # 2D list of the mapCells at each map location
        self.__num_rows = 0
        self.__num_cols = 0

        # A dictionary of all non-landmark objects.
        self.__objects = {}

        # A list of all landmark objects.
        self.__landmarks = {}

    #===========================================================================
    def create(self, world_size):
    # view_size is set to world_size when the world is created, but in theory
    #   could be other sizes, and just show portions of the world.

        self.__view_size = world_size   # The size of the map grid.

        # Note that the map is actually size+1
        self.__num_rows = self.__num_cols = world_size + 1

        # 2D list of of the text contents of each map location. Fill the map.
        # Fill the grid, row by row
        for i in range(self.__num_rows):
            # Insert a list that will be row i.  Initialize as a list.
            self.__cells.append([])
            for j in range(self.__num_cols):
                # Append a list
                self.__cells[i].append([])

        # Fill each grid location with a two-characters string.
        self.__clear_grid()


    #===========================================================================
    def update_object(self, name, location=None):
        '''
        Keeps a dictionary of all of the non-landmark objects in the simulation.
        (name, location) -> None
        arguments: name, a lowercase string name of a map object
                    location, a tuple of two ints of a map location
        For example: {'joe':(0, 0), 'junling':(1, 1)}
        '''
        # Find the object with 'name' and update its 'location'.
        # If the name is not in the list, add it with 'location'.
        # Update the method so that the object is removed from the view if location is None.
        if location != None:
            self.__objects.update({name:location})
        else:
            del self.__objects[name]




    #===========================================================================
    def add_landmark(self, name, location):
        '''
        Same as update_object( ) except dictionary is like {'a':(0, 0), 'b':(1, 1)}
        Adds landmark of name 'letter' at location 'location
        (The only landmarks in this particular project are the waypoints.)
        '''

        self.__landmarks.update({name:location})


    #===========================================================================
    def draw(self):
        '''
        Draw all __cells.  Each cell is ' .  ', or ' WO ' with a possible
            Waypoint and Object.
        '''

        # If the world (and thus view) has no size, return an error
        if not self.__view_size:
            raise BadMsgError("Error: Cannot 'show' the world until it has a size.")

        # If no arguments, show everything
        else:
            # Clear the grid.
            self.__clear_grid( )

            # Fill the grid starting with the

            # Add the landmarks
            # Get the name and location of each landmark.
            for name, location in self.__landmarks.items():
                # Get the current four-char string contents of the location.
                contents = self.__cells[location[0]][location[1]]
                # Change the second character to the landmark name
                contents = contents[0] + name[0].capitalize() + '  '
                # Put the contents back into the location
                self.__cells[location[0]][location[1]] = contents


            # Add the mutable simulation objects
            # Get the name and location of each object.
            for name, location in self.__objects.items():
                # Get the current four-char string contents of the location.
                contents = self.__cells[location[0]][location[1]]

                # If the current third position is ' '
                if contents[2] == ' ':
                    # Change the third character to the name
                    contents = ' ' + contents[1] + name[0].capitalize() + ' '
                else:
                    # Else there are multiple items at this location.
                    contents = ' ' + contents[1] + '* '

                # Put the contents back into the location
                self.__cells[location[0]][location[1]] = contents

            self.__draw_grid( )


    #===========================================================================
    def __clear_grid(self):

        # Clear the map grid, row by row
        for j in range(self.__num_rows):
            # Step through row i.
            for i in range(self.__num_cols):
                # Clear the string at location i, j.
                self.__cells[i][j] = ' .  '


    #===============================================================================
    # Display the map in the console.
    def __draw_grid(self):

        # Draw the grid
        j = self.__num_rows - 1

        # Print each row. Start with the top row and go down to 0.
        while j >= 0:
            # row_list = self.__cells[i]

            # Assemble a string for the row.
            row_string = ''

            # Show the legend on the y-axis
            if j % 5 == 0:
                row_string = '%02d' % j + ' '
            else:
                row_string = '   '

            # Add each cell in the row.
            for i in range(self.__num_cols):
                row_string += self.__cells[i][j]

            print(row_string) # Print the line.
            j -= 1  # Iterate.

        # Print the last row, the x-axis legend.
        row_string = '  '
        for i in range(self.__num_cols):
            if i % 5 == 0:
                row_string += '  %02d' % i
            else:
                row_string += '    '
        print(row_string) # Print the line.

