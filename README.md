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

<li> Zach Non-Spatial Visualization </li>
This visualization is a simple bar chart that displays on the x-axis all of the different services offered by Zayo, and on the y-axis the number of each service provided to customers. I created a smaller csv file with all pertinent information to use as the dataset called ZayoHackathonData_Services_Cleanup. I viewed this visualization as important because it would allow Zayo to look at which services they are providing the most and least of to customers and take the proper steps into placing their resources into the right services and it would appear that Dark Fiber is the most popular service. The interactivity of this visualization is a hover feature that shows how many customers are receiving a service and what percentage of the total services are in a specific service. I used http://bl.ocks.org/d3noob/8952219 as a resource.

<li> Rachel Data Exploration Visualization </li>
This visualization is a way for the user to explore the data given by Zayo. This visualization uses Python and Bokeh (a python plotting library: http://bokeh.pydata.org/en/latest/). You can install Bokeh using Anaconda (conda install bokeh) or Pypi (pip install bokeh). Using the command line you can pass in any of the csv files provided and the program will launch a visualization that allows you to explore the different numerical data that is in each file. There is a selection box with which the user can choose which elements they want shown on the x and y axis. Bokeh then has some built in interactions that allow the user to pan and zoom to explore the data further and see if there are interesting patterns to investigate further.


<h2> Design Process </h2>
Our design process included exploratory data analysis in Tableau and Excel, in combination with interactions with the Zayo team. Because the Zayo team wanted to answer, largely open ended questions about the best places to expand markets, we designed visualizations with data exploration in mind. Both the spatial and non-spatial visualizations attempt to provide ways to interact with the data and identify markets that might be profitiable to expand into. 


<h2> Team Roles </h2>
All members were present for at least one day of brainstorming and discussion on visualization planning.
<li> Rachel : Created data exploration visualization.</li>
<li> Zachary : Created non spatial visualization of services Zayo offers</li>
<li> Ashlynn : Created spatial visualization. Dashboarded two visualizations. </li>
<li> Varsha : Created the interactive parallel coordinates plot. Cleaned data.</li>
<li> Tyler :  Created the README.md. </li>


<h2> How to run </h2>
Navigate to "project1-teamseven" folder and type in command "python -m SimpleHTTPServer 8000". Open web browser and go to "localhost:8000/index.html"
