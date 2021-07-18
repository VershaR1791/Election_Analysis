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

The input to the data is a combination of voting methods such as mail-in ballots, punch card, and direct recording electronic machines. The overall objective is to automate with help *Python* and help certify US Congresional race for Colorado Precint.

## Election-Audit Results 
The election-audit results for the Colorado Precint are as follows:
Using a bulleted list, address the following election outcomes. Use images or examples of your code as support where necessary.

- The total number of votes cast in this congressional election were **369,711**.
  
  This is achieved through a simple *for loop syntax* in python as seen in the snapshot below.
  
  ![Total_Votes_code](https://user-images.githubusercontent.com/84694664/126076827-c9cdbc3d-e46d-4609-b91e-1500b96fc269.JPG)

- The number of votes and the percentage of total votes for each county in the precinct are as seen in the below snapshot.

  ![County_Votes_result](https://user-images.githubusercontent.com/84694664/126076941-5807e529-1507-4ee1-a58a-d6674fd4336e.JPG)
  
  This result is obtained by creating a list to store *'county names'* and a dictionary to store *'county votes'*. The county names are extracted from each row and unique values are stored in the list and county votes are added against the name through a *if conditional statement*.
  
  ![County Votes_code](https://user-images.githubusercontent.com/84694664/126077155-47be7dac-b5f0-434b-84d5-abf97a27cfc6.JPG)

- The county with the largest voter turnout or number of votes was **Denver**.
  
  ![Votes_largest_county](https://user-images.githubusercontent.com/84694664/126077219-89f8b81c-a168-4c03-be6e-42560f979ab3.JPG)

  Denver's vote count and winning percentage was **306,055** and **82.8%** respectively.
  
  The syntax to create this summary is as follows:
  
  ![Winner County_vote](https://user-images.githubusercontent.com/84694664/126077282-221afd12-f670-4462-bdcb-1c4d79b472d2.JPG)

- The number of votes and the percentage of the total votes for each candidate are as follows:

  ![Candidate vote summary](https://user-images.githubusercontent.com/84694664/126077408-f38afc2e-e1a6-419d-a043-50866a006bd4.JPG)

  The syntax for the candidate summary is similar to the county summary:
  
  ![Candidate_summary_code](https://user-images.githubusercontent.com/84694664/126077447-2a85c4af-1a77-4762-9581-5b8f0229d30e.JPG)

- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?


## Election-Audit Summary
In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.
