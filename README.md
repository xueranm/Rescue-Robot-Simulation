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
Starting Human-Robot Interaction Simulation
Reading file: P4_Sample_Input_File_6.txt
Time 0 FILE> create world 6
Creating world of size 6
Time 0 FILE> create waypoint D 0 6
Creating waypoint D at location (0, 6)
Time 0 FILE> create waypoint A 0 0
Creating waypoint A at location (0, 0)
Time 0 FILE> create waypoint B 6 0
Creating waypoint B at location (6, 0)
Time 0 FILE> create waypoint C 6 6
Creating waypoint C at location (6, 6)
Time 0 FILE> status
The contents of the world are as follows:
The world is of size 6
Waypoint D at location (0, 6)
Waypoint A at location (0, 0)
Waypoint B at location (6, 0)
Waypoint C at location (6, 6)
Time 0 FILE> show
    D   .   .   .   .   .   C  
05  .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
00  A   .   .   .   .   .   B  
    00                  05    
Time 0 FILE> create Robot R1 3 0
Creating robot R1 at location (3, 0)
Time 0 FILE> create fire Flames 2 0
Creating fire Flames at location (2, 0)
Time 0 FILE> create human H1 4 0
Creating human H1 at location (4, 0)
Time 0 FILE> r1 move b c d a b
Robot R1 at location (3, 0) moving to (6, 0), (6, 6), (0, 6), (0, 0), (6, 0)
Time 0 FILE> h1 move b c d a b
Human H1 at location (4, 0) moving to (6, 0), (6, 6), (0, 6), (0, 0), (6, 0)
Time 0 FILE> go
Time 1 FILE> show
    D   .   .   .   .   .   C  
05  .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
00  A   .   .F  .   .R  .H  B  
    00                  05    
Time 1 FILE> status
The contents of the world are as follows:
The world is of size 6
Waypoint D at location (0, 6)
Waypoint A at location (0, 0)
Waypoint B at location (6, 0)
Waypoint C at location (6, 6)
Human H1 at location (5, 0) moving to (6, 0), (6, 6), (0, 6), (0, 0), (6, 0)
Robot R1 at location (4, 0) moving to (6, 0), (6, 6), (0, 6), (0, 0), (6, 0)
Fire Flames at location (2, 0) of strength 5
Time 1 FILE> go
Time 2 FILE> show
    D   .   .   .   .   .   C  
05  .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
00  A   .   .F  .   .   .R  BH 
    00                  05    
Time 2 FILE> go
Time 3 FILE> show
    D   .   .   .   .   .   C  
05  .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .H 
00  A   .   .F  .   .   .   BR 
    00                  05    
Time 3 FILE> go
Time 4 FILE> show
    D   .   .   .   .   .   C  
05  .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .H 
    .   .   .   .   .   .   .R 
00  A   .   .F  .   .   .   B  
    00                  05    
Time 4 FILE> go
Time 5 FILE> show
    D   .   .   .   .   .   C  
05  .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .H 
    .   .   .   .   .   .   .R 
    .   .   .   .   .   .   .  
00  A   .   .F  .   .   .   B  
    00                  05    
Time 5 FILE> go
Time 6 FILE> show
    D   .   .   .   .   .   C  
05  .   .   .   .   .   .   .  
    .   .   .   .   .   .   .H 
    .   .   .   .   .   .   .R 
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
00  A   .   .F  .   .   .   B  
    00                  05    
Time 6 FILE> go
Time 7 FILE> show
    D   .   .   .   .   .   C  
05  .   .   .   .   .   .   .H 
    .   .   .   .   .   .   .R 
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
00  A   .   .F  .   .   .   B  
    00                  05    
Time 7 FILE> go
Time 8 FILE> show
    D   .   .   .   .   .   CH 
05  .   .   .   .   .   .   .R 
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
00  A   .   .F  .   .   .   B  
    00                  05    
Time 8 FILE> go
Time 9 FILE> show
    D   .   .   .   .   .H  CR 
05  .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
00  A   .   .F  .   .   .   B  
    00                  05    
Time 9 FILE> go
Time 10 FILE> show
    D   .   .   .   .H  .R  C  
05  .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
00  A   .   .F  .   .   .   B  
    00                  05    
Time 10 FILE> go
Time 11 FILE> show
    D   .   .   .H  .R  .   C  
05  .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
00  A   .   .F  .   .   .   B  
    00                  05    
Time 11 FILE> go
Time 12 FILE> show
    D   .   .H  .R  .   .   C  
05  .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
00  A   .   .F  .   .   .   B  
    00                  05    
Time 12 FILE> go
Time 13 FILE> show
    D   .H  .R  .   .   .   C  
05  .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
00  A   .   .F  .   .   .   B  
    00                  05    
Time 13 FILE> go
Time 14 FILE> show
    DH  .R  .   .   .   .   C  
05  .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
00  A   .   .F  .   .   .   B  
    00                  05    
Time 14 FILE> go
Time 15 FILE> show
    DR  .   .   .   .   .   C  
05  .H  .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
00  A   .   .F  .   .   .   B  
    00                  05    
Time 15 FILE> go
Time 16 FILE> show
    D   .   .   .   .   .   C  
05  .R  .   .   .   .   .   .  
    .H  .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
00  A   .   .F  .   .   .   B  
    00                  05    
Time 16 FILE> go
Time 17 FILE> show
    D   .   .   .   .   .   C  
05  .   .   .   .   .   .   .  
    .R  .   .   .   .   .   .  
    .H  .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
00  A   .   .F  .   .   .   B  
    00                  05    
Time 17 FILE> go
Time 18 FILE> show
    D   .   .   .   .   .   C  
05  .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .R  .   .   .   .   .   .  
    .H  .   .   .   .   .   .  
    .   .   .   .   .   .   .  
00  A   .   .F  .   .   .   B  
    00                  05    
Time 18 FILE> go
Time 19 FILE> show
    D   .   .   .   .   .   C  
05  .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .R  .   .   .   .   .   .  
    .H  .   .   .   .   .   .  
00  A   .   .F  .   .   .   B  
    00                  05    
Time 19 FILE> go
Time 20 FILE> show
    D   .   .   .   .   .   C  
05  .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .R  .   .   .   .   .   .  
00  AH  .   .F  .   .   .   B  
    00                  05    
Time 20 FILE> go
Time 21 FILE> show
    D   .   .   .   .   .   C  
05  .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
00  AR  .H  .F  .   .   .   B  
    00                  05    
Time 21 FILE> go
Human H1 stopping short of fire Flames
Time 22 FILE> show
    D   .   .   .   .   .   C  
05  .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
00  A   .*  .F  .   .   .   B  
    00                  05    
Time 22 FILE> go
Time 23 FILE> show
    D   .   .   .   .   .   C  
05  .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
00  A   .H  .*  .   .   .   B  
    00                  05    
Time 23 FILE> go
Time 24 FILE> show
    D   .   .   .   .   .   C  
05  .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
00  A   .H  .F  .R  .   .   B  
    00                  05    
Time 24 FILE> go
Time 25 FILE> show
    D   .   .   .   .   .   C  
05  .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
00  A   .H  .F  .   .R  .   B  
    00                  05    
Time 25 FILE> status
The contents of the world are as follows:
The world is of size 6
Waypoint D at location (0, 6)
Waypoint A at location (0, 0)
Waypoint B at location (6, 0)
Waypoint C at location (6, 6)
Human H1 at location (1, 0)
Robot R1 at location (4, 0) moving to (6, 0)
Fire Flames at location (2, 0) of strength 5
Time 25 FILE> go
Time 26 FILE> show
    D   .   .   .   .   .   C  
05  .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
00  A   .H  .F  .   .   .R  B  
    00                  05    
Time 26 FILE> go
Robot R1 arrived at location (6, 0)
Time 27 FILE> show
    D   .   .   .   .   .   C  
05  .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
    .   .   .   .   .   .   .  
00  A   .H  .F  .   .   .   BR 
    00                  05    
Time 27 FILE> status
The contents of the world are as follows:
The world is of size 6
Waypoint D at location (0, 6)
Waypoint A at location (0, 0)
Waypoint B at location (6, 0)
Waypoint C at location (6, 6)
Human H1 at location (1, 0)
Robot R1 at location (6, 0)
Fire Flames at location (2, 0) of strength 5
Time 27 FILE> quit
Are you sure you want to quit? (Y/N) Time 27 FILE> y
Fire Flames has disappeared from the simulation






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

