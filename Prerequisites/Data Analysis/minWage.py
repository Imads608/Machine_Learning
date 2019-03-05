import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests


def convertFile():
    df = pd.read_csv("datasets/Minimum Wage Data.csv", encoding="latin")
    df.to_csv("datasets/minWageUTF8.csv", encoding="utf-8")

def analysis():
    df = pd.read_csv("datasets/minWageUTF8.csv", encoding="utf-8")
    gb = df.groupby("State")
    print(gb.get_group("Alabama").set_index("Year").head())

    act_min_wage = pd.DataFrame()

    for name, group in df.groupby("State"):
        if (act_min_wage.empty):
            act_min_wage = group.set_index("Year")[["Low.2018"]].rename(columns={"Low.2018":name})
        else:
            act_min_wage = act_min_wage.join(group.set_index("Year")[["Low.2018"]].rename(columns={"Low.2018":name}))
    print(act_min_wage.corr())

    issue_df = df[df["Low.2018"] == 0.0]
    print(issue_df["State"].unique())
    min_wage_corr = act_min_wage.replace(0, np.NaN).dropna(axis=1).corr().head()

    for problem in issue_df["State"].unique():
        if (problem in min_wage_corr.columns):
            print("Something is missing here")

    grouped_issues = issue_df.groupby("State")
    print(grouped_issues.head())
    print(grouped_issues.get_group("Alabama")["Low.2018"].sum())

    for state, data in grouped_issues:
        if (data["Low.2018"].sum() != 0.0):
            print("Some data found for " + state)

def analysis2():
    df = pd.read_csv("datasets/minWageUTF8.csv")
    act_min_wage = pd.DataFrame()

    for name, group in df.groupby("State"):
        if act_min_wage.empty:
            act_min_wage = group.set_index("Year")[["Low.2018"]].rename(columns={"Low.2018": name})
        else:
            act_min_wage = act_min_wage.join(group.set_index("Year")[["Low.2018"]].rename(columns={"Low.2018": name}))

    min_wage_corr = act_min_wage.replace(0, np.NaN).dropna(axis=1).corr()

    labels = [c[:2] for c in min_wage_corr]
    fig = plt.figure(figsize=(12,12))
    ax = fig.add_subplot(111)
    ax.matshow(min_wage_corr, cmap=plt.cm.RdYlGn)
    ax.set_xticks(np.arange(len(labels)))
    ax.set_yticks(np.arange(len(labels)))
    ax.set_xticklabels(labels)
    ax.set_yticklabels(labels)

    web = requests.get("https://www.infoplease.com/state-abbreviations-and-state-postal-codes")
    dfs = pd.read_html(web.text)

    state_abbv = dfs[0]
    print(state_abbv[["State/District", "Postal Code"]])
    state_abbv[["State/District", "Postal Code"]].to_csv("datasets/state_abbv.csv", index=False)  # index in this case is worthless
    #state_abbv.to_csv("datasets/state_abbv.csv", index=False)
    state_abbv = pd.read_csv("datasets/state_abbv.csv", index_col=0)
    abbv_dict = state_abbv.to_dict()
    abbv_dict = abbv_dict.get("Postal Code")
    abbv_dict['Federal (FLSA)'] = "FLSA"
    abbv_dict['Guam'] = "GU"
    abbv_dict['Puerto Rico'] = "PR"
    labels = [abbv_dict[c] for c in min_wage_corr.columns]  # get abbv state names.

    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(111)
    ax.matshow(min_wage_corr, cmap=plt.cm.RdYlGn)
    ax.set_xticks(np.arange(len(labels)))
    ax.set_yticks(np.arange(len(labels)))
    ax.set_xticklabels(labels)
    ax.set_yticklabels(labels)
    plt.show()

if __name__ == "__main__":
    convertFile()
    analysis2()