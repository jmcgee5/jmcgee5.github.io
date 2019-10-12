var tableData = data;
var tbody = d3.select("tbody");

//build the table using data
function buildTable(data) {
 // clear out the existing body
 tbody.html("");

 // Loop through data and append rows and cells for each value
 data.forEach((rows) => {
   // Append data rows to table
   var row = tbody.append("tr");

   // Loop through field in the rows and add each value as a table cell (td)
   Object.values(rows).forEach((val) => {
     var cell = row.append("td");
     cell.text(val);
   });
 });
}
// create filters for data
var filters = {};
function updateFilters() {

 //Capture new input entered
 var newInput = d3.select(this).select("input");
 var Value = newInput.property("value");
 var filterId = newInput.attr("id");

 // If a filter value was entered then add that filterId and value to the filters list. 
 //else clear filter from the filters object
 if (Value) {
   filters[filterId] = Value;
 }
 else {
   delete filters[filterId];
 }
 //function to apply filter
 filterTable_Data();
}
function filterTable_Data() {

 // Set the filteredData to the tableData
 let filteredData = tableData;

 // Loop through filter and keep any data matches the filter values
 Object.entries(filters).forEach(([key, value]) => {
   filteredData = filteredData.filter(row => row[key] === value);
 });

 // Change table witg filtered Data
 buildTable(filteredData);
}

// Event to listen for changes to each filter
d3.selectAll(".filter").on("change", updateFilters);

// Build the table when the page loads
buildTable(tableData);