#--------------------This code was written by Berkay Berat Sönmez--------------------#
import random #We import the random library to generate random numbers.(While importing this library, you may get an error in some IDEs.)

win = 0 #List of how many times we've won without the door change.
count = 0 #List of how many times we've played without the door change.
win2 = 0 #List of how many times we've won with the door change.
count2 = 0 #List of how many times we've played with the door change.
i = 0

while i <= 1000 * 1000:

    #We don't change the door here..
    car_door = random.randrange(0,3) #We decide which door the car is at.
    competitor_door = random.randrange(0,3) #We decide which door the competitor chooses.
    if competitor_door == car_door:  #We look at the competitor wins or not.
        win +=1 #If the competitor wins, we add 1 to the list.
        count +=1 #Counting how many times we played
    else:
        count +=1
        
    #We change the door here..
    car_door = random.randrange(0,3) #We decide which door the car is at.
    competitor_door = random.randrange(0,3) #We decide which door the competitor chooses.
    opened_door = next(j for j in range(3) if j != competitor_door and j != car_door) #We create an iterator for the for the opened the door.
    changed_door =  next(j for j in range(3) if j != opened_door and j != competitor_door) #We create an iterator for the for the change the door.
    if changed_door == car_door: #We look at the competitor wins or not.
        win2 +=1 #If the competitor wins, we add 1 to the list.
        count2 +=1 #Counting how many times we played
    else:
        count2 +=1
    i += 1

#To find the probability of winning, we divide the length of the list of how many times we've won by the length of the list of how many times we've played.
print("The probability of winning if the door is not changed:", win / count) 
print("The probability of winning if the door is changed: ", win2 / count2)
