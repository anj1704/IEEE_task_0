# Anjaneya Bajaj - 2022A7PS0164P
# IEEE Python Task Question 2



N = int(input("Enter a number."))

for k in range (0,N):
    print(chr(65+k),end = '')
for m in range (63 + N,64,-1):
    print(chr(m),end = '')

print ("\n")

for i in range (1,N):
    
    for j in range (65,65 + N - i):

        print(chr(j),end = '')
        
    print(" "*(2*i-1),end = " \b")

    for l in range(N-i-1,-1,-1):
        
        temp = 65 + l
        print(chr(temp),end = '')
        
    print("\n")

for i in range(2,N):

    for j in range(65,65 + i):

        print(chr(j),end = '')
    
    print(" "*(2*(N-i)-1),end = " \b")

    for l in range(i,0,-1):

        temp = 65 + l -1
        print(chr(temp),end = '')
        
    print("\n")
    
for k in range (0,N):
    print(chr(65+k),end = '')
for m in range (63 + N,64,-1):
    print(chr(m),end = '')

print ('\n')

for i in range(N):
    for j in range(N):
        if (i == 0 or i == N - 1 or (i+j == N - 1)):
            print("*",end =" ")
        else:
            print(" ",end = " ")
    print()