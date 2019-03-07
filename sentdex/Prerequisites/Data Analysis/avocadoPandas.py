import pandas as pd
import matplotlib.pyplot as plt

def part1():
    df = pd.read_csv("datasets/avocado.csv")
    print(df.head())
    print(df["AveragePrice"].head())
    albany_df = df[df["region"] == "Albany"]
    print(albany_df.head())
    print(albany_df.index)
    albany_df.set_index("Date", inplace=True)
    print(albany_df.head())
    albany_df["AveragePrice"].plot()
    plt.show()

def part2():
    df = pd.read_csv("datasets/avocado.csv")

    albany_df = df.copy()[df["region"] == "Albany"]
    albany_df.set_index("Date", inplace = True)
    albany_df.sort_index(inplace=True)
    albany_df["price25ma"] = albany_df["AveragePrice"].rolling(25).mean()
    #print(albany_df.head(30))


    df = df.copy()[df['type'] == 'organic']
    graph_df = pd.DataFrame()
    for region in df["region"].unique():
        region_df = df.copy()[df["region"] == region]
        region_df.set_index("Date", inplace=True)
        region_df.sort_index(inplace=True)
        strColName = region + "_price25ma"
        region_df[strColName] = region_df["AveragePrice"].rolling(25).mean()
        if (graph_df.empty):
            graph_df = region_df[[strColName]]
        else:
            graph_df = graph_df.join(region_df[strColName])
    #graph_df.dropna().plot(figsize=(8, 5), legend=False)
    #plt.show()
    print(df["region"])
if __name__ == "__main__":
    part2()