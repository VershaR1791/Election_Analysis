# Election_Analysis
Perform an audit to determine election results of Colorado US Precinct using Python
## Overview of Election Audit 
The Colorado Board of Election Employee Tom has seeked assistance to help audit the election data for US Congressional Precint Election in Colorado. The output of the election will require determining -
- the total number of votes cast, 
- the number of votes case per county,
- largest county turnout,
- the number of votes cast per candidate, 
- the % of votes cast per candidate and,
- finally, the winner of election based on popular vote. 

The input data is a combination of voting methods such as mail-in ballots, punch card, and direct recording electronic machines. The overall objective is to automate with help *Python* and help certify US Congresional race for Colorado Precint.

## Election-Audit Results 
The 'election results' excel file contains data of 3 counties *'Arapahoe', 'Denver'* and *'Jefferson'* and candidates *'Charles Casper Stockham', 'Diana DeGette'* and *'Raymon Anthony Doane'*. The election-audit results for the Colorado Precint are as follows:

- The total number of votes cast in this congressional election were **369,711**. This is achieved through a simple *'for loop syntax'* in python as seen in the snapshot below.
  
  ![Total_Votes_code](https://user-images.githubusercontent.com/84694664/126076827-c9cdbc3d-e46d-4609-b91e-1500b96fc269.JPG)

- The number of votes and the percentage of total votes for each county in the precinct are as seen in the below snapshot.

  ![County_Votes_result](https://user-images.githubusercontent.com/84694664/126076941-5807e529-1507-4ee1-a58a-d6674fd4336e.JPG)
  
  This result is obtained by creating a list to store *'county names'* and a dictionary to store *'county votes'*. The county names are extracted from each row and unique values are stored in the list and county votes are added against the name through a *if conditional statement*.
  
  ![County Votes_code](https://user-images.githubusercontent.com/84694664/126077155-47be7dac-b5f0-434b-84d5-abf97a27cfc6.JPG)

- The county with the largest voter turnout or number of votes was **Denver**. Denver's vote count and winning percentage was **306,055** and **82.8%** respectively.
  
  The syntax to create this summary is as follows:
  
  ![Winner County_vote](https://user-images.githubusercontent.com/84694664/126077282-221afd12-f670-4462-bdcb-1c4d79b472d2.JPG)

- The number of votes and the percentage of the total votes for each candidate are as follows:

  ![Candidate vote summary](https://user-images.githubusercontent.com/84694664/126077408-f38afc2e-e1a6-419d-a043-50866a006bd4.JPG)

  The syntax for the candidate summary is similar to the county summary syntax:
  
  ![Candidate_summary_code](https://user-images.githubusercontent.com/84694664/126077447-2a85c4af-1a77-4762-9581-5b8f0229d30e.JPG)

- **Diana DeGette** won the election with an outstanding vote count of **272,892**. She beat the other 2 candidates by a large margin of **73.8%**.
  
  ![winning_candidate_summary](https://user-images.githubusercontent.com/84694664/126078561-1fc8db25-06bd-4e63-9ffb-fce5fb37a91d.JPG)

## Election-Audit Summary
The benefit of performing this election analysis through python is that it can be modified slightly to be used for similar analysis for any other precint or for gathering additional insights.
- If we would like to create an analysis for a the entire state, we can create additional *list* for state and a *dictionary* to store the state votes. New variables to store the winner data such as name, vote count and percentage can be created. Using the *if conditional statement* we can store the unique counties within the state and calculate the vote for the counties and candidates. Again using *if statement* and *comparison operator* we can determine the winning state.
- If we have the population data of county or state, additional analysis can be carried out to see the voter turnout for each county and state. Firstly, the population data can be stored into a variable and using a simple division operator the % voter turnout can be found out. The candidates as well as the election commission board can strategize the campaigning plan for the next election usinh this data especially in the low turnout county or state.
