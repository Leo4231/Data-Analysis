# Analyzes overall trend of road vehicles for traffic applications
# Based on data updated till year 2020. Reference csv file: annual-motor-vehicle-population-by-vehicle-type.csv
# libraries used: pandas, matplotlib

import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("annual-motor-vehicle-population-by-vehicle-type.csv")
year = df["year"].tolist()
val1 = df.loc[df["type"]=="Private cars"].index
val2 = df.loc[df["type"]=="Taxis"].index
val3 = df.loc[df["type"]=="Motorcycles and Scooters"].index
val4 = df.loc[df["type"]=="Private Hire (Chauffeur) cars"].index
val5 = df.loc[df["type"]=="Light Goods Vehicles (LGVs)"].index
List1 = df.loc[val1]
List2 = df.loc[val2]
List3 = df.loc[val3]
List4 = df.loc[val4]
List5 = df.loc[val5]
plt.plot(List1["year"], List1["number"], label = "Number of Private Cars")
plt.plot(List2["year"], List2["number"], label = "Number of Taxis")
plt.plot(List3["year"], List3["number"], label = "Number of Motorcycles and Scooters")
plt.plot(List4["year"], List4["number"], label = "Number of Private Hire (Chauffeur) cars")
plt.plot(List5["year"], List5["number"], label = "Number of Light Goods Vehicles (LGVs)")
plt.xlabel("Year")
plt.ylabel("Number of vehicles")
plt.xticks(List1["year"])
plt.title("Selected number of vehicles over the years")
plt.legend()
plt.show()