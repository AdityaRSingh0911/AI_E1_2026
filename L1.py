# # SIMPLE REFLEX AGENT FOR VACCUM CLEANER WORLD
# # FUNCTION TO STIMULATE THE VACCUM CLEANER AGENT
# def reflex_vaccum_agent(location,status):
#     if status=="Dirty":
#         return "Suck"
#     elif location=="A":
#         return "Right"
#     elif location=="B":
#         return "Left"
# #Test the reflex agent
# #Environment:Location A is dirty,location B is clean
# location="A"
# status="Dirty"

# #Agent's action
# action=reflex_vaccum_agent(location,status)
# print(f"Location:{location},Status:{status},Action:{action}")

import random
def display(room):
    print(room)

room = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
]
print("All the rooms are dirty")
display(room)


x = 0  
y = 0  

while x < 4:  
    while y < 4:  
        room[x][y] = random.choice([0, 1])
        y += 1 
    x += 1  
    y = 0  

print("Before cleaning the room, I detect all of these random dirts")
display(room)


x = 0  
y = 0  
z = 0  


while x < 4:  
    while y < 4:  
        if room[x][y] == 1:  
            print("Vacuum in this location now:", x, y)
            room[x][y] = 0  
            print("Cleaned:", x, y)
            z += 1 
        y += 1 
    x += 1 
    y = 0  

performance = (100 - ((z / 16) * 100))
print("Room is clean now. Thanks for using the Robot Vacuum Cleaner!")
display(room)
print('Performance=', performance, '%')

  