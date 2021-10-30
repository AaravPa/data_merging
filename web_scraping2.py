from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

df=pd.read_csv("/Users/Kartik/Downloads/datascience.csv")
data=list(df)

for planet_data in data:
    mass_data=planet_data[3]
    mass_value = mass_data.split(" ")[0]
    mass_value = float(mass_value) * 0.000954588
    mass_final_data=mass_value

    radius_data=planet_data[7]
    radius_value = radius_data.split(" ")[0]
    radius_value = float(radius_value) * 0.102763
    radius_final_data=radius_value

print(mass_final_data)
print(radius_final_data)
    

