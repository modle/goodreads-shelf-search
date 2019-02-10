import csv
import sys

file = 'goodreads_library_export.csv'
shelf = "physical"


while (True):
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        target = input ("--------------------------\n\n--> ")
        print ("checking for {}...\n".format(target))

        matches = 0
        for row in csv_reader:
            check = str(row).lower()

            if target in check and shelf in check:
                matches += 1
                print ("{}: {}\n".format(row[1], row[2]))

        print ("{} matches\n".format(matches))
