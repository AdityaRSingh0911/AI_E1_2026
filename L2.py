# SIMPLE REFLEX AGENT FOR VACCUM CLEANER WORLD
# FUNCTION TO STIMULATE THE VACCUM CLEANER AGENT
def reflex_vaccum_agent(location,status):
    if status=="Dirty":
        return "Suck"
    elif location=="A":
        return "Right"
    elif location=="B":
        return "Left"
#Test the reflex agent
#Environment:Location A is dirty,location B is clean initially
location="A"
status="Dirty"

#Define locations
locations=["A","B"]

#Stimulate Agent actions
for _ in range(5):    #Stimulate for 5 iterations
    #Agent's action
    action=reflex_vaccum_agent(location,status)
    print(f"Location:{location},Status:{status},Action:{action}")

    #Update status
    if action=="Suck":
        status="Clean"
    elif action=="Right":
        location="B"
    elif action=="Left":
        location="A"