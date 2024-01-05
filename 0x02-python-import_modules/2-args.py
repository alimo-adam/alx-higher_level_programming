#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    # Number of arguments (excluding the script name)
    num_args = len(sys.argv) - 1

    # Printing the number of arguments
    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print(f"{num_args} arguments:")

    # Printing each argument with its position
    for i in range(1, len(sys.argv)):
        print(f"{i}: {sys.argv[i]}")
