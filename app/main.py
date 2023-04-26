import utils
import read_csv
import charts
import pandas as pd 

def run():
    """
    Traditional ways to create data filters
    
    data = list(filter(lambda item : item["Continent"] == "South America",data))

    countries = list(map(lambda x: x [],data))
    percentages = list(map(lambda x:x ["World Population Percentage"],data))
    
    """

    df = pd.read_csv("data.csv")
    df = df[df["Continent"] == "North America"]
    countries = df["Country"].values
    percentages = df["World Population Percentage"].values
    data = read_csv.read_csv("data.csv")
    charts.generate_pie_chart(countries, percentages)
    
if __name__ == "__main__":
    run()

