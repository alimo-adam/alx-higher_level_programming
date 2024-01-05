#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    # Calculate the number of arguments, excluding the script name itself
    num_args = len(sys.argv) - 1

    # Print the number of arguments
    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print(f"{num_args} arguments:")

    # Print each argument along with its position
    for i in range(1, len(sys.argv)):
        print(f"{i}: {sys.argv[i]}")
