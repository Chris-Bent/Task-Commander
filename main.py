import argparse
import json
import os
import datetime

# main entry to program
def main():
    # Top-level parser (cmdr)
    parser = argparse.ArgumentParser(prog="cmdr", description="CLI Task Manager")
    subparsers = parser.add_subparsers(dest="command", help="Available Commands")

    # Subparser for 'add' command

if __name__ == "__main__":
    main()
