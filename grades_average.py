#!/usr/bin/env python3

# Created by Samuel Webster
# Created on March 2022
# This program calculates the circumference of a circle
#     with inputted radius


def find_average(grades=[]):
    total = 0
    for grade in grades:
        total += grade
    average = total / len(grades)
    return average


def main():
    # I calculate circumference

    # process
    grades_list = []
    while True:
        str_grade = input("Input grade: ")
        try:
            int_grade = int(str_grade)
            if int_grade == -1:
                break
            elif int_grade <= 100 and int_grade >= 0:
                grades_list.append(int_grade)
            else:
                raise Exception("Error")
        except Exception:
            print("Invalid Input")

    # call functions
    average = find_average(grades_list)

    # output
    print("\nThe average is {}.".format(average))
    print("\nDone.")


if __name__ == "__main__":
    main()
