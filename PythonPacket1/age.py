from argparse import ArgumentDefaultsHelpFormatter


ageInput = int(input("Input your age in years"))

ageDecade = ageInput / 10
ageWeek = ageInput * (365/7)
ageDay = ageInput * 365

print("You have been alive for {} days, {} weeks, {} years, and {} decades.".format(ageDay, ageWeek, ageInput, ageDecade))