"""
Author: Andrei Benea
Date: 6/5/2024
Assignment: M01 Practice Programming Exercise 2-2
This program prompts the user for a number (edge[int]), calculates the surface
area of the cube having that edge, then prints the resulting value.
"""

edge = int(input("Type in a number to represent the edge of a cube: ")) #gets input and transform it to int

surface_area = 6 * edge**2 #calculates surface area using formula

print("The cube's surface area is", surface_area) #prints the result