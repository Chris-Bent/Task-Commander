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
    add_parser = subparsers.add_parser("add", help="Add a new task")
    # Default positional argument for name
    add_parser.add_argument("name", help="Name of the task")
    # Additional positional arguments for added detail on tasks
    add_parser.add_argument("--d", required=False, help="Task Description")
    # Parse Arguments    
    args = parser.parse_args()

    # Handle Subcommands
    if args.command == "add":
        print("IT WORK")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
