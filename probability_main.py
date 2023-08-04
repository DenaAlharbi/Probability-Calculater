# Give the user the freedom of choosing the num of balls for each color
# Validate the input
# How many balls do you want to pick from the hat?
# And what distribution of colors are you interested in?
import math
import pandas as pd
import numpy as np
import scipy.stats


class Object:

    def __init__(self):
        pass

    # This is if the user wants to choose just one color
    def oneColor(self, total_balls, numTake, color_num_balls, numCalculate):
        the_calculation1 = scipy.stats.binom.pmf(numCalculate, numTake, color_num_balls / total_balls)

    # def balance_update(self):
    # infile = open("record.txt", "w")
    # infile.write(f"\n")
    # infile.close()


def Validate(x):
    if x.isspace():
        return False
    if x.isdigit():
        return False
    if not (x == "yes" or x == "no"):
        return False
    return True


class Inputs:

    def __init__(self):
        self.num_balls_take = None
        self.green_user = None
        self.blue_user = None
        self.red_user = None
        self.num_balls_col = None
        self.total_of_balls = None

    def specificColorNum(self):
        one_specific_color = input(
            "What is the color you want to find the probability of?\n 'red' or 'blue' or 'green':")
        if one_specific_color == "red":
            return self.red_user
        if one_specific_color == "blue":
            return self.red_user
        if one_specific_color == "green":
            return self.green_user

    def numToCalculate(self):
        self.num_balls_col = input("How many balls of that color do you want to take out?")
        return self.num_balls_col

    def red(self):
        self.red_user = input("How many red balls are there in your imaginary hat? ")
        self.red_user = int(self.red_user)
        return self.red_user

    def blue(self):
        self.blue_user = input("How many blue balls are there in your imaginary hat? ")
        self.blue_user = int(self.blue_user)
        return self.blue_user

    def green(self):
        self.green_user = input("How many green balls are there in your imaginary hat? ")
        self.green_user = int(self.green_user)
        return self.green_user

    def numOfBallsTake(self):  # That the user is going to take out
        self.num_balls_take = input("How many balls do you want to take out? ")
        self.num_balls_take = int(self.num_balls_take)
        return self.num_balls_take

    def total(self, col_red, col_blue, col_green):
        self.total_of_balls = col_red + col_blue + col_green
        return self.total_of_balls


def main():
    objectA = Inputs
    objectB = Object
    firstInput = input("Do you want to play the probability game? 'yes' or 'no': ")
    while firstInput != "":
        if Validate(firstInput):
            objectB.oneColor(objectA.total(objectA.red(), objectA.blue(), objectA.green()), objectA.numOfBallsTake(),
                             objectA.specificColorNum(), objectA.numToCalculate())

        elif firstInput == "":
            print("The program will stop now...")
            break
        firstInput = input("Do you want to play the probability game? 'yes' or 'no': ")


main()
