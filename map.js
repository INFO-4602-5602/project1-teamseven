// help from http://bl.ocks.org/michellechandra/0b2ce4923dc9b5809922



var width = 960;
var height = 500;
var on_zayo = "On Zayo Network";
var not_on_zayo = "Not on Zayo Network";



// D3 Projection
var projection = d3.geo.albersUsa()
                        // translate to center of screen
                       .translate([width/2, height/2])
                        // scale things down so see entire US
                       .scale([1000]);

// Define path generator
// path generator that will convert GeoJSON to SVG paths
var path = d3.geo.path()
                 .projection(projection);


// Define linear scale for output
var color = d3.scale.quantize()
.range(["rgb(237,248,233)","rgb(186,228,179)","rgb(116,196,118)","rgb(49,163,84)","rgb(0,109,44)"]);


var x = d3.scale.linear()
    .domain([1, 10])
    .rangeRound([600, 860]);


//Create SVG element and append map to the SVG
var svg = d3.select("body")
            .append("svg")
            .attr("width", width)
            .attr("height", height);

// add the key
var g = svg.append("g")
    .attr("class", "key")
    .attr("transform", "translate(0,40)");

g.selectAll("rect")
  .data(color.range().map(function(d) {
      d = color.invertExtent(d);
      if (d[0] == null) d[0] = x.domain()[0];
      if (d[1] == null) d[1] = x.domain()[1];
      return d;
    }))
  .enter().append("rect")
    .attr("height", 20)
    .attr("x", function(d) {  return x(d[0]); })
    .attr("width", function(d) {  return x(d[1]) - x(d[0]); })
    .attr("fill", function(d) { return color(d[0]); });

g.append("text")
    .attr("class", "caption")
    .attr("x", x.range()[0])
    .attr("y", -6)
    .attr("fill", "#000")
    .attr("text-anchor", "start")
    .attr("font-weight", "bold")
    .text("Key");

g.call(d3.svg.axis(x)
    .tickSize(13)
    .tickValues(color.domain()))
  .select(".domain")
    .remove();

// Append Div for tooltip to SVG
var div = d3.select("body")
             .append("div")
             .attr("class", "tooltip")
             .style("opacity", 0);


// convert from state abbreviation to state name
var states_array = {
    "AL": "Alabama",
    "AK": "Alaska",
    "AS": "American Samoa",
    "AZ": "Arizona",
    "AR": "Arkansas",
    "CA": "California",
    "CO": "Colorado",
    "CT": "Connecticut",
    "DE": "Delaware",
    "DC": "District Of Columbia",
    "FM": "Federated States Of Micronesia",
    "FL": "Florida",
    "GA": "Georgia",
    "GU": "Guam",
    "HI": "Hawaii",
    "ID": "Idaho",
    "IL": "Illinois",
    "IN": "Indiana",
    "IA": "Iowa",
    "KS": "Kansas",
    "KY": "Kentucky",
    "LA": "Louisiana",
    "ME": "Maine",
    "MH": "Marshall Islands",
    "MD": "Maryland",
    "MA": "Massachusetts",
    "MI": "Michigan",
    "MN": "Minnesota",
    "MS": "Mississippi",
    "MO": "Missouri",
    "MT": "Montana",
    "NE": "Nebraska",
    "NV": "Nevada",
    "NH": "New Hampshire",
    "NJ": "New Jersey",
    "NM": "New Mexico",
    "NY": "New York",
    "NC": "North Carolina",
    "ND": "North Dakota",
    "MP": "Northern Mariana Islands",
    "OH": "Ohio",
    "OK": "Oklahoma",
    "OR": "Oregon",
    "PW": "Palau",
    "PA": "Pennsylvania",
    "PR": "Puerto Rico",
    "RI": "Rhode Island",
    "SC": "South Carolina",
    "SD": "South Dakota",
    "TN": "Tennessee",
    "TX": "Texas",
    "UT": "Utah",
    "VT": "Vermont",
    "VI": "Virgin Islands",
    "VA": "Virginia",
    "WA": "Washington",
    "WV": "West Virginia",
    "WI": "Wisconsin",
    "WY": "Wyoming"
}

function map (menu){
   if (menu===''){
      console.log('default');
      menu = 'On Zayo Network';
   }
   d3.csv("../data/ZayoHackathonData_Sites.csv", function(data) {
       console.log('menu', menu);
       var onZayo = {};
       $.each(data, function (i){
              if (data[i]['On Zayo Network Status']===menu){
                   if (data[i]['State'] in onZayo){
                      onZayo[data[i]['State']] +=1;
                   } else {
                      onZayo[data[i]['State']]= 1
                   }
              }
          });;
          //console.log(onZayo);
          color.domain([ d3.min(d3.values(onZayo)),
                         d3.max(d3.values(onZayo))
          ]);
          //console.log(color.domain());
    // Load GeoJSON data and merge with states data
    d3.json('../data/usa_data.json', function(json) {
    // Loop through each state data value in the onZayo object
       //console.log(onZayo);
       for (var i = 0; i < Object.keys(onZayo).length; i++) {
         keys = Object.keys(onZayo);
         // Grab State Name
         var dataState = states_array[keys[i]];
         // Grab data value
         var dataValue = onZayo[keys[i]];
         // Find the corresponding state inside the GeoJSON
         for (var j = 0; j < json.features.length; j++)  {
             var jsonState = json.features[j].properties.name;
             if (dataState === jsonState) {
                // Copy the data value into the JSON
                 json.features[j].properties.onZayo = dataValue;
                 //console.log(json.features[j]);
                // Stop looking through the JSON
                break;
             }
      }
   }
   // Bind the data to the SVG and create one path per GeoJSON feature
   svg.selectAll("path")
      .data(json.features)
      .style("fill", function(d) {
            // Get data value
            var value = d.properties.onZayo;
            if (value) {
            //If value exists…
            return color(value);
            } else {
            //If value is undefined…
            return "rgb(213,222,217)";
            }
         })
      .enter()
      .append("path")
      .attr("d", path)
      .style("stroke", "#fff")
      .style("stroke-width", "1")
        .on("mouseover", function(d) {
             div.transition()
                  .duration(200)
                  .style("opacity", .9);
                 div.text(d.properties.onZayo)
                    .style("left", (d3.event.pageX) + "px")
                    .style("top", (d3.event.pageY - 28) + "px");
   });
});

});

}

map('On Zayo Network');
