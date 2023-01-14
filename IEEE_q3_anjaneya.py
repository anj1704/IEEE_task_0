# Anjaneya Bajaj - 2022A7PS0164P
# IEEE Python Task Question 3

dict = {}
dict_1 = {}
dict_2 = {}
keys = []
values = []

# taking input 

n = int(input("PLease enter the number of terms in the dictionary. "))
while n > 0:
    
    key = eval(input("Enter the key."))
    value = eval(input("Enter the corresponding value."))
    dict.update({key : value})
    keys.append(key)
    values.append([key,value])
    n -= 1

# q1 sorting dictionary with keys in ascending order

n = len(dict)
for i in range(0, n):
    for j in range(0, n-i-1):
        if (keys[j] > keys[j + 1]):
            t = keys[j]
            keys[j]= keys[j + 1]
            keys[j + 1]= t

for i in keys:
    for j in dict.keys():
        if i == j :
            dict_1.update({i:dict[i]})

# q2 sorting dictionary with values in ascending order


for i in range(0, n):
    for j in range(0, n-i-1):
        if (values[j][1] > values[j + 1][1]):
            t = values[j]
            values[j]= values[j + 1]
            values[j + 1]= t

for i in values:
    for j in dict.keys():
        if i[0] == j:
            dict_2.update({j:dict[j]})

print(f"The original dictionary is {dict}. \n")
print(f"On sorting the keys in ascending order we get {dict_1}. \n")
print(f"On sorting the values in ascending order we get {dict_2}. \n")