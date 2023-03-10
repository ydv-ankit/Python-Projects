from sys import platform
from os import system
from getpass import getpass
from time import sleep
from pickle import load, dump

temp = ['SITE', 'USERNAME', 'PASSWORD', 'OTHER DETAILS']


def clrscr():
    if platform == "linux" or platform == "linux2":
        system('clear')
    else:
        system('cls')

def encrypt(data):
    newData = ""
    for i in data:
        newData += chr( ord(i) * 3 -1 )
    return newData

def decrypt(data):
    newData = ""
    for i in data:
        newData += chr((ord(i) + 1)//3)
    return newData

def addData():
    clrscr()
    dataList = list()
    print("\n\tProvide following details...\n\n")
    dataList.append(encrypt(input("\tSITE : ")))
    dataList.append(encrypt(input("\tUSERNAME : ")))
    dataList.append(encrypt(input("\tPASSWORD : ")))
    dataList.append(encrypt(input("\tOTHER DETAILS : ")))
    try:
        with open('userData.dat', 'ab') as file:
            dump(dataList, file)
        input("\tSuccess...")
    except Exception as e :
        print("\t\tFailed...")
        input(e)


def viewData():
    clrscr()
    try:
        with open('userData.dat','rb') as file:
            try:
                while(True):
                    data = load(file)
                    for i in range(4):
                        print(temp[i]," --> ", decrypt(data[i]))
                    print()
            except EOFError:
                input()
                return
    except Exception as e:
        print("\t\tCannot read file...")
        input("\t\t"+e)

def delData():
    pass

def menu():
    clrscr()
    print("\t\t1. Add Data")
    print("\t\t2. View Data")
    print("\t\t3. Delete Data")
    print("\t\t4. Logout")
    op = input("\n\t\t> ")
    if(op == '1'):
        addData()
        menu()
    elif(op == '2'):
        viewData()
    elif(op == '3'):
        delData()
    elif(op == '4'):
        return
    else:
	    input("Invalid input!!")
	    menu()

def login():
    clrscr()
    print("\t>>> Welcome to Password Manager <<<\n\t\t\t\t\t- Cyfer")
    user = input("\n\n\t\tUsername : ")
    passwd = getpass("\n\t\tPassword : ")
    if(user == '' and passwd == ''):
        menu()
    else:
        print("\n\n\t\tInvalid Credentials !!")
        sleep(1)

login()
