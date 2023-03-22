
#import libraries
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import RPi.GPIO as GPIO

#Global GPIO initialisation
motor_pin = 16
motor_pin_s2 = 18
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(motor_pin.GPIO.OUT)
GPIO.setup(motor_pin_s2.GPIO.OUT)


#class definitions
#Motor Functions: contains functions for the control of motor 
class MotorFunction():

    def rotateUpwards(self):
        GPIO.output(motor_pin, False)
        GPIO.output(motor_pin_s2, True) 

    def stop(self):
        GPIO.output(motor_pin, False)
        GPIO.output(motor_pin_s2, False)

    def rotateDownwards(self):
        GPIO.output(motor_pin, True)
        GPIO.output(motor_pin_s2, False) 

#MotorSubscriber contains initialisation of subscriber, publisher and has a timer for publishing
#Also contains the conditions to for motor control inside the callback functions   
class MotorSubscriber(Node):

    def __init__(self):
        super()._init__('motor_subscriber')
        self.subscription = self.create_subscription(String, 'lift_topic', self. listener_callback, 10)
        self.subscription # prevent unused variable warning
        self .publisher_ = self.create_publisher(String,'end_lift', 10)
        timer_period = 0.5 #seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        #x = 0

    def timer_callback(self):
        msg = String()
        msg. data = 'End Pose Reached: %d' % self. i
        #self.publisher_publish (msg)
        #self,get_ logger). info('Publishing: "9s' % msg data)
        #self.i += 1

    def listener_callback (self, msg):
        self.get_logger().info('Recieved: "%s"' % msg. data)
        self.data = msg.data
        #print(self.data)
        if msg.data == 'Goal Pose Reached':
            MotorFunction.rotateUpwards()
            self.i += 1 
            if self.i >= 13:
                self.get_logger().info('End Pose Reached')
                msg.data ='End Pose Reached'
                MotorFunction.stop()
                self.i = 0
                self.publisher_publish(msg)

        if msg.data == 'Final Pose Reached':
            MotorFunction.rotateDownwards()
            self.i += 1 
            if self.i >= 13:
                self.get_logger().info('Final Pose Reached')
                msg. data = 'End Pose Reached'
                MotorFunction.stop()
                self.i = 0
                self.publisher_publish(msg)



def main(args=None):
    rclpy.init(args=args)
    motor_subscriber = MotorSubscriber()
    rclpy.spin(motor_subscriber)
    # Destroy the node explicitly
    # Coptional - otherwise it will be done automatically
    # when the garbage collector destroys the node object).
    # stop function to put the motor to False
    MotorFunction.stop()
    motor_subscriber.destroy_node()
    rclpy.shutdown()
