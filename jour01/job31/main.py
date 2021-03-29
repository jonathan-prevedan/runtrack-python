import math

# mylist = [*range(10, 21, 1)]
# print(mylist[1])

# p= [mylist[1]]
# q= [5]

# if math.dist(p,q) >= 5:
#     print("Helo")



def arrondi():
    mylist = [20,80,83,43,33,63,73,72,70,35,53]
    p = [mylist[1]]
    q = [5]
    if math.dist(p,q) <=3:
        print("yes")
        list2 = []
        p.append(list2)

    else:
        print("sorry")  
        
arrondi()
    
