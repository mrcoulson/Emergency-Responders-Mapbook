from datetime import datetime
import csv

# Open the files I need.
with open("county_addresses_search.csv", "r") as infile:
    with open("../js/array.js", "w") as outfile:

        data = ""
        rowcount = 0
        for row in csv.reader(infile):
            # Add the row's data to a string object.
            data += "address[\"" + row[0] + "\"] = \"" + row[1] + "\";\n"
            # Increment rowcount by 1.
            rowcount += 1

        # Write stuff into the JS file.
        outfile.write("// Written: " + str(datetime.now()) + "\n\n")
        outfile.write("var address = new Array();\n\n")
        outfile.write(data)
        outfile.write("\n\n// End.\n")

        # Show success and number of records written.
        print("Finished. " + str(rowcount) + " records written.")


# Code above as inspired by https://github.com/jcarbaugh.
# Code below is what I wrote first.

"""
import csv
import io
import datetime

# Get the datetime.
now = datetime.datetime.now()

# Swap the abridged CSV in for testing.
# Create an object to hold CSV data.
addressReader = csv.reader(open("addresses.csv", "r"), delimiter=",")
# Get and print number of rows just to see how many were processed.
rowcount =  len(open("addresses.csv").readlines())
print(rowcount)

# Create an object for writing.
f = open("../js/array.js", "w")
# Timestamp.
f.write("// Written: " + str(now) + "\n\n")
# Create the array.
f.write("var address = new Array();\n\n")
# Fill the array for each line of CSV.
for row in addressReader:
    f.write("address[\"")
    colnum = 0
    for column in row:
        colnum += 1
        if (colnum == 1):
            f.write(column + "\"] = \"")
        elif (colnum == 2):
            f.write(column + "\";\n")
# End.
f.write("\n// End.")
f.close()
print("finished")

# address["226 CLAVEN LN"] = "312";

"""