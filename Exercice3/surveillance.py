# /*
#  * /FILE
#  * 	surveillance.py
#  * 
#  * /AUTHOR
#  *      REIF Hugo       <hugo.reif.faudemer@gmail.com>  || <21701260@etu.unicaen.fr>
#  *      
#  * /DESCRIPTION 
#  *      Software for surveillance system for a sensitive site is composed of a drone D and three robots R1, R2 and R3 
#  * 
#  * /DATES
#  *      07/01/2023 : Original Code
#  */

#!/usr/bin/python3
import rospy
from std_msgs.msg import String
import random

def choose_site_to_verify(message):
  # Convert the message to a list of bits
  bits = [int(x) for x in bin(message)[2:]]
  
  # Pad the list with zeros to make it length 3
  bits = [0] * (3 - len(bits)) + bits
  
  # Choose a random site that has not been verified yet
  sites = [i for i, x in enumerate(bits) if x == 1]
  if not sites:
    return message
  site = random.choice(sites)
  
  # Set the bit corresponding to the chosen site to 0
  bits[site] = 0
  
  # Convert the modified list of bits back to an integer
  return int("".join(str(x) for x in bits), 2)

def set_bit(message, site):
  # Convert the message to a list of bits
  bits = [int(x) for x in bin(message)[2:]]
  
  # Pad the list with zeros to make it length 3
  bits = [0] * (3 - len(bits)) + bits
  
  # Set the bit corresponding to the chosen site to 0
  bits[site] = 0
  
  # Convert the modified list of bits back to an integer
  return int("".join(str(x) for x in bits), 2)

# callback function for when the drone publishes a message
def drone_callback(msg):
  message = int(msg.data)  # convert message to integer

  if message != 0:  # if message is not 0, choose a site to verify
    site = choose_site_to_verify(message)  # function to choose a site to verify
    message = set_bit(message, site-1, 0)  # set the bit corresponding to the chosen site to 0
    message_to_publish = String()
    message_to_publish.data = str(message)
    robot1_pub.publish(message_to_publish)  # publish message to robot 2

# callback function for when robot 1 publishes a message
def robot1_callback(msg):
  message = int(msg.data)  # convert message to integer

  if message != 0:  # if message is not 0, choose a site to verify
    site = choose_site_to_verify(message)  # function to choose a site to verify
    message = set_bit(message, site-1, 0)  # set the bit corresponding to the chosen site to 0
    message_to_publish = String()
    message_to_publish.data = str(message)
    robot2_pub.publish(message_to_publish)  # publish message to robot 3

# callback function for when robot 2 publishes a message
def robot2_callback(msg):
  message = int(msg.data)  # convert message to integer

  if message != 0:  # if message is not 0, choose a site to verify
    site = choose_site_to_verify(message)  # function to choose a site to verify
    message = set_bit(message, site-1, 0)  # set the bit corresponding to the chosen site to 0
    message_to_publish = String()
    message_to_publish.data = str(message)
    robot3_pub.publish(message_to_publish)  # publish message to robot 3

if __name__ == '__main__':
  rospy.init_node('surveillance_system')

  # subscribe to messages from the drone
  rospy.Subscriber('drone_messages', String, drone_callback)

  # subscribe to messages from robot 1
  rospy.Subscriber('robot1_messages', String, robot1_callback)

  # subscribe to messages from robot 2
  rospy.Subscriber('robot2_messages', String, robot2_callback)

  # create publishers for each robot
  robot1_pub = rospy.Publisher('robot1_messages', String, queue_size=10)
  robot2_pub = rospy.Publisher('robot2_messages', String, queue_size=10)
  robot3_pub = rospy.Publisher('robot3_messages', String, queue_size=10)

  rospy.spin()

