Emergency Responders Mapbook
============================

Background
----------

Emergency response personnel (e.g., ambulance drivers or police officers) were navigating the county with a massive printed tome of paper maps.  This application gives them an electronic equivalent that allows them to find addresses more quickly and easily.  One of the biggest (and most fun) challenges so far has been the need to create a web application that can run 100% locally on the device (we use it on an iPad) without needing any network connection.  

Components
----------

The components of the application are separated into different folders.

### CSS

This folder obviously just holds the CSS files for the web pages.

### Data

This folder contains CSV files and Python scripts.  The CSV files are produced with ESRI ArcMap.  The Python scripts read the CSV files and write them into HTML and JavaScript files.  In our implementation of the application, the end user does not need any interaction with these files.  They are simply there to update data when we push out a new version.

### HTMLs

This is where all of the HTML files for the web application live.  They're all static HTML files because the application needs to run in an environment without server-side processing.

### JPEGs

The JPEGs folder contains the images required for the project.  There are two folders: one for index maps and one for the mapbook pages themselves.  These JPEGs are exported from ArcMap with a Python script.  Here on GitHub we have only included a subset of the images to be respectful of storage concerns.

### JS

The JS folder contains the JavaScript files necessary to run the application.  This includes the jQuery library, general scripts to run the web pages, and the data needed for the address search.

How It Works
------------

### Displaying Mapbook Pages

Basically, any requested mapbook page is handled by jpeg.html.  The file name of the map is passed in the URL like this:

> jpeg.html?s=map12

### Searching Addresses

The address search uses an associate array to match addresses as output from ArcMap with mapbook page numbers.  Basically, the value of the search box is passed as a value for the array.  Simplified example:

> var search = $("#txtAddress").val();

> var result = address[search];

We use the associative array approach because it runs right inside the browser as long as JavaScript is supported and it is much faster than other options we tried (e.g., jQuery plugins for searching tables).

Deployment
----------

Here at Frederick County, we use the mapbook on iPads with an app called GoodReader.  It is simple to download new versions of the mapbook to the iPad (since we cannot simply access the file system on iOS) and then run the files locally inside GoodReader.  In tests on Android devices, we were able to run the mapbook locally in a web browser by storing it on an SD card.

Credit Is Due
-------------

The original inspiration for this project came from a similar application used by Page County, VA.  Lindsey Felton is responsible for maps and project guidance.  Scripting and pretentious HTML compliance is by Jeremy Coulson.


