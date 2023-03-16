# Project-4-Motor-Control-with-Sabertooth-
Please have a read through on using the code in the repository.
This repo focuses on connecting a Raspberry Pi 4 Model B to a Sabertooth 2x25 Motor Driver via GPIO I/O pins and controlling a motor for lifting and lowering a scissors lift



Step 1:
  Ensure you have all the necessary ROS2 packages installed on your OS( I am using Ubuntu 22.04 with ROS2 Humble but it should work well with Foxy as well)
  
Step 2:
  Connecting up the Motor Driver to your Raspberry Pi 4
  For the sake of controlling 1 motor, connections to 0V(GND) , 5V(PWR), S1 , S2 would be needed.
  S1 , S2 should be connected to the output pins that you declared on your RPi
  ![image](https://user-images.githubusercontent.com/92089905/225609329-4eea2289-9a6c-4930-923c-0e9b69109b36.png)

  Ensure that the Motor Driver is powered , either by an external power source connected to B+/ B- or powered with the RPi( If there is enough voltage)
  ![image](https://user-images.githubusercontent.com/92089905/225581416-b644f78d-dd99-4dd3-ad81-be2b20858320.png)
  
  Step 3: 
    Be sure to find IP address that your RPi is connected to, open a command terminal(personally prefer to use Terminator) and type in ssh user@ip address(mine would     be pi@123.456.789.1 for example) 
    Create a ROS2 workspace with its src folder, colcon build and create your package in the src folder
    you may use the python script provided in this repo to test that it works else you may also write your own python/c++ script in the package and use it
    
  Essentially you should see your motor moving when it recieves the compared string from the topic it is subscribed to and after recieving for set amount of times,   
  publishes to an end_topic a string which will tell the noded subscribed to that node that operaation is complete.
  
  To test you would need a simple publisher that publishes to /lift_topic 'Goal Pose Reached'.


  
