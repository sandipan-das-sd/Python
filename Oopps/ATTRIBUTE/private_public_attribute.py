class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass # now acc.pass is private we cant access the account password outside the class
    #we can access the password now because it is now out of the class 
    def reset_pass(self):
        print(self.__acc_pass)
acc1=Account("12345","abcde")
print(acc1.acc_no)
print(acc1.__acc_pass)
print(acc1.reset_pass())

        

        