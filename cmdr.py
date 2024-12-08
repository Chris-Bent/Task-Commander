import argparse
import os
import json
import datetime 

def startupCheck():
    if os.path.isfile("cmdrtasks.json"):
        print("Exists")
    else:
        data = {}
        with open("cmdrtasks.json", "w") as fileOut:
            json.dump(data, fileOut)
        print("File created")




def addTask():
    pass



def main():

    startupCheck()




main()


