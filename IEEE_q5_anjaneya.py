# Anjaneya Bajaj - 2022A7PS0164P
# IEEE Python Task Question 5

class Subset:

    def __init__(self):

        n = int(input("Enter no. of elements in set."))
        self.n = n
        l = []
        for i in range (0,n):
            a = int(input("Input integer."))
            l.append(a)
        l.sort()
        self.set = l

    def sub(self):
        
        N = int(pow(2,len(self.set)))
        s = set()
        self.set.sort()

        for i in range (N):
            subset = []
            for j in range (len(self.set)):
                if i & (1 << j):
                    subset.append(self.set[j])
            
            s.add(tuple(subset))
        
        print(s)


        

a = Subset()
a.sub()