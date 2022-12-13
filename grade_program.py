#!/usr/bin/env python3

# Created by: Nolan Shami
# Created on: Dec 13th, 2022
# This program gets the users grade as a level,
# It then returns the middle percentage mark.


# Function that uses a switch case to
# display the middle percentage.
def calc_mark(level):
    # switch case to display the middle percentage for each level
    match level:
        case "4+":
            message = "Level {} has a middle percentage of 98%".format(level)
        case "4":
            message = "Level {} has a middle percentage of 91%".format(level)
        case "4-":
            message = "Level {} has a middle percentage of 83%".format(level)
        case "3+":
            message = "Level {} has a middle percentage of 78%".format(level)
        case "3":
            message = "Level {} has a middle percentage of 75%".format(level)
        case "3-":
            message = "Level {} has a middle percentage of 71%".format(level)
        case "2+":
            message = "Level {} has a middle percentage of 68%".format(level)
        case "2":
            message = "Level {} has a middle percentage of 65%".format(level)
        case "2-":
            message = "Level {} has a middle percentage of 61%".format(level)
        case "1+":
            message = "Level {} has a middle percentage of 58%".format(level)
        case "1":
            message = "Level {} has a middle percentage of 55%".format(level)
        case "1-":
            message = "Level {} has a middle percentage of 51%".format(level)
        case _:
            message = "Level {} is a -1 and has a middle percentage of 25%".format(
                level
            )
    return message


# Main function that gets the user's grade level
# then calls the percentage function to get the middle percentage
def main():

    # Get the user's grade level
    level_user = input("Enter the level you want as a percentage: ")
    print("")
    # calls the function to display the middle percentage
    # depending on the user's given mark
    percent = calc_mark(level_user)
    print(percent)


if __name__ == "__main__":
    main()
