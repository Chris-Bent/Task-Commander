import argparse
import os
import json
import datetime 

def main():
    task = input("What is ur task?") # should be read from an argparse command 

    def addTask(task):
    
        if os.path.exists("cmdrtasks.json"):
            print(task, "Exists")
        else:
            with open("cmdrtasks.json", "w") as f:
                print("JSON File Created")
        

    addTask(task)

main()

