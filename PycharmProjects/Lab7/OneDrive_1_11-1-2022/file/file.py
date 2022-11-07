import sys


try:
    data_in = sys.argv[1]
    data = open(data_in, 'r')
except IndexError:
    print('Index Error')
    exit()
except FileNotFoundError:
    print('File Not Found')
    exit()
for line in data:
    try:
        line = line.split()
        sum = float(line[0]) + float(line[1])
        print(sum)
    except IndexError:
        print('Not enough numbers')
    except ValueError:
        print('Not a number')