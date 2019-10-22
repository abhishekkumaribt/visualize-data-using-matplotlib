# --------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

electors_2009 = pd.read_csv(path)
candidate_2009 = pd.read_csv(path1)

# Plot a bar chart to compare the number of male and female candidates in the election
candidate_2009.Candidate_Sex.value_counts().plot(kind="bar")
# Plot a histogram of the age of all the candidates as well as of the winner amongst them. Compare them and note an observation
candidate_2009.Candidate_Age.plot(kind="hist")
for age in candidate_2009[candidate_2009.Position==1]["Candidate_Age"]:
    plt.axvline(age, color='red', linewidth=1)
# Plot a bar graph to get the vote shares of different parties
candidate_2009.groupby("Party_Abbreviation")[["Total_Votes_Polled"]].sum().plot(kind="bar", figsize=[100,20])
# Plot a barplot to compare the mean poll percentage of all the states
electors_2009.groupby(by="STATE")["POLL PERCENTAGE"].mean().plot(kind="bar",figsize=[20, 10])
# Plot a bar plot to compare the seats won by different parties in Uttar Pradesh
candidate_2009[(candidate_2009.State_name=="Uttar Pradesh") & (candidate_2009.Position==1)].groupby("Party_Abbreviation")[["Position"]].count().plot(kind="bar")
# Plot a stacked bar chart to compare the number of seats won by different `Alliances` in Gujarat,Madhya Pradesh and Maharashtra. 
win = candidate_2009[((candidate_2009.State_name=="Madhya Pradesh")|(candidate_2009.State_name=="Gujarat")|(candidate_2009.State_name=="Maharashtra")) & (candidate_2009.Position==1)]
win.pivot_table(index="Alliance", columns="State_name", aggfunc="count", values="Position").plot(kind="bar", stacked=True)
# Plot a grouped bar chart to compare the number of winner candidates on the basis of their caste in the states of Andhra Pradesh, Kerala, Tamil Nadu and Karnataka
win = candidate_2009[((candidate_2009.State_name=="Andhra Pradesh")|(candidate_2009.State_name=="Kerala")|(candidate_2009.State_name=="Tamil Nadu")|(candidate_2009.State_name=="Karnataka")) & (candidate_2009.Position==1)]
win.pivot_table(index="Candidate_Category", columns="State_name", aggfunc="count", values="Position").plot(kind="bar", figsize=[20,10])
# Plot a horizontal bar graph of the Parliamentary constituency with total voters less than 100000
less = electors_2009[electors_2009.Total_Electors<100000]
less.index = less.STATE
less = less[["Total_Electors"]]
less.plot(kind="barh")
# Plot a pie chart with the top 10 parties with majority seats in the elections
top_10 = candidate_2009[candidate_2009.Position==1].groupby("Party_Abbreviation")[["Position"]].count().sort_values(by="Position", ascending=False).head(10)
plt.pie(top_10, labels=top_10.index)
# Plot a pie diagram for top 9 states with most number of seats
top_9 = candidate_2009[["State_name", "PC_name"]].drop_duplicates().groupby("State_name").count().sort_values("PC_name", ascending=False).head(9)
plt.pie(top_9, labels=top_9.index)



