# Anjaneya Bajaj - 2022A7PS0164P
# IEEE Python Task Question 1 

n = int(input("Enter the number of test cases."))
N = 0

while n > 0 :

    flag = True 
    while flag:

        N = int(input("Enter the length of the initial string - should be even."))
        if N % 2 == 0:
            flag = False
        else :
            print("Try again with a string of even length.")
        

    S = input("Enter the string with length {}.".format(N))

    # condition for getting same string back on joining

    L = len(S)

    P = S[0 : int(L/2)]
    Q = S[int(L/2) : L]

    if (P == Q):
        print("Yes")

    else : 
        print("No")

    n = n-1


#####new commit################

<<<<<<< HEAD
### random new commit $##$####
=======
## random 2 ###
>>>>>>> feature-b
