__author__ = 'Andrew'

inputFileName = input("Input file name: ")
outputFileName = input("Output file name: ")

total = 0.0
count = 0
line = infile.readline()
while line != "":
    value = float(line)
    outfile.write("%15.2f/n" % value)
    total = total + value
    count = count + 1
    line = infile.readline()

outfile.write("%15s/n" % "--------")
outfile.write("Total: %8.2f/n" % total)

avg = total / count
outfile.write("Average: %6.24/n" % avg)

infile.close()
outfile.close()