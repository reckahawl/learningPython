import string

card_A = {'Ad':('A dice', 50),'Af':('A flower', 50),'As':('A spade', 50),'Ah':('A heart', 50)}


values = {'abr' : 'Mean'}

d = string.Template("""
 Card Abriviation    : $$Ad
 Card Itself         : $Ad[0]
 Player throw        : ${Ad[0]} is your Play 
""")

print('\tTEMPLATE:\n',d.safe_substitute(card_A))


s = """
Card Itself         :%(As[0])
Card abriviation    :%%As
Player throw        :%(As[0]) is your play
"""

#print('\tINTERPOLATION:\n', s%(card_A))


f = """
Card Itself         : {Af[0]}
Card abriviation    : {{Af}}
Player throw        : {Af[0]} is your play
"""
print('\tFORMAT:', f.format(**card_A))
""" 

card_A = {'Ad':('A dice', 50),'Af':('A flower', 50),'As':('A spade', 50),'Ah':('A heart', 50)}
card_2 = {'2d':('2 dice', 20),'2f':('2 flower', 20),'2s':('2 spade', 20),'2h':('2 heart', 20)}
card_3 = {'3d':('3 dice', 30),'3f':('3 flower', 30),'3s':('3 spade', 30),'3h':('3 heart', 30)}
card_4 = {'4d':('4 dice', 4),'4f':('4 flower', 4),'4s':('4 spade', 4),'4h':('4 heart', 4)}
card_5 = {'5d':('5 dice', 5),'5f':('5 flower', 5),'5s':('5 spade', 5),'5h':('5 heart', 5)}
card_6 = {'6d':('6 dice', 6),'6f':('6 flower', 6),'6s':('6 spade', 6),'6h':('6 heart', 6)}
card_7 = {'7d':('7 dice', 7),'7f':('7 flower', 7),'7s':('7 spade', 7),'7h':('7 heart', 7)}
card_8 = {'8d':('8 dice', 8),'8f':('8 flower', 8),'8s':('8 spade', 8),'8h':('8 heart', 8)}
card_9 = {'9d':('9 dice', 9),'9f':('9 flower', 9),'9s':('9 spade', 9),'9h':('9 heart', 9)}
card_10 = {'10d':('10 dice', 10),'10f':('10 flower', 10),'10s':('10 spade', 10),'10h':('10 heart', 10)}
card_J = {'Jd':('J dice', 11),'Jf':('J flower', 11),'Js':('J spade', 11),'Jh':('J heart', 11)}
card_Q ={'Qd':('Q dice', 12),'Qf':('Q flower', 12),'Qs':('Q spade', 12),'Qh':('Q heart', 12)}
card_K = {'Kd':('K dice', 13),'Kf':('K flower', 13),'Ks':('K spade', 13),'Kh':('K heart', 13)}

cardlist = [card_A, card_2,card_3,card_4,card_5,card_6,card_7,card_8,card_9,card_10,card_J, card_Q,card_K]




def userTuitorial():
    one = input("\t Welcome to my Humble abroad.\nType your username Here\n\t@>")
    two = input("Wonderful user {one} For choosing wisely.\nRules of various Games are found on a .txt file\n\n\t Suicide Type here \n\t@> ")

    print(f"user {one} Welcome to Game {two}.\n\t{one} Has agreed to the terms and condition of game {two}")

    l = ['d', 'D', 's', 'S', 'f', 'F', 'h', 'H']

    print()
    print()

    def uservalid():
        
        print("\t The game is played by the abriviation \n\t Char  Mean\n\t's' 'Spade'\n\t'd' 'Dice'\n\t'h' 'Heart'\n\t'f' 'Flower'")
        print("\t The other Abriviation is the card Number 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'")


        print('\tTEMPLATE:\n',d.safe_substitute(card_A))
        inpOne = input("Try by throwing all the cards of A \t\n i.e all threes will look like\n\t@> 3s3d3f3h :- \n\t @here >>  ")
        
        inpNumber = []
        inpSuit = []
        #while inpOne[0] != '1':
     
        for i in range(len(inpOne)):
            if i%2 == 0 and '1' not in inpOne:
                inpNumber.append(inpOne[i])
            elif i%2==0 and '1' in inpOne:
                inpNumber.append(inpOne[i])
                inpNumber.append(inpOne[i+1])
            else: inpSuit.append(inpOne[i])

        

        #for i in range(len(inpOne)):
        for i in inpOne:
            if i%2 == 0 and i != '1':
                inpNumber.append(i)
            elif i%2 == 0 and j == '1':
                inpNumber.append(i)
                inpNumber.append(inpOne[i+1])
            else: inpSuit.append(i)

       
        #for i in inpOne:
        def oneAbsent(iin):
            for i in range(len(iin)):
                if i%2 == 0 :
                    inpNumber.append(iin[i])
                else:inpSuit.append(iin[i])
        
        def onePre(iin):
            for i in range(len(iin)):
                if iin[i] == '1':
                    inpNumber.append(iin[i])
                elif iin[i] == '0':    
                    inpNumber.append(iin[i])                    
                else:
                
                


            print()  
        if '1' in inpOne:
            onePre(inpOne)
        

        print(inpNumber)
    

        print(inpSuit)
        
    uservalid()
userTuitorial()

"""

