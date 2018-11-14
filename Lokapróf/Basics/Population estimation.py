"""Assume that the current US population is 307,357,870
- a birth every 7 seconds
- a death every 13 seconds
- a new immigrant every 35 seconds
Write a program that takes years as input (as an integer) and prints
out estimated population (as integer).
Assume that there are exactly 365 days in a year."""

years = input("Input years: ")

years_int = int(years)

br = 1/7
dr = 1/13
im = 1/35

gr = br + im + dr

growth = gr * 60 * 60 * 24 *365 * years_int
new_pop = 307357870 + growth

print("New population after", years_int)