import argparse
import os
import json
import datetime 

def main():

    def addTask(task):
        return os.path.exists("cmdrtasks.json")

        if addtask("cmdrtasks.json"):
            pass
        else:
            data = {
                "task": input("Task: ")
            }

            with open("cmdrtasks.json", "w") as fileOut: # w for write r for read
                json.dump(data, fileOut)

main()

