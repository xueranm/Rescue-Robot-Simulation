#===============================================================================
# P2_Controller.py
# Created by Anthony Hornof - 4-8-2016
# Modified by < Xueran Ma > - < 4-24-2016 >
# Version 0.2
# Implementation for Spring 2016 CIS 211 Project 2
# Derived in part from Dave Kieras' design and implementation of EECS 381 Proj 4
#===============================================================================

import sys  # for argv
import os   # for os.path.isfile() and os.access()

import P2_Model
#===============================================================================
def main ():
#===============================================================================
# Create a global Model object and assign it to a global variable called "the_model"
# Create a local instance of a Controller and have it start the run() function.

    global the_model
    the_model = P2_Model.Model()
    con = Controller()
    con.run()

#===============================================================================
class Controller:
#===============================================================================
    '''
    The controller object handles user keyboard input and provides textual to
    the console.  It follows the model view-controller software design pattern.
    '''

    #===========================================================================
    def __init__(self):
        #intialize the 3 attributes
        self.__input_filename = 'command.txt'
        self.__input_file_object = None
        self.__current_input_mode = None
    #===========================================================================
    def run(self):
    #===========================================================================
        '''
        () -> None.
        Process the command lines for the human-robot simulation.
        '''

        print("Starting Human-Robot Interaction Simulation.")

        # Attempt to open an input file for an initial set of commands
        self.open_initial_input_file()

        #=======================================================================
        # Command loop
        while True:

            # Get the next line of input whether it is from the user or a file.
            line = self.get_next_input_line()
            line_list = line.lower().split()
            #create command
            if line_list[0] == 'create':
                #create a list without 'create'
                line_list = line_list[1:]
                #call the create_sim_object from model class to implement the command
                the_model.create_sim_object(line_list)


            #status command
            elif line_list[0] == 'status' and len(line_list) == 1:
                the_model.describe_all()

            #quit command
            elif line_list[0] == 'quit' and len(line_list) == 1:
                print('Are you sure you want to quit? (Y/N): ', end = '')
                #read the next line to make sure to quit
                line = self.get_next_input_line()
                if line.upper() == 'Y':
                    break

            #move command
            #firstly, check the name didn't exist before
            elif the_model.get_human(line_list[0]) != None:
                #secondly, check if the command use the key word "move" as the second word
                if line_list[1] == 'move':
                    #implement the move command
                    self.do_human_command(line_list)
                else:
                    print("Error: Invalid human command.")
            else:
                print('Unrecognized command: ',line)
        return None


    #===========================================================================
    # Manage the command line input file
    #===========================================================================

    def get_next_input_line(self):
        '''
        ( ) -> string
        • Displays the prompt.
        • Returns the next line to be processed, or '' if there is no line.
        • Gets the next line of text either from an input file or from the user,
          depending on the current setting of current_input_mode.
        • When reading from an input file, and either a blank line or an end of file
          is encountered, close the input file and set the file object var to None.
        '''

        #check the mode is file or user
        if self.__current_input_mode == 'file':
            #there is a file to read and read one line from the file
            print("File>", end ='')
            content = self.__input_file_object.readline().strip()

            #check if the file gets to its end
            if content == None or content == '':

                self.__input_file_object = None
                self.__input_file_object.close()
                print("Closing file.")
                return ""

            else:
                print(content)
                return content

        else:
            print('>', end = '')
            command = input()
            return command

    #===========================================================================
    def open_initial_input_file (self):
        '''
        Attempt to open a file for an initial set of commands.
        ( ) -> None
        If a filename was entered as a command line argument, overwrite the
          controller's member variable with that new filename.
        '''
        #check if there is one more argument in command line
        #just one argument, implement the default file and check if it existe
        if len(sys.argv) == 1 and os.path.isfile(self.__input_filename):
            #it existes, check if it can be opened
            if os.access(self.__input_filename, os.R_OK):
                #open it
                self.open_input_file()
                print('Reading file:',self.__input_filename)
                self.__current_input_mode = 'file'
            else:
                print("Error: Could not open and read input file:", self.__input_filename)
        #there are 2 or more arguments
        elif len(sys.argv) >1:
            #change the input_file_name
            self.__input_filename = sys.argv[1]
            #check if it is a file
            if os.path.isfile(self.__input_filename):
                #check if it can be opened
                if os.access(self.__input_filename, os.R_OK):
                    self.open_input_file()
                    print('Reading file:',self.__input_filename)
                    #change the input_mode to 'file'
                    self.__current_input_mode = 'file'
                else:
                    print("Error: Could not open and read input file:", self.__input_filename)
            else:
                self.__current_input_mode = 'user'

        else:
            self.__current_input_mode = 'user'
        return None

    #===========================================================================
    def open_input_file (self):
        '''
        ( ) -> None
        Attempts to open the filename in the input file member variable to
          execute a set of commands.
        '''
        #open the file and get the object
        self.__input_file_object = open(self.__input_filename)
        return None

    #===========================================================================
    # Execute commands
    #===========================================================================

    def do_human_command(self, args):
        '''
        Parameters: args, a list of arguments that is already confirmed to be
                          nonempty with the first argument a human in the model.
        Returns:    None (All errors are reported within, so no need to return
                          an error flag.)

        Processes the remainder of the arguments to insure that they at least
        represent valid locations on the map.  If they are valid,
        call the appropriate function calls in the model to build them.
        '''
        #check the length is right
        if len(args) == 4:
            #check the location is in the world
            if the_model.get_valid_location(args[2],args[3]) != None:
                #get the location tuple
                global location
                location = the_model.get_valid_location(args[2],args[3])
                #change  the human's location in the model
                new = the_model.get_human(args[0]).move_to(location)
                print("Human %s moved to location "%args[0],new)
        else:
            print("Error: Invalid move command.")





#===============================================================================
main ()
#===============================================================================

