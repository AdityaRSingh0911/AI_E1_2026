rows = int(input("Enter number of X values: "))
cols = int(input("Enter number of Y values: "))

joint = []
print("Enter joint probability values row by row:")

for i in range(rows):
    row = list(map(float, input().split()))
    
    if len(row) != cols:
        print("Error: Please enter exactly", cols, "values per row")
        exit()
        
    joint.append(row)

px = [sum(row) for row in joint]
py = [sum(col) for col in zip(*joint)]

px = [round(x, 1) for x in px]
py = [round(x, 1) for x in py]

print("Marginal P(X):", px)
print("Marginal P(Y):", py)