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
  print("Excellent choice, the Hummer eV9! Did you know it has 1000 horsepower? That's the power of one thousand horses!\n")
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
quest_2 = input("\tEnter 'gas' or 'electric':  ")
if quest_2 == 'gas':
  print("\nExcellent choice! You should consider electric though! \nElectric cars have numerous environmental benefits, such as Vehicle-To-Grid Technology, which pushes excess energy from an vehicles battery back into the electrical grid!")
if quest_2 == 'electric':
  print("\nEnvironmentally conscious! Did you know that some electric cars have numerous benefits, such as Vehicle-To-Grid Technology, which pushes excess energy from an vehicles battery back into the electrical grid!")

print("\n===============================================\n")

#Pose Question Three, another short answer question asking if the customer would like their car to start only using their voice.

quest_3 = input("Would you like Voice Rec-Ignition? \nState 'yes' or 'no': ")

#Based on the response to the third question, if yes, prompt the user to see if they would like to know more about Voice Rec-Ignition.

if quest_3 == 'yes':
  quest_llm = input("Would you like to know how Voice Reg-Ignition works? (yes/no)")
  if quest_llm == 'yes':
    print("\nVoice Rec-Ignition uses a transformer-based speech-recognizer for user-specific voice-activated ignition.\n")
    print("\n===================================================\n")
print("What wrap would you like for your vehicle?")
    
#If no, move onto fourth question, asking about the wrap the customer would like to have for their car.

if quest_llm == 'no':
  print("\n===========================================\n")
  print("What wrap would you like for your vehicle?")

print("\ta: Matte")
print("\tb: Pearlescent")
print("\tc: Chrome")
print("\td: Carbon Fiber")

quest_4 = input("\nSelect 'a', 'b', 'c', or 'd' : ")

#Copy the value of the wrap preference & map to name of wrap
wrap_preference = ''
quest_4 = wrap_preference

if wrap_preference == 'a':
  wrap_preference = 'Matte'
if wrap_preference == 'b':
  wrap_preference = 'Pearlescent'
if wrap_preference == 'c':
  wrap_preference = 'Chrome'
if wrap_preference == 'd':
  wrap_preference = 'Carbon Fiber'

#Pose question five, whether the customer would like a nitrous oxide canister to be attached to their vehicle's engine intake system.

print("\n===========================================\n")

quest_5 = input("\nWould you like to increase your vehicles horsepower with a canister of nitrous oxide? (yes/no) : ")

if quest_5 == 'yes':
  quest_nitrous = input("\nWould you like to know how your vehicle utilizes nitrous? (yes/no) : ")
  if quest_nitrous == 'yes':
    print("\nA bottle of nitrous oxide is connected to the car's engine intake system. When the driver activates the nitrous valve, the nitrous is injected into the engine's combustion chamber. The high temperature in the combustion chamber breaks down the nitrous oxide into nitrogen monoxide and oxygen gas. The injection of nitrous oxide into an engine means that more oxygen is available during combustion. The extra oxygen allows the engine to burn more fuel, which produces more power and makes the car go faster. ")







