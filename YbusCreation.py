import pandas as pd #use if pandas is installed. can be installed using pip install pandas on terminal. Program will run without it however

buses = int(input("How many buses are there in the system? "))
lines = int(input("How many lines are there in the system? "))
print("--------------------------------------")
filepath = input("Enter the full file path of line data file. It should be csv format. ")

while True:
    headers = int(input("Does your file contain header row? Write 0 for NO and 1 for YES "))
    if headers in [0, 1]:
        a = headers
        break
    else:
        print("Invalid input. Please enter either 0 or 1.")


def readFile(filepath):
    try:
        with open(filepath, 'r') as file:
                    content = file.read()
                    # print("File content:")
                    # print(content)
                    return content
    except FileNotFoundError:
        print("The file was not found.")
    except IOError:
        print("File is not in correct format or corrupted.")

linedata = readFile(filepath)
lineparams = linedata.split('\n')

linetable = []
for line in lineparams[a:]:
      row = line.split(',')
      linetable.append(row)

print("Here is the entered data: ")
print(linetable)

ybus = [[0+0j for _ in range(buses)] for _ in range(buses)]

def magnitude_sq(z):
    return (z.real**2 + z.imag**2)

for line in linetable:
    tap = complex(line[5])
    if tap != complex(1, 0):
        ybus[int(line[0])-1][int( line[1])-1] = (-1/complex(float(line[2]), float(line[3])))/complex(tap.imag, tap.real)
        ybus[int(line[1])-1][int( line[0])-1] = (-1/complex(float(line[2]), float(line[3])))/tap
        ybus[int(line[0])-1][int( line[0])-1] += (1/complex(float(line[2]), float(line[3])))/magnitude_sq(tap)
    else:
        ybus[int(line[0])-1][int( line[1])-1] = (-1/complex(float(line[2]), float(line[3])))
        ybus[int(line[1])-1][int( line[0])-1] = (-1/complex(float(line[2]), float(line[3])))
        ybus[int(line[0])-1][int( line[0])-1] += (1/complex(float(line[2]), float(line[3])))

    ybus[int(line[0])-1][int( line[0])-1] += float(line[4])*1j/2
    ybus[int(line[1])-1][int( line[1])-1] += (1/complex(float(line[2]), float(line[3])))+ float(line[4])*1j/2

zero_count = 0
non_zero_count = 0
for row in ybus:
    for element in row:
        if element == 0:
            zero_count += 1
        else:
            non_zero_count += 1
print(pd.DataFrame(ybus)) #use if pandas is available else use line commeted below
# print(ybus)

print(f"Number of zero entries: {zero_count}")
print(f"Number of non-zero entries: {non_zero_count}")
