import os
import time


class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PINK = '\033[95m'
    CYAN = '\033[96m'
    ORANGE = '\033[89m'
    END = '\033[97m'


def menu():
    print(colors.PINK + "\tElectoral System")
    print("\t*****************\n" + colors.BLUE)
    # Print statements to display menu options to user
    print("\t\t1. Setup polling station votes file")
    print("\t\t2. Enter polling booth")
    print("\t\t3. Review statistics")
    print("\t\t4. Exit" + colors.END)

    while True:  # Will infinitely run until user enters appropriate data
        try:
            menOpt = int(input("\tEnter menu option: "))
            if menOpt > 4 or menOpt < 1:
                print(colors.RED + "Please enter 1-4" + colors.END)
            elif len(str(menOpt)) == 1:
                return menOpt
            else:
                print(colors.RED + "Please enter 1-4" + colors.END)
        except ValueError:  # Checks for ValueError exception, catches it and returns the print statement below
            print(colors.RED + "Please Enter a Number From 1 to 4" + colors.END)


def revStatsMenu():
    print(colors.PINK + "\tReview Statistics - Votes Analysis")
    print("\t**********************************\n" + colors.BLUE)
    # Print statements to display menu options to user
    print("\t\t1. Display votes tally (ordered by party name)")
    print("\t\t2. Display votes tally (ordered in descending order of votes)")
    print("\t\t3. Overall winner, with percentage share of the total votes")
    print("\t\t4. Percentage breakdown of male to female split")
    print("\t\t5. Return to main menu" + colors.END)

    while True:  # Runs infinitely until appropriate data is entered
        try:
            revOpt = int(input("Enter Menu Option: "))
            if revOpt > 5 or revOpt < 1:  # Checks if user enters a number outside the menu's options and returns
                print(colors.RED + "Please Enter 1 - 5" + colors.END)
            else:
                return revOpt
        except ValueError:  # Checks for ValueError exception, catches it and returns the below print statement
            print(colors.RED + "Please Enter 1 - 5" + colors.END)


def orderByPartyName(parties):
    print("| & ***** Votes in Order of Party Names ***** & |\n")
    i = 0
    with open("Belfast_SouthEast.txt", "r") as file:  # Opens "Belfast_SouthEast.txt in read only mode"
        for _ in parties:  # For loop to iterate through each value in the parties list
            print(parties[i] + " - " + file.readline().strip("\n"))
            # Prints party name with the suitable values in file
            i += 1
    input("\n| & ***** Press Enter to Return to Statistics Menu ***** & |")


def votesDesc(parties):
    fileLines = []

    with open("Belfast_SouthEast.txt") as file:
        for lines in file:  # iterates through each line in file and saves it to a list
            fileLines.append(lines.rstrip("\n"))
    try:
        partiesWithValues = {parties[0]: fileLines[0],  # Dictionary to pair each line of text file
                             parties[1]: fileLines[1],  # With correct party name in parties list
                             parties[2]: fileLines[2],  # Eg. parties[0] = "Blue parties" and the first line
                             parties[3]: fileLines[3],  # of text file(fileLines[0]) will always correspond
                             parties[4]: fileLines[4]}  # to the blue party value

        partiesWithValuesSorted = sorted(partiesWithValues.items(), key=lambda y: y[1], reverse=True)

        # Sorts above dictionary by value
        # Uses a lambda function (inline function)
        # to refer to index 1 of the dictionary value
        # which is equal to the numeric value of votes
        # found in the text file

        print("| & *** parties in Descending Order of Votes *** & |\n")
        for x in partiesWithValuesSorted:  # Runs through each value in sorted dictionary and displays them
            print(x[0] + " - " + x[1])
    except IndexError:  # Catches IndexError exception and prints below text
        print(colors.RED + "\nPlease Enter Polling Booth Before Using This Option..." + colors.END)
    input("\n| & ***** Press Enter to Return to Statistics Menu ***** & |")  # Code will pause until user presses enter


def overallWinner(partyVars, parties):
    print("| & ***** The Overall Winner Can Be Seen Below ***** & |")
    try:
        i = partyVars.index(max(partyVars))  # Finds the index of the max value inside the partyVars list
        percent = (max(partyVars) / sum(partyVars) * 100)  # Calculates the percentage share
        if percent == 0:  # If the result is 0 then the below message is printed
            print("All parties Currently Hold 0 Votes")
        else:  # If the result is not 0 then the below statement is displayed
            print("\n" + parties[i] + " With " + str(round(percent, 2)) + "% of the votes")
    except ZeroDivisionError:  # Catches ZeroDivisionError and prints the below message
        print("\n\tAll parties Currently Hold 0 Votes")

    input("\n| & ***** Press Enter to Return to Statistics Menu ***** & |")


def Male2Female(mCount, fCount):
    print("| & ***** Male:Female Percentage Split ***** & |")

    total = mCount + fCount  # Calculates the total count of voters
    try:
        maleSplit = (mCount / total) * 100  # Calculates percentage of male voters
        femaleSplit = (fCount / total) * 100  # Calculates percentage of female voters

        print("\n\t" + str(round(maleSplit, 2)) + "% of Voters Were" + colors.BLUE + " Male" + colors.END)
        #  Prints male and female split rounded to 2 decimal places
        print("\t" + str(round(femaleSplit, 2)) + "% of Voters Were" + colors.PINK + " Female" + colors.END)

    except ZeroDivisionError:  # Catches ZeroDivisionError and prints below message
        print(colors.RED + "\nPlease Enter Polling Booth Before Using This Option..." + colors.END)

    input("\n| & ***** Press Enter to Return to Statistics Menu ***** & |")  # Waits for user input before continuing


def setFile():
    with open("Belfast_SouthEast.txt", "w") as file:
        for x in range(7):  # Will iterate 7 times resulting in 7 0's being written to "Belfast_SouthEast.txt"
            file.write("0\n")  # Writes 0 to the file and takes a new line each time

    print("\n\t& | ***** Setting Up File ***** | &")
    time.sleep(0.75)  # Pauses for 750 milliseconds

    if os.path.exists("Belfast_SouthEast.txt"):  # Checks if file exists and returns message
        print("\n\t& | ***** File Successfully Created ***** | &\n")
        time.sleep(0.75)  # Pauses for 750 milliseconds
    else:  # If file does not exist then displays the below message
        print(colors.RED + "\n\t& | ***** File Could Not Be Created ***** | &\n" + colors.END)
        time.sleep(0.75)  # Pauses for 750 milliseconds


def pollingBooth(maleCount, femaleCount, partyVars, parties):
    finished = "N"  # finished begins as 'N'
    print("\t***** Polling Booth *****")

    print("\n--- Choose Your Gender ---\n")

    while finished == "N":  # While loop to run so long as finished remains = to 'N'
        votes, i = [], 0
        while True:  # Infinitely loops until each m or f is entered
            MorF = input(colors.BLUE + "Male[M]" + colors.END + " OR " + colors.PINK + "Female[F]: " + colors.END).upper()
            # Converts user input to uppercase, input is not case-sensitive
            if MorF == "M":
                maleCount += 1  # If m is entered then increment the maleCount by 1
                break
            elif MorF == "F":
                femaleCount += 1  # If f is entered then increment the femaleCount by 1
                break
            else:
                print(colors.RED + "Please Enter 'M' Or 'F'" + colors.RED)
                # If neither m nor f are entered then the user is instructed as seen
                # until m or f has been entered
                continue

        while i <= 4:
            print(parties[i])  # Prints each party name

            while True:
                try:
                    vote = int(input("Enter Vote(0-5): "))  # Prompts user for numeric input
                    if vote not in votes and vote == 0:  # if input is not contained in votes list then allow the input
                        partyVars[i] += 0  # add 0 to partyVars value
                        i += 1  # increment i by 1, this moves the partyVars value along as well as the parties value
                    elif vote not in votes and vote == 1:
                        votes.append(vote)
                        # If proper input is entered then vote is added to a list
                        # This prevents the user entering the same number more than once other than 0
                        partyVars[i] += 1
                        i += 1
                    elif vote not in votes and vote == 2:
                        partyVars[i] += 0.5
                        votes.append(vote)
                        i += 1
                    elif vote not in votes and vote == 3:
                        partyVars[i] += 0.33
                        votes.append(vote)
                        i += 1
                    elif vote not in votes and vote == 4:
                        partyVars[i] += 0.25
                        votes.append(vote)
                        i += 1
                    elif vote not in votes and vote == 5:
                        partyVars[i] += 0.2
                        votes.append(vote)
                        i += 1
                    elif vote > 5 or vote < 0:  # If the input is outside the given boundaries then the user is reminded
                        print(colors.RED + "Enter a Number From 0-5" + colors.END)
                    else:
                        print(colors.RED + "| *** Please Enter A Different Number *** |" + colors.END)
                        # If user enters 2 of the same number other
                        # than 0 they will be asked to enter a different number
                        time.sleep(0.5)  # Pauses for 500 milliseconds
                except ValueError:  # Catches ValueError and returns below message
                    print(colors.RED + "Enter a Number From 0-5" + colors.END)
                else:
                    break
        finished = input("Finished Polling(Y/N): ").upper()
        # Asks user if polling is finished and converts all input to uppercase

        if finished == "Y":
            while True:  # Password prompt will loop until correct password has been entered or CANCEL has been entered
                password = input("Enter Password to Continue: ")
                # if finished = 'y' then user is asked to enter password
                if password == "Belfast_SouthEast.txt":
                    break
                elif password == "CANCEL":
                    finished = "N"
                    break
                else:
                    print("Password Incorrect")
                    # if password does not equal CANCEL or 'Belfast_SouthEast.txt'
                    # then user is told the password is incorrect
                    continue
        elif finished == "N":
            print("\n| & *** Polling Continues *** & |"
                  "\n\n--- Choose Your Gender ---\n")
        elif finished != "Y" and finished != "N":  # If finished is neither y nor n then invalid input has been received
            while True:
                finished = input(colors.RED + "Please enter 'Y' or 'N': " + colors.END).upper()
                # If finished is neither y nor n then user is told to
                # enter either y or n and input is converted to uppercase
                if finished == "Y" or finished == "N":
                    break
    return maleCount, femaleCount, partyVars
    # Returns these updated values to the main function to be passed into other functions in the program


def revStats(partyVars, mCount, fCount, parties):
    with open("Belfast_SouthEast.txt", "w") as file:
        i = 0
        for _ in partyVars:
            file.write(str(round(partyVars[i], 2)) + "\n")
            # Runs through each index of partyVars and writes it to the file
            i += 1  # Increments i by 1 each time the loop is run, moving the index along each time
        file.write(str(mCount) + "\n")
        file.write(str(fCount) + "\n")

    revOpt = revStatsMenu()  # Creates a variable to hol the value returned by the statistics menu

    while revOpt != 5:  # If 5 is entered then the loop is terminated
        if revOpt == 1:
            orderByPartyName(parties)
            revOpt = revStatsMenu()
            # Reassigns the revOpt variable to allow for a different input than the original
        elif revOpt == 2:
            votesDesc(parties)
            revOpt = revStatsMenu()
        elif revOpt == 3:
            overallWinner(partyVars, parties)
            revOpt = revStatsMenu()
        elif revOpt == 4:
            Male2Female(mCount, fCount)
            revOpt = revStatsMenu()

    print("Returning to Main Menu...")
    time.sleep(0.5)  # Pauses for 500 milliseconds


def main():
    partyVars = [0, 0, 0, 0, 0]  # partiesVars e.g. the votes each party holds initialized at 0 for each party
    maleCount, femaleCount = 0, 0  # Male, female count initialized at 0
    parties = (colors.BLUE + "Blue Party" + colors.END,  # Declares the party names list, declared in the main so
               colors.GREEN + "Green Party" + colors.END,
               # it is only declared once and then is passed from function to funtion within the program
               colors.YELLOW + "Orange Party" + colors.END,
               # Also stored in the form of a tuple to prevent changes to the data
               colors.RED + "Red Party" + colors.END,
               colors.YELLOW + "Yellow Party" + colors.END)
    menOpt = menu()  # Creates a variable to store value returned from menu function

    while menOpt != 4:  # Runs with any input other than 4
        if menOpt == 1:
            if os.path.exists("Belfast_SouthEast.txt"):
                # Checks if the file "Belfast_SouthEast.txt" exists before continuing
                print(colors.RED + "\n\t| ***** The file already exists! ***** |\n" + colors.END)
                time.sleep(0.75)  # Pauses for 750 milliseconds
                menOpt = menu()  # menOpt variable reassigned allowing user to enter different input than before
            else:
                setFile()
                # if the file does not exist then the file setup function is called, file is created and 7 0's written
                menOpt = menu()
        elif menOpt == 2:
            if os.path.exists("Belfast_SouthEast.txt"):
                maleCount, femaleCount, partyVars = pollingBooth(maleCount, femaleCount, partyVars, parties)
                menOpt = menu()
            else:
                print("\n| & *** Please Set Up The Polling File Before Using This Option *** & |\n")
                time.sleep(1)
                menOpt = menu()
        elif menOpt == 3:
            if os.path.exists("Belfast_SouthEast.txt"):
                revStats(partyVars, maleCount, femaleCount, parties)
                menOpt = menu()
            else:
                print("\n| & *** Please Set Up The Polling File Before Using This Option *** & |\n")
                time.sleep(1)  # Pauses the program for 1 whole second
                menOpt = menu()

    print(colors.PINK + "\n\t| ***** GoodBye! ***** |")
    time.sleep(0.5)


main()  # Calls the main function of the program to being execution
