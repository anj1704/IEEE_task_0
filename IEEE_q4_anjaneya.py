# Anjaneya Bajaj - 2022A7PS0164P
# IEEE Python Task Question 4

class Roman:

    def __init__(self):

        bnum = input("Enter 8 bit unsigned binary number.")
        self.bnum = bnum

    def decimal(self):
        self.num = 0
        for i in range (0,8):
            self.num += (2 ** (i))*int(self.bnum[8 - i - 1])
        print("The decimal representation is : ",self.num)
    
    def convert(self):
        dict = {1:"I",4:"IV",5:'V',9:"IX",10:"X",50:"L",100:"C",40:"XL",90:"XC"}
        n = self.num

        if n == 0:
            print ("Number does not exist in roman numeral system !")
        else:
            rem = 0
            num = 0
            l = []
            rem = int(n / 100)
            l.append(dict[100]*rem)
            n = n % 100
            rem = int(n/10)
            if 1 <= rem <= 3:
                l.append(rem*dict[10])
            elif rem == 4:
                l.append(dict[40])
            elif rem == 5:
                l.append(dict[50])
            elif 6 <= rem <= 8:
                l.append(dict[50]+ dict[10]* (rem - 5))
            n = n % 10
            rem = int(n)
            if 1 <= rem <= 3:
                l.append(rem*dict[1])
            elif rem == 4:
                l.append(dict[4])
            elif rem == 5:
                l.append(dict[5])
            elif 6 <= rem <= 8:
                l.append(dict[5]+ dict[1]* (rem - 5))
            
            self.answer = "".join(l)
            print("The number in roman numerals is : ",self.answer)


a = Roman()
a.decimal()
a.convert()