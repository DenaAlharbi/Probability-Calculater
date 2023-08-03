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


class Inputs:

    def specificColorNum(self):
        global red_user # one color only
        one_specific_color = input(
            "What is the color you want to find the probability of?\n 'red' or 'blue' or 'green':")
        if one_specific_color == "red":
            return red()
        if one_specific_color == "blue":
            return blue()
        if one_specific_color == "green":
            return green()

    def numToCalculate(self):
        num_balls_col = input("How many balls of that color do you want to take out?")
        return num_balls_col

    def Validate(self,x):
        if x.isspace():
            return False
        if x.isdigit():
            return False
        if not (x == "yes" or x == "no"):
            return False
        return True

    def red(self):
        red_user = input("How many red balls are there in your imaginary hat? ")
        red_user = int(red_user)
        return red_user

    def blue(self):
        blue_user = input("How many blue balls are there in your imaginary hat? ")
        blue_user = int(blue_user)
        return blue_user

    def green(self):
        green_user = input("How many green balls are there in your imaginary hat? ")
        green_user = int(green_user)
        return green_user

    def numOfBallsTake(self):  # That the user is going to take out
        num_balls_take = input("How many balls do you want to take out? ")
        num_balls_take = int(num_balls_take)
        return num_balls_take

    def total(self,col_red, col_blue, col_green):
        total_of_balls = col_red + col_blue + col_green
        return total_of_balls


def main():
    objectA = Inputs
    objectB = Object
    firstInput = input("Do you want to play the probability game? 'yes' or 'no': ")
    while firstInput != "":
        if objectA.Validate(firstInput):
            objectB.oneColor(objectA.total(objectA.red(), objectA.blue(), objectA.green()), objectA.numOfBallsTake(), specificColorNum(), numToCalculate())

        elif firstInput == "":
            print("The program will stop now...")
            break
        firstInput = input("Do you want to play the probability game? 'yes' or 'no': ")


pass

main()
