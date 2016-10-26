from datetime import datetime
import sqlite3

def timer(start_time):
    return (start_time-datetime.now()).total_seconds()

def begin():
    print ("\n\n\t\tWELCOME TO QUIZMASTER 3000!")
    print ("\n\t1 --> Login")
    print ("\t2 --> Sign Up")
    print ("\t3 --> Exit")

    try:
        choice=int(input("\n\tEnter your choice - "))

        if (choice==1):
            login()
        elif (choice==2):
            signup()
        elif (choice==3):
            print ("\nTHANK YOU FOR PLAYING! GOODBYE!")
        else:
            print ("\nWRONG CHOICE! PLEASE ENTER A VALID OPTION!")
            
    except ValueError:
        print ("\nWRONG CHOICE! PLEASE ENTER A VALID OPTION!")
        begin()
        
def signup():
    
