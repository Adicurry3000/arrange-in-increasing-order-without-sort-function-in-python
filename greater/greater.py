nos = []

vals = int(input('how many values:'))

for i in range(0,vals):
    ints = int(input('enter the values:'))
    nos.append(ints)

new_list = []

minimum = nos[0]

while nos:
    for i in nos:
        if i<minimum:
            minimum = i
            
    for i in nos:        
        if minimum == i:
            new_list.append(minimum)
            nos.remove(minimum)
            if nos:
                minimum = nos[0] 
    
print(new_list)

