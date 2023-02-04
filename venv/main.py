from Scripts import drivers as dr
from Scripts import teams as tm


driverList = dr.autoDriverAuto("drivers.csv")
teamListName = ["Ferrari", "Mercades", "McLaren", "Alpine", "Red Bull", "Alfa Romeo", "Aston Martin", "Williams", "Haas", "Alfa Tauri"]

dr.showAllDrivers(driverList)


tm.createTeams(driverList)





