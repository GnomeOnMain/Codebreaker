import random
import os
def getInt(msg):
    run=True
    while run==True:
        outpt=1
        inpt=""
        print(msg,end="")
        inpt=input()
        if inpt.find("-")!=-1: #Change if negatives are allowed
            print("\nInvalid input\n")
            continue;
        if inpt.isnumeric()==True:
            outpt*=int(inpt)
            return outpt;
        else:
            print("\nInvalid input\n")
SCORE=[0,0,0]
SCORETF=False
def AIG(C):
    KEY=[0,0,0,0,0,0]
    random.seed()
    C1=-1
    for z in C:
        C1+=1
        C[C1]=random.randrange(1,7)
        KEY[C[C1]-1]+=1
    os.system("cls" if os.name == "nt" else "clear")
    print("The computer has selected its numbers\n")
    print("You may now begin decoding.\n")
    Cz=0
    while Cz<10:
        G=[0,0,0,0]
        GKEY=[0,0,0,0,0,0]
        Gs=[0,0,0]
        Cz+=1
        yes=True
        while yes ==True:
            C2=-1
            GKEY=[0,0,0,0,0,0]
            G=[0,0,0,0]
            Gs=[0,0,0]
            while C2<3:
                C2+=1
                print("Position",C2+1)
                while G[C2]>6 or G[C2]<1: 
                    G[C2]=getInt("Guess a number between 1 and 6: ")
                print(G)
                GKEY[G[C2]-1]+=1
                if KEY[G[C2]-1]==0:
                    Gs[0]+=1
                elif GKEY[G[C2]-1]>KEY[G[C2]-1]:
                    Gs[0]+=1
            print("Is",G,"your guess? Y/N:")
            inp = ""
            while inp!="Y" and inp!="N" and inp!="YES" and inp!="NO":
                inp = input("Answer: ")
                inp = inp.strip()
                inp = inp.upper()
            if inp=="Y" or inp=="YES":
                yes=False
            else:
                yes =True
                GKEY=[0,0,0,0,0,0]
                G=[0,0,0,0]
        C1=-1
        for x in C:
            C1+=1
            C2=-1
            for y in G:
                C2+=1
                if x==y:
                    if C1==C2:
                        Gs[2]+=1
        Gs[1] = 4-Gs[0]-Gs[2]
        if 10-Cz>1:
            print(10-Cz,"rounds left...\n")
        elif Cz==9:
            print(10-Cz,"round left!\n")
        if Gs[0]>0:
            print(Gs[0],"are incorrect\n")
        if Gs[1]>0:
            print(Gs[1],"are in the wrong position\n")
        if Gs[2]>0:
            if Gs[2]==4:
                print("Congratulations, you cracked the code!")
                if SCORETF==True:
                    SCORE[2]+=1
                    SCORE[1]+=1
                break;
            else:
                print(Gs[2],"are perfectly correct\n")
    if Cz==10:
        SCORE[2]+=1
        SCORE[0]+=1
        print("GAME OVER!\n")
        print("The code was:",C)
    print("")
    inp = ""
    if SCORETF==True:
        if SCORE[0]>1:
            print(SCORE[0],": games lost")
        else:
            print(SCORE[0],": game lost")

        if SCORE[1]>1:
            print(SCORE[1],": games won")
        else:
            print(SCORE[1],": game won")

        if SCORE[2]>1:
            print(SCORE[2],": games played")
        else:
            print(SCORE[2],": game played")
    while inp!="Y" and inp!="N" and inp!="YES" and inp!="NO":
        inp = input("Play again? Y/N: ")
        inp = inp.strip()
        inp = inp.upper()
    if inp=="Y" or inp=="YES":
        AIG(C)
    else:
        run=False
    return;
def PG(C):
    KEY=[0,0,0,0,0,0]
    yes=True
    C1=-1
    print("The Codemaker may now enter their numbers.\n")
    while yes ==True:
        KEY=[0,0,0,0,0,0]
        C=[0,0,0,0]
        for z in C:
            C1+=1
            while C[C1]>6 or C[C1]<1: 
                C[C1]=getInt("Enter a number from 1 to 6: ")
                print(C)
                KEY[C[C1]-1]+=1
        print("Is",C,"your code? Y/N:")
        inp = ""
        while inp!="Y" and inp!="N" and inp!="YES" and inp!="NO":
            inp = input("Answer: ")
            inp = inp.strip()
            inp = inp.upper()
            if inp=="Y" or inp=="YES":
                yes=False
            else:
                yes =True
    os.system("cls" if os.name == "nt" else "clear")
    print("The Codemaker has made their code.\n")
    print("You may now begin decoding.\n")
    Cz=0
    while Cz<10:
        G=[0,0,0,0]
        GKEY=[0,0,0,0,0,0]
        Gs=[0,0,0]
        Cz+=1
        yes=True
        while yes ==True:
            C2=-1
            while C2<3:
                C2+=1
                print("Position",C2+1)
                while G[C2]>6 or G[C2]<1: 
                    G[C2]=getInt("Guess a number between 1 and 6: ")
                print(G)
                GKEY[G[C2]-1]+=1
                if KEY[G[C2]-1]==0:
                    Gs[0]+=1
                elif GKEY[G[C2]-1]>KEY[G[C2]-1]:
                    Gs[0]+=1
            print("Is",G,"your guess? Y/N:")
            inp = ""
            while inp!="Y" and inp!="N" and inp!="YES" and inp!="NO":
                inp = input("Answer: ")
                inp = inp.strip()
                inp = inp.upper()
            if inp=="Y" or inp=="YES":
                yes=False
            else:
                yes =True
                GKEY=[0,0,0,0,0,0]
                G=[0,0,0,0]
        C1=-1
        for x in C:
            C1+=1
            C2=-1
            for y in G:
                C2+=1
                if x==y:
                    if C1==C2:
                        Gs[2]+=1
        Gs[1] = 4-Gs[0]-Gs[2]
        if 10-Cz>1:
            print(10-Cz,"rounds left...\n")
        elif Cz==9:
            print(10-Cz,"round left!\n")
        if Gs[0]>0:
            print(Gs[0],"are incorrect\n")
        if Gs[1]>0:
            print(Gs[1],"are in the wrong position\n")
        if Gs[2]>0:
            if Gs[2]==4:
                print("Congratulations, you cracked the code!")
                print("The Codemaker Wins!")
                break;
            else:
                print(Gs[2],"are perfectly correct\n")
    if Cz==10:
        print("GAME OVER! Codemaker Wins!\n")
        if SCORETF == True:
            SCORE[2]+=1
            SCORE[0]+=1
        print("The code was:",C)
    print("")
    inp = ""
    if SCORETF==True:
        if SCORE[0]>1:
            print(SCORE[0],": games won by the Codemaker",sep="")
        else:
            print(SCORE[0],": game won by the Codemaker",sep="")
        if SCORE[1]>1:
            print(SCORE[1],": games won by the Codebreaker",sep="")
        else:
            print(SCORE[1],": game won by the Codebreaker",sep="")
        if SCORE[2]>1:
            print(SCORE[2],": games played")
        else:
            print(SCORE[2],": game played")
    while inp!="Y" and inp!="N" and inp!="YES" and inp!="NO":
        inp = input("Play again? Y/N: ")
        inp = inp.strip()
        inp = inp.upper()
    if inp=="Y" or inp=="YES":
        AIG(C)
    else:
        run=False
    return;

run = True
C=[0,0,0,0]
while (run == True):
    SCORE=[0,0,0]
    os.system("cls" if os.name == "nt" else "clear")
    inp=0
    print("Codebreaker\n")
    print("Options\n")
    print("1: Player vs Player")
    print("2: Player vs Computer")
    print("3: How to play")
    print("4: Credits")
    print("5: Quit\n")
    while inp<1 or inp>5:
        inp = getInt("Your choice: ")
        if inp<1 or inp>5:
            print("Invalid input")
    if inp==1:
        inp = ""
        print("Play with score enabled?")
        while inp!="Y" and inp!="N" and inp!="YES" and inp!="NO":
            inp = input("Answer: ")
            inp = inp.strip()
            inp = inp.upper()
            if inp=="Y" or "YES":
                SCORETF =False
            else:
                SCORETF =True
        PG(C)
    elif inp ==2:
        inp = ""
        print("Play with score enabled? Y/N")
        while inp!="Y" and inp!="N" and inp!="YES" and inp!="NO":
            inp = input("Answer: ")
            inp = inp.strip()
            inp = inp.upper()
            if inp=="Y" or inp=="YES":
                SCORETF =False
            else:
                SCORETF =True
        AIG(C)
    elif inp==3:
       print("\n\nComputer vs Player rules:\n\n")
       print("The computer will select 4 random numbers ranging from 1 to 6.\n")
       print("It is up to the player to try and crack the sequence the computer has selected.\n")
       print("The computer will provide feedback on how many numbers are incorrect, correct but in the wrong place, or fully correct.\n")
       print("If the Player fails to guess the correct pattern within 10 rounds, the computer will have won.\n")
       print("The player may select whether or not to keep track of how many rounds they have won and lost.\n\n")
       print("Player vs Player rules:\n\n")
       print("The Codemaker will select 4 numbers ranging from 1 to 6, after which the Codebreaker will attempt to crack the coded within 10 rounds.\n")
       print("The computer will provide feedback on how many numbers are incorrect, correct but in the wrong place, or fully correct.\n")
       print("The players may select whether or not to keep track of how many rounds the Codemaker and Codebreaker have won.\n")
       pp = input("\nPress Enter to return to the main menu")
    elif inp==4:
        print("Made by a bored Gnome\n")
        pp = input("Press Enter to return to the main menu")
    elif inp==5:
        print("Are you sure you want to exit? Y/N")
        while inp!="Y" and inp!="N" and inp!="YES" and inp!="NO":
            inp = input("Answer: ")
            inp = inp.strip()
            inp = inp.upper()
        if inp=="Y" or inp=="YES":
            run=False
    else:
        print("Invalid input")
