from argparse import ArgumentParser
import os
import json
import datetime 

def startupCheck():
    print("""
    		                                
                                            Task Commander
                                            
                                            ..:--------:
                                         :#####%%%%%%%%%##*.
                                       .##%%%%%%%%%%%%%%%%%###=
                                      +*%%%%%%%%%%%%%%%%%%%%%%#*:
                                    =#%%%%%%%%%%%%%%%%%%%%%%%%%%-..
                                    +%%%%%%%%%%%%%%%%%%%%%%%%%%%%#.
                                  :%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%.
                                  :%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%+-
                                  :%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*
                                  :%%%:..:-*%%%%%%%%%%%%%%%...=%%%+-
                                  :%%%:  ....#%%%%%%%%%+....  ..*%..
                                  .+*%:         -%%%-:         .*%.
                                  ..+%:     ....-%%%-:....    ..#%.
                                  :%%%:......#%%%%-.#%%%%-....+%%%:.
                                  :%%%%%%%%%%%%%+  .***#%%%%%%%%%%%*
                                  :%%%%%%#*-.#%+=    :%%%-.#%%%%%%%*
                                  .:+#=-.  +%%#...:-.:%%%+=.  =###.
                                           +%%%%%#%%=+%%%=:.
                                           +%**%#*#%%%%%%%%.
                                           +%::%*.*%**%#+#%.
                                           +%::%+ +%.:%+.=+.
                                           :=.:%+ +%.:%+....
                                              .:: +%..:.
                                                  +%.
                                                  ::.

    
    
    """)

    if os.path.isfile("cmdrtasks.json"):
        print("CMDR Task File Already Exists")
    else:
        taskData = {
            "name": input("Task: "),
            "timestamp": "DATETIME"
        }
        with open("cmdrtasks.json", "w") as fileOut:
            json.dump(taskData, fileOut)
        print("CMDR Task File Created")


def addTask():
    pass



def main():

    parser = ArgumentParser(prog="Task Commander", add_help=True)
    parser.add_argument("cmdr")
    parser.add_argument("-a", "--add")
    parser.add_argument("-l", "--list")

    args = parser.parse_args()
    print(args.cmdr, args.add, args.list)

    startupCheck()




main()


