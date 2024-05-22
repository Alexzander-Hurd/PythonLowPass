import sys
from sys import argv

averageWindow = 5
alpha = 0.5
previousValue = 0.0
inputPath = "data.csv"
outputPath = "output.csv"

print(len(argv))
if len(argv) > 1 :
    if (argv[1] == '-h' or argv[1] == '--help'):
            print("""Usage: python filter.py < -i inputFile > < -o outputFile > < -a alphaValue > < -w windowSize >
                  \nAll flags are optional and default to the example values if not specified
                  Example: python filter.py -i data.csv -o output.csv -a 0.5 -w 5""")
            sys.exit()

for i in range(1, len(argv), 2):
        if not argv[i].startswith('-'):
            print("Error: invalid argument: " + argv[i] + " (must start with '-')")
            print("For help please use -h or --help")
            sys.exit()

        match argv[i].lower():
            case '-i':
                inputPath = argv[i + 1]
            case '-o':
                outputPath = argv[i + 1]
            case '-a':
                alpha = float(argv[i + 1])
            case '-w':
                averageWindow = int(argv[i + 1])
            case _:
                print("Error: invalid argument: " + argv[i])
                print("For help please use -h or --help")
                sys.exit()
        

print("The parameters are:" +
      "\ninput file: " + inputPath + 
      "\noutput file: " + outputPath + 
      "\nalpha value: " + str(alpha) + 
      "\nwindow size: " + str(averageWindow)
)

dataIn = []
window = [0.0] * averageWindow
counter = 0

with open(inputPath, 'r') as file:
    for line in file:
        line = line.rstrip('\n')
        linearr = line.split(',')
        # for data in linearr:
        #     dataIn.append(float(data))
        dataIn.append(float(linearr[1]))

dataOut = [0.0] * len(dataIn)

with open(outputPath, 'w') as file:
    file.flush()

for i in range(len(dataIn)):
    if i == 0:
        previousValue = dataIn[i]

    if counter < averageWindow:
        window[counter] = dataIn[i]
        counter += 1
    else:
        for j in range(averageWindow-1):
            window[j] = window[j + 1]    
        window[averageWindow-1] = dataIn[i]

    ybar = sum(window) / counter+1
    yhat = previousValue + alpha * (ybar - previousValue)
    dataOut[i] = yhat

    print(dataIn[i], dataOut[i])

    with open(outputPath, 'a') as file:
        file.write(str(i) + ',' + str(dataOut[i]) + '\n')

