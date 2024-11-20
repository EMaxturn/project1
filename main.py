#Snowblue Detail & Body is a Customs Shop in the year 2034.
#Introduce the Snowblue Detail & Body Customization Form 
print("==============================")
print("Welcome to the Snowblue Detail\n & Body Customization Form!")
print("==============================\n")

#Pose Multiple Choice Question One, each choice corresponding to a particular make & Model of a car. 
#Use an if statement to compliment the customer on their choice, giving a fun fact about the car they chose. 
print("What make & model would you like customized?")
print()
print('a: Hummer eV2')
print('b: Tesla Roadster')
print('c: Mercedez-Benz GLE 350')
print('d: Dodge Charger\n')

quest_1 = input("Select 'a', 'b', 'c', or 'd' : ")
print()

#Use series of if statements to compliment the customer on their choice, giving a fun fact about the car they chose. 
if quest_1 == 'a':
  print("Excellent choice, the Hummer eV9! Did you know it has 1000 horsepower? That's the power of one thousand horses!")
if quest_1 == 'b':
  print("Excellent choice, the Tesla Roadster! Did you know that the Tesla Roadster was the first")
if quest_1 == 'c':
  print("Excellent choice, the Mercedez-Benz GLE 350! \n\nDid you know that the 'G' in GLE stands for Geländewagen, which is German for 'off-road vehicle' or 'off land wagon'? The 'L' links the GLE to the E-Class, making the GLE the SUV equivalent of the E-Class.")
if quest_1 == 'd':
  print("Excellent choice, the Dodge Charger! Did you know it ...")
  

print("===========================================")

print()

#Pose Question Two, a short answer question asking if the customer would like a gas or electric model.

print('Would you like a gas or electric model?')
quest_2 = input("Enter 'gas' or 'electric':  ")
print("Excellent choice! You should consider electric though!  Electric cars have numerous environmental benefits, such as Vehicle-To-Grid Technology, which pushes excess energy from an vehicles battery back into the electrical grid!")

print("===========================================\n")

#Pose Question Three, another short answer question asking if the customer would like their car to start only using their voice.

quest_3 = input("Would you like Voice Rec-Ignition? \nState 'yes' or 'no': ")

#Based on the response to the third question, if yes, prompt the user to see if they would like to know more about Voice Rec-Ignition.

if quest_3 == 'yes':
  quest_llm = input("Would you like to know how Voice Reg-Ignition  works?")
#If no, move onto fourth question
if quest_llm == 'no':
  print()
  quest_4


