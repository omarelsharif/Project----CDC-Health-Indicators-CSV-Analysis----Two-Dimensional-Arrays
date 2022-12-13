


#Omar El-Sharif 

'''
This program uses two-dimensional arrays to store the highest and lowest temperatures for each month of the year (received as user input),
then completes an analysis on the temperatures received.
''' 



def getData():

    matrix = []

    while 1==1:

        print("Enter highest temperatures for 12 months, separated by spaces: ")
        x = input()
        if len(x) < 12:
            continue
        else:
            break   
    list1 = x.split()
    for i in range(len(list1)):
            list1[i] = float(list1[i])

    print()
    while True:
        print("Enter lowest temperatures for 12 months, separated by spaces: ")
        x = input()
        if len(x) < 12:
            continue
        else:
            break
    list2 = x.split()
    for y in range(len(list2)):
            list2[y] = float(list2[y])
    matrix.append(list1)
    matrix.append(list2)
    return matrix

def averageHigh(matrix):
    sum1 = 0
    for i in matrix[0]:
        sum1 = i + sum1
    aveHigh = sum1/len(matrix[0])
    return aveHigh

def averageLow(matrix):
    sum2 = 0
    for i in matrix[1]:
        sum2 = i + sum2
    aveLow = sum2/len(matrix[1])
    return aveLow

 
def highTemp(matrix):

    x = max(matrix[0])

    y = max(matrix[1])

    if x > y:
        return x
    elif y > x:
        return y
    elif y == x:
        return y






def lowTemp(matrix):
    x = min(matrix[0])
    y = min(matrix[1])
    if x > y:
        return y
    elif y > x:
        return x
    elif y == x:
        return y
     


def main():

    matrix = getData()
    print()
    print("List of the highest and lowest temperatures for each month of the year")
    print()
    print("Highest Temps:", matrix[0])
    print("Lowest Temps:", matrix[1])
    print()
    lowestTemp = lowTemp(matrix)
    highestTemp = highTemp(matrix)
    aveHighTemp = averageHigh(matrix)
    aveLowTemp = averageLow(matrix)

    aveHighTemp = "{:.1f}".format(aveHighTemp) 
    aveLowTemp = "{:.1f}".format(aveLowTemp) 

    highestTemp = "{:.1f}".format(highestTemp) 

    lowestTemp = "{:.1f}".format(lowestTemp) 
    
    print("Average high temperature for the year",aveHighTemp)
    print("Average low temperature for the year",aveLowTemp)
    print("Highest highest temperature for the year",highestTemp)
    print("Lowest low temperature for the year",lowestTemp)


main()

