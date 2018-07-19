import random
X=0
budget=500
thing = 0
tryi = 0
win = 0
bine = 13
Y=0
turn=0
XC=0
var = 0
endspots=0
def run():
    global X
    global XC
    global turn
    global budget
    global thing
    global Y
    def boi():
        check()
    def check():
        global endspots
        tryi = 0
        win = 0
        bine = 13
        var = 0
        while tryi<=26:
            tryi=int(tryi)+1
            var = random.randint(0,1)
            if var==1:
                bine=int(bine)+1
            else:
                bine=int(bine)-1                
        else:
            if bine==26 or bine==1:
                win=8192
            if bine==25 or bine==2:
                win=4096
            if bine==24 or bine==3:
                win=2048
            if bine==23 or bine==4:
                win=1024
            if bine==22 or bine==5:
                win=256
            if bine==21 or bine==6:
                win=128
            if bine==20 or bine==7:
                win=64
            if bine==19 or bine==8:
                win=32
            if bine==18 or bine==9:
                win=16
            if bine==17 or bine==10:
                win=8
            if bine==16 or bine==11:
                win=4
            if bine==15 or bine==12:
                win=2
            if bine==14 or bine==13:
                win=0
    X=int(X)+1
    thing=0
    def thinge():
        runres()
    def runres():
        global X
        global XC
        global turn
        global tryi
        global Y
        global budget
        global bine
        global thing
        if turn==0:
            print ("Your budget is $",budget,"")
            N=input("How many chips would you like to drop? Each chip costs $100: ")
            XC=int(N)
            Y=int(N)*100
            budget=int(budget)-int(Y)
            thing = 0
            turn = turn + 1
        while XC!=0:
            XC=int(XC)-1
            var = 0
            bine = 13
            tryi=0
            win = 0
            while tryi<=26:
                tryi=int(tryi)+1
                var = random.randint(0,1)
                if var==1:
                    bine=int(bine)+1
                else:
                    bine=int(bine)-1                
            else:
                if bine==26 or bine==1:
                    win=8192
                    budget=budget+win
                if bine==25 or bine==2:
                    win=4096
                    budget=budget+win
                if bine==24 or bine==3:
                    win=2048
                    budget=budget+win
                if bine==23 or bine==4:
                    win=1024
                    budget=budget+win
                if bine==22 or bine==5:
                    win=256
                    budget=budget+win
                if bine==21 or bine==6:
                    win=128
                    budget=budget+win
                if bine==20 or bine==7:
                    win=64
                    budget=budget+win
                if bine==19 or bine==8:
                    win=32
                    budget=budget+win
                if bine==18 or bine==9:
                    win=16
                    budget=budget+win
                if bine==17 or bine==10:
                    win=8
                    budget=budget+win
                if bine==16 or bine==11:
                    win=4
                    budget=budget+win
                if bine==15 or bine==12:
                    win=2
                    budget=budget+win
                if bine==14 or bine==13:
                    win=0
                    budget=budget+win
                print ("This chip landed in bin",bine,"! You won $",win,"! Your new balance is $",budget,".The bins are numbered 26,25 and so on")
        if budget>=100:
                    turn = 0
                    thinge()
        else:
            print ("You seem to have gambling issues. Please do your family a favor and contact the National Gambling Help Hotline at 1-800-522-4700")
    thinge()
run()
