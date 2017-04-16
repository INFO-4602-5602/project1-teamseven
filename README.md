# Project1-teamseven
Project1-teamseven created by GitHub Classroom

<h2> Visualizations Information </h2>
<li> Non-Spatial Visualization: </li>


<li> Spatial Visualization: </li>
This visualizations uses [Highmaps](http://www.highcharts.com/products/highmaps) to show characteritistics of buildings that are not on the Zayo network. The hope is that this visualization could provide a method to explore characteristics of buildings that are not on the Zayo network (and are thus opportunities to expand Zayo). Data are from the Data_Buildings file and are colored by proximity to the network. Clicking on a color allows a user to filter by distance. The map is fully zoomable and panable. However, it is <it>quite<it> slow. Note: to combat this, we limit the number of points it shows to 1000, so that it renders. Tooltips on the points include the build cost and the type of network classification of the building. Points are labeled by the building ID.

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
