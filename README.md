# Project1-teamseven
Project1-teamseven created by GitHub Classroom

<h2> Visualizations Information </h2>
<li> Parallel Coordinates plot Visualization: </li>
The Parallel visualization depicts the ratio of the total annual revenue for each Vertical i.e each sub-sector and annual cost that occurs for that sector both recurring and non-recurring. 

The visualization is based on the data present in the below files.
1. ZayoHackathonData_Accounts.csv
2. ZayoHackathonData_CPQs.csv


As the annual revenue values of the Vertical is widely distributed, log scale has been chosen so that the lesser values are also easily located. 

The color of the lines connecting the vertical, annual revenue and total cost depicts the Industry. 

The visualization is provided with the feature where they can filter out the data based on whether to include the companies in On Zayo Network and others.


Technologies Used: 

1. HTML
2. CSS
3. D3
4. Python

References: 

http://alignedleft.com/tutorials/d3
https://d3js.org/


<li> Spatial Visualization: </li>
This visualization uses [Highmaps](http://www.highcharts.com/products/highmaps) to show characteritistics of buildings that are not on the Zayo network. The hope is that this visualization could provide a method to explore characteristics of buildings that are not on the Zayo network (and are thus opportunities to expand Zayo). Data are from the Data_Buildings file and are colored by proximity to the network. Clicking on a color allows a user to filter by distance. The map is fully zoomable and panable. However, it is *quite* slow. Note: to combat this, we limit the number of points it shows to 1000, so that it renders. Tooltips on the points include the build cost and the type of network classification of the building. Points are labeled by the building ID. Of note, I (Ashlynn) spent a fairly substantial amount of time trying to build a similar map in D3, but had a difficult time finding compatibility between functions in v3 and v4. As such, I switched over to highmaps, which turns out to be fairly easy to use and customize (except for the fact that it becomes slow quickly).

<li> Third Visualization: </li>


<h2> Design Process </h2>
Our design process included exploratory data analysis in Tableau and Excel, in combination with interactions with the Zayo team. Because the Zayo team wanted to answer, largely open ended questions about the bst places to expand markets, we designed visualizations with data exploration in mind. Both the spatial and non-spatial visualizations attempt to provide ways to interact with the data and identify markets that might be profitiable to expand into. 


<h2> Team Roles </h2>
All members were present for at least one day of brainstorming and discussion on visualization planning.
<li> Rachel : </li>
<li> Zachary : </li>
<li> Ashlynn : Created spatial visualization. Dashboarded two visualizations. </li>
<li> Varsha : Created the interactive parallel coordinates plot. Cleaned data.</li>
<li> Tyler :  Created the README.md. </li>


<h2> How to run </h2>
Navigate to "project1-teamseven" folder and type in command "python -m SimpleHTTPServer 8000". Open web browser and go to "localhost:8000/index.html"
