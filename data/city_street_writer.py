import csv
import io

streetsReader = csv.reader(open("city_street_index.csv", "r"), delimiter=",")

"""
for row in streetsReader:
    print(", ".join(row))
"""

f = open("../htmls/city_street_index.html", "w")
# Start writing HTML.
f.write("<!DOCTYPE html>\n\n\
<html>\n\n\
<head>\n\
\t<meta charset=\"utf-8\">\n\
\t<meta name=\"description\" content=\"CSV with Python.\" />\n\
\t<meta name=\"author\" content=\"Jeremy's code.\" />\n\
\t<title>Streets</title>\n\
\t<link rel=\"stylesheet\" href=\"../css/style.css\" />\n\
\t<script src=\"../js/jquery.min.js\"></script>\n\
\t<script src=\"../js/outputready.js\"></script>\n\
\t<script src=\"../js/common.js\"></script>\n\
\t<script>\n\
\t\t//<![CDATA[\n\
\t\t$(document).ready(function() {\n\
\t\t\t//\n\
\t\t});\n\
\t\t//]]>\n\
\t</script>\n\
</head>\n\n\
<body>\n\
\t<div id=\"nav\">\n\
\t\t<select id=\"selNav\" name=\"selNav\">\n\
\t\t\t<option value=\"select\">- select destination -</option>\n\
\t\t\t<option value=\"county_index_map.html\">County Index Map</option>\n\
\t\t\t<option value=\"county_street_index.html\">County Street Index</option>\n\
\t\t\t<option value=\"city_street_index.html\">City Street Index</option>\n\
\t\t\t<option value=\"search.html\">Address Search</option>\n\
\t\t</select>\n\
\t</div>\n\
\t<p class=\"nav\">\n\
\t\t<a href=\"#A\">A</a> | \n\
\t\t<a href=\"#B\">B</a> | \n\
\t\t<a href=\"#C\">C</a> | \n\
\t\t<a href=\"#D\">D</a> | \n\
\t\t<a href=\"#E\">E</a> | \n\
\t\t<a href=\"#F\">F</a> | \n\
\t\t<a href=\"#G\">G</a> | \n\
\t\t<a href=\"#H\">H</a> | \n\
\t\t<a href=\"#I\">I</a> | \n\
\t\t<a href=\"#J\">J</a> | \n\
\t\t<a href=\"#K\">K</a> | \n\
\t\t<a href=\"#L\">L</a> | \n\
\t\t<a href=\"#M\">M</a> | \n\
\t\t<a href=\"#N\">N</a> | \n\
\t\t<a href=\"#O\">O</a> | \n\
\t\t<a href=\"#P\">P</a> | \n\
\t\t<a href=\"#Q\">Q</a> | \n\
\t\t<a href=\"#R\">R</a> | \n\
\t\t<a href=\"#S\">S</a> | \n\
\t\t<a href=\"#T\">T</a> | \n\
\t\t<a href=\"#U\">U</a> | \n\
\t\t<a href=\"#V\">V</a> | \n\
\t\t<a href=\"#W\">W</a> | \n\
\t\t<a href=\"#X\">X</a> | \n\
\t\t<a href=\"#Y\">Y</a> | \n\
\t\t<a href=\"#Z\">Z</a> \n\
\t</p>\n\
\t<table>\n")
# Write the table contents for each line of CSV.
rownum = 0
for row in streetsReader:
    if rownum == 0: # Write th row.
        f.write("\t\t<tr>\n")
        for column in row:
            f.write("\t\t\t<th>" + column + "</th>\n")
        f.write("\t\t</tr>\n")
    else: # Write other rows.
        colcount = len(row)
        if colcount == 1:
            f.write("\t\t<tr>\n")
            colnum = 0
            for column in row:
                if len(column) == 1:
                    colnum += 1
                    f.write("\t\t\t<td><a id=\"" + column + "\">" + column + "</a></td>\n\t\t\t<td><a href=\"#nav\">Go to nav</a></td>\n")
                else:
                    colnum += 1
                    if colnum == 1:
                        f.write("\t\t\t<td>" + column + "</td>\n")
                    elif colnum == 2:
                        f.write("\t\t\t<td><a href=\"jpeg.html?s=map" + column + "\">" + column + "</a></td>\n")
        elif colcount == 2:
            f.write("\t\t<tr>\n")
            colnum = 0
            for column in row:
                colnum += 1
                if colnum == 1:
                    f.write("\t\t\t<td>" + column + "</td>\n")
                elif colnum == 2:
                    f.write("\t\t\t<td><a href=\"jpeg.html?s=map" + column + "\">" + column + "</a></td>\n")                    
        f.write("\t\t</tr>\n")
    rownum += 1
f.write("\t</table>\n")
# Finish the HTML.
f.write("</body>\n\n</html>")
f.close()
print("finished")
