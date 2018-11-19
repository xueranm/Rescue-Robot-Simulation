# Rescue Robot Simulation
Project 1 - Load a Rescue Robot Simulation File (This one is too easy so I do not post it.)

Project 2 - An Object-Based Model-View-Controller World

Project 3 - Expand the Simulation with a Class Hierarchy

Project 4 - Add Time and Object Interaction to the Simulation

The course is structured around a number of important programming concepts, as follows: Problem decomposition, structured programming, files manipulation, exceptions, inheritance, object-oriented programming, namespaces and scope, testing and debugging, and possibly event-driven programming and graphical-user interface programming. 

Model data: World, Human, Waypoint, Robot, Fire Flames (with strength level)
Action command: create, show (show view), status (print the data and their position), go (execute the commands one step above and time goes), move, (robot) attack (fire)

Two example ouput file of project 4:

File 1:
( Show how do the basic orders and make robot/human move:)







File 2:
(show one more function that robot extinguish fire)
Starting Human-Robot Interaction Simulation
Reading file: P4_Sample_Input_File_5.txt
Time 0 FILE> create world 5
Creating world of size 5
Time 0 FILE> create robot T1 0 5
Creating robot T1 at location (0, 5)
Time 0 FILE> create robot T2 4 5
Creating robot T2 at location (4, 5)
Time 0 FILE> create fire Inferno 2 5
Creating fire Inferno at location (2, 5)
Time 0 FILE> create waypoint B 2 5
Creating waypoint B at location (2, 5)
Time 0 FILE> status
The contents of the world are as follows:
The world is of size 5
Waypoint B at location (2, 5)
Robot T1 at location (0, 5)
Robot T2 at location (4, 5)
Fire Inferno at location (2, 5) of strength 5
Time 0 FILE> show
05  .T  .   BI  .   .T  .  
    .   .   .   .   .   .  
    .   .   .   .   .   .  
    .   .   .   .   .   .  
    .   .   .   .   .   .  
00  .   .   .   .   .   .  
    00                  05
Time 0 FILE> t1 move B
Robot T1 at location (0, 5) moving to (2, 5)
Time 0 FILE> t2 move B
Robot T2 at location (4, 5) moving to (2, 5)
Time 0 FILE> go
Time 1 FILE> show
05  .   .T  BI  .T  .   .  
    .   .   .   .   .   .  
    .   .   .   .   .   .  
    .   .   .   .   .   .  
    .   .   .   .   .   .  
00  .   .   .   .   .   .  
    00                  05
Time 1 FILE> go
Robot T1 arrived at location (2, 5)
Robot T2 arrived at location (2, 5)
Time 2 FILE> show
05  .   .   B*  .   .   .  
    .   .   .   .   .   .  
    .   .   .   .   .   .  
    .   .   .   .   .   .  
    .   .   .   .   .   .  
00  .   .   .   .   .   .  
    00                  05
Time 2 FILE> t2 attack Inferno
Robot T2 at location (2, 5) extinguishing fire Inferno
Time 2 FILE> t1 attack Inferno
Robot T1 at location (2, 5) extinguishing fire Inferno
Time 2 FILE> go
Time 3 FILE> show
05  .   .   B*  .   .   .  
    .   .   .   .   .   .  
    .   .   .   .   .   .  
    .   .   .   .   .   .  
    .   .   .   .   .   .  
00  .   .   .   .   .   .  
    00                  05
Time 3 FILE> go
Time 4 FILE> show
05  .   .   B*  .   .   .  
    .   .   .   .   .   .  
    .   .   .   .   .   .  
    .   .   .   .   .   .  
    .   .   .   .   .   .  
00  .   .   .   .   .   .  
    00                  05
Time 4 FILE> go
Fire Inferno has disappeared from the simulation
Time 5 FILE> show
05  .   .   B*  .   .   .  
    .   .   .   .   .   .  
    .   .   .   .   .   .  
    .   .   .   .   .   .  
    .   .   .   .   .   .  
00  .   .   .   .   .   .  
    00                  05
Time 5 FILE> status
The contents of the world are as follows:
The world is of size 5
Waypoint B at location (2, 5)
Robot T1 at location (2, 5)
Robot T2 at location (2, 5)
Time 5 FILE> quit
Are you sure you want to quit? (Y/N) Time 5 FILE> y

