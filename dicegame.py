import random
import time

rounds = 1
p1score = 0
p2score = 0
p1loggedin = False
p2loggedin = False
continueg = False
while p1loggedin == False:
    #P1 Login/Register
    print("P1 : Do you have an account?")
    print("1 ~ Register ")
    print("2 ~ Login ")
    wsel = input("-> ")


    if wsel == "1":
        while True:
            username  = input("Enter a username: ")
            password  = input("Enter a password: ")
            password1 = input("Confirm password: ")
            if password == password1:
                file = open("database.txt", "a+")
                file.write(username+":"+password+" "+"|"+" ")
                file.close()
                wsel = "2"
                break
            print("Passwords do NOT match!")
     
    if wsel == "2":
        while True:
            login1 = input("Username:")
            login2 = input("Password:")
            file = open("database.txt", "r")
            data = file.readline()
            file.close()
            if (login1+":"+login2) in data:
                p1loggedin = True
                print("Welcome P1")
                break
            print("Incorrect username or password.")

    if wsel == "admin":
        p1loggedin = True
        p2loggedin = True


while p2loggedin == False and p1loggedin == True:
    #P2 Login/Register
    print("")
    print("P2: Do you have an account?")
    print("1 ~ Register ")
    print("2 ~ Login ")
    wsel = input("-> ")


    if wsel == "1":
        while True:
            username1  = input("Enter a username: ")
            password  = input("Enter a password: ")
            password1 = input("Confirm password: ")
            if password == password1:
                file = open("database.txt", "a+")
                file.write(username+":"+password+" "+"|"+" ")
                file.close()
                wsel = "2"
                break
            print("Passwords do NOT match!")

            if username == username1:
                print("Username already in use")
     
    if wsel == "2":
        while True:
            login3 = input("Username:")
            login4 = input("Password:")
            file = open("database.txt", "r")
            data2 = file.readline()
            file.close()
            if (login3+":"+login4) in data2:
                p2loggedin = True
                print("Welcome P2")
                break
            
            print("Incorrect username or password.")


while p1loggedin == True and p2loggedin == True:
    print("Home")
    print("1 ~ Play Game ")
    print("2 ~ Log out")
    sel = input("-> ")

    if sel == "2":
        p1loggedin = False
        p2loggedin = False
        print("P1 & P2: You have logged out")
        break

    if sel == "1":
        print("")
        print("Welcome to Squid Game")
        while rounds < 5:
            print("")
            print("")
            print("")
            print("")
            print("")
            #P1 Roll Dice
            print("Round:", rounds)
            print("------------------")
            print("P1: Roll dice?")
            print("1 ~ Yes ")
            print("2 ~ No ")
            dicei = input("-> ")
            if dicei == "2":
                p1loggedin = False
                p2loggedin = False
                print("P1 & P2: You have logged out")
                break
            if dicei == "1":
                p1roll = random.randint(1, 6)
                p1roll2 = random.randint(1, 6)
                print("P1: Roll 1 ~", p1roll, " Roll 2 ~", p1roll2)
                time.sleep(1)
                print("----------------------------")
                print("P1's combined total = [", p1roll + p1roll2,"]")
                p1total = p1roll + p1roll2
                if (p1total % 2) == 0:
                    p1score += 10
                    if p1score < 0:
                        p1score = 0
                    print("P1: Score =", p1score)
                else:
                    p1score -= 5
                    if p1score < 0:
                        p1score = 0
                    print("P1: Score =", p1score)
                p1loggedin = False
                
                
            #P2 Roll Dice
            print("")
            print("")
            print("")
            print("P2: Roll dice?")
            print("1 ~ Yes ")
            print("2 ~ No ")
            dicei = input("-> ")
            if dicei == "2":
                p1loggedin = False
                p2loggedin = False
                print("P1 & P2: You have logged out")
                break
            if dicei == "1":
                p2roll = random.randint(1, 6)
                p2roll2 = random.randint(1, 6)
                print("P2: Roll 1 ~", p2roll, " Roll 2 ~", p2roll2)
                time.sleep(1)
                print("----------------------------")
                print("P2's combined total = [", p2roll + p2roll2,"]")
                p2total = p2roll + p2roll2
                if (p2total % 2) == 0:
                    p2score += 10
                    if p2score < 0:
                        p2score = 0
                    print("P2: Score =", p2score)
                else:
                    p2score -= 5
                    if p2score < 0:
                        p2score = 0
                    print("P2: Score =", p2score)
                p2loggedin = False
            rounds += 1
            continueg = True 



while continueg == True:
    ovrt = "Overtime"
    if p1score == p2score: # Continues to overtime if player scores are the same at the end of the game.
        print("")
        print("")
        print("")
        time.sleep(1)
        print("Round:", ovrt)
        print("------------------")
        print("P1: Roll dice?")
        print("1 ~ Yes ")
        print("2 ~ No ")
        dicei = input("-> ")
        if dicei == "2":
            p1loggedin = False
            p2loggedin = False
            print("P1 & P2: You have logged out")
            break
        if dicei == "1":
            p1roll = random.randint(1, 6)
            p1roll2 = random.randint(1, 6)
            print("P1: Roll 1 ~", p1roll, " Roll 2 ~", p1roll2)
            time.sleep(1)
            print("----------------------------")
            print("P1's combined total = [", p1roll + p1roll2,"]")
            p1total = p1roll + p1roll2
            if (p1total % 2) == 0:
                p1score += 10
                if p1score < 0:
                    p1score = 0
                print("P1: Score =", p1score)
                time.sleep(1)
            else:
                p1score -= 5
                if p1score < 0:
                    p1score = 0
                print("P1: Score =", p1score)
                time.sleep(1)
            p1loggedin = False

    #P2 Roll Dice
        print("")
        print("")
        print("")

        time.sleep(1)
        print("Round:", ovrt)
        print("------------------")
        print("P2: Roll dice?")
        print("1 ~ Yes ")
        print("2 ~ No ")
        dicei = input("-> ")
        if dicei == "2":
            p1loggedin = False
            p2loggedin = False
            print("P1 & P2: You have logged out")
            break
        if dicei == "1":
            p2roll = random.randint(1, 6)
            p2roll2 = random.randint(1, 6)
            print("P2: Roll 1 ~", p2roll, " Roll 2 ~", p2roll2)
            time.sleep(1)
            print("----------------------------")
            print("P2's combined total = [", p2roll + p2roll2,"]")
            p2total = p2roll + p2roll2
            if (p2total % 2) == 0:
                p2score += 10
                if p2score < 0:
                    p2score = 0
                print("P2: Score =", p2score)
                time.sleep(1)
            else:
                p2score -= 5
                if p2score < 0:
                    p2score = 0
                print("P2: Score =", p2score)
                time.sleep(1)
            p2loggedin = False
        rounds += 1
        continueg = True

        
    winner = max(p1score, p2score)
    p1 = "Player 1"
    p2 = "Player 2"
    if winner == p1score:
        print(p1, "is the winner!")
    elif winner == p2score:
        print(p2, "is the winner!")
    
    print("Game Over!")
    break

            
            
        
        
        

















        
    




        
