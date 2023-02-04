from Scripts import drivers as dr

class team:
    def __init__(self, name, drivers):
        self.name = name
        self.drivers = drivers



def createTeams(driverList):
    x = 0
    teamList = []
    for d in driverList:

        if d.team not in teamList

            teamList.append(team(str(d.team), d))


            print(len(teamList))
            driverList.remove(d)




    for i in teamList:

        print(teamList[x].driver1.firstName + " " + teamList[x].driver1.team +
              teamList[x].driver2.firstName + teamList[x].name)
        x += 1











# def driverTeamMatch(driverList, teamListInput):
#     teamListOutput = []
#     driverPair = []
#     for d in driverList:
#         for t in teamListInput:
#             if d.team == t and len(driverPair) == 0:
#                 driverPair.append(d)
#                 driverList.remove(d)
#                 print(driverPair[0].abbrev + driverPair[0].team)
#                 break
#             elif d.team == t and driverPair[0].team == d.team:
#                 driverPair.append(d)
#                 driverList.remove(d)
#                 print(driverPair[1].abbrev + driverPair[1].team)
#
#                 if driverPair[0].statRtg > driverPair[1].statRtg:
#                     d1 = driverPair[0]
#                     d2 = driverPair[1]
#                 else:
#                     d1 = driverPair[1]
#                     d2 = driverPair[0]
#
#                 print(d1.abbrev)
#                 print(d2.abbrev)
#
#                 teamListOutput.append(team(t, d1, d2))
#
#                 print(len(teamListOutput))
#
#                 driverPair = []
#                 break


    # for t in teamListOutput:
    #     d1 = t.driver1
    #     d2 = t.driver2
    #     if d1.statRtg > d2.st

def showAllTeams(list):
    for x in list:
        print(x.name + " " + x.driver1.lastName + " " + x.driver2.lastName)