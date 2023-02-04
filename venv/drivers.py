import csv
import pickle
import pandas as pd


class Driver:
    def __init__(self, firstName, lastName, abbrev, nat, team, statRtg, statExp, statRac, statAwa, statPac):
        self.firstName = str(firstName)
        self.lastName = str(lastName)
        self.abbrev = str(abbrev)
        self.nat = str(nat)
        self.team = str(team)
        self.statRtg = int(statRtg)
        self.statExp = int(statExp)
        self.statRac = int(statRac)
        self.statAwa = int(statAwa)
        self.statPac = int(statPac)

# add driver manually
def addDriverManual():
    firstName = input("The first name of the drive is: ")
    lastName = input("The last name of" + firstName + "is: ")
    abbrev = input("What is the 3 letter abbreviation for " + firstName + " " + lastName + "?: ")
    nat = input("What is the nationality for " + abbrev + "?: ")
    team = input("What is the team for " + abbrev + "?: ")
    statRtg = input("What is the Rating for " + abbrev + "?: ")
    statExp = input("What is the Experince for " + abbrev + "?: ")
    statRac = input("What is the Racecraft for " + abbrev + "?: ")
    statAwa = input("What is the Awareness for " + abbrev + "?: ")
    statPac = input("What is the Pace for " + abbrev + "?: ")

    driver = Driver(firstName, lastName, abbrev, nat, team, statRtg, statExp, statRac, statAwa, statPac)

    return driver

# adds driver data from csv file
def autoDriverAuto(csv):

    # Creates column names for driver DF
    columnNames = ["firstName", "lastName", "abbrev", "nat", "team", "statRtg", "statExp", "statRac", "statAwa",
                   "statPac"]
    # Imports csv data with the correct column names
    drivers = pd.read_csv(csv, names=columnNames)


    # Strips whitespace from every data entry
    for i in drivers.columns:
        # checking datatype of each columns
        if drivers[i].dtype == 'object':
            # applying strip function on column
            drivers[i] = drivers[i].map(str.strip)
        else:
            # if condn. is False then it will do nothing.
            pass

    # creates driver list for driver objs to be added
    driverList = []
    x = 0
    y = len(drivers.index)
    driverNumber = 0

    # appends all driver data from driver DF to a list of driver objects
    while x < y:

        firstName = drivers.iloc[driverNumber, 0]
        lastName = drivers.iloc[driverNumber, 1]
        abbrev = drivers.iloc[driverNumber, 2]
        nat = drivers.iloc[driverNumber, 3]
        team = drivers.iloc[driverNumber, 4]
        statRtg = drivers.iloc[driverNumber, 5]
        statExp = drivers.iloc[driverNumber, 6]
        statRac = drivers.iloc[driverNumber, 7]
        statAwa = drivers.iloc[driverNumber, 8]
        statPac = drivers.iloc[driverNumber, 9]

        obj = Driver(firstName, lastName, abbrev, nat, team, statRtg, statExp, statRac, statAwa, statPac)

        driverList.append(obj)

        x += 1
        driverNumber += 1

    return driverList

# Shows all current drivers in list
def showAllDrivers(list):

    for x in list:
        print(x.firstName + " " + x.lastName + " " + x.abbrev + " " + x.nat + " " + x.team + " " + str(x.statRtg)
              + " " + str(x.statExp) + " " + str(x.statRac) + " " + str(x.statAwa) + " " + str(x.statPac))

