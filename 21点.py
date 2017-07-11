import random
player1=0
final1=0
player2=0
final2=0
def add1():
        global player1
        global player2
        global final1
        global final2
        change=random.randint(1,10)
        i=raw_input("do you want to add? Y or N?")
        if i=="Y":
            player1+=change
            print "your number is",player1      
        if i=="N":
            final1=1
            print "your final number is",player1
      
def add2():
        global flag
        global player1
        global player2
        global final1
        global final2
        change=random.randint(1,13)
        i=raw_input("do you want to add? Y or N?")
        if i=="Y":
            player2+=change
            print "your number is",player2
        if i=="N":
            final2=1
            print "your final number is",player2        

while 1:
        if  player1<=21 and final1==0:
                print "[player1]your number is",player1
                add1()        
        if player2<=21 and final2==0:
                print "[player2]your number is",player2
                add2()
        if player1>21:
                print"player2 wins!"
                break
        if player2>21:
                print"player1 wins!"
                break
        if final1==1 and final2==1:
                if player1>player2:
                    print"player1 wins!"
                if player1<player2:
                    print"player2 wins!"
                if player1==player2:
                    print"tie!"
                break

