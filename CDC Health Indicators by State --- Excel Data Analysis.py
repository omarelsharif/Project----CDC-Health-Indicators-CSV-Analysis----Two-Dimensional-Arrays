
# Omar El-Sharif elsharifomar293@gmail.com


'''
Code Idea  / Explainer

There are 20 health indicators that the CDC includes in the CSV file that it regularly publishes,
but for simplicity the program I wrote looks at five: Heart Disease Death Rate, Motor Vehicle Death Rate, Teen Birth Rate, Adult Smoking, and Adult Obesity. 

Essentially, this code reads data from the CSV file and finds the states with the best and worst record for each indicators.
It then produces a file called “best_and_worst.txt”
which lists the states that have the highest and lowest value for each of the indicators,along with their values.
I made sure that the code was general enough to work with a similar file with states as rows and with the same column headers,
so if the CDC puts out a new file with different values in the cells
this program will continue to work correctly.
'''







def dataoperations(): # This function extracts and completes data operations to pass arguments to the writing function
    import csv
    inFile = open("riskfactors.csv", "r")
    csvReader =csv.reader(inFile)   
    for i in range(6):
        titles = next(csvReader)


    statelist = [] # These statements ensure that code works for all column lengths and orders 
    statecol = 0
    found = "false"
    statelist = [] 
    for i in titles:
        if i == 'State':
            state = i
            found = "true"
            statecol+=1 
            
        if found!= "true":

            statecol +=1
    statecol -=1

    for aline in csvReader:
        statelist.append(aline[statecol])
     

    inFile = open("riskfactors.csv", "r")
    csvReader =csv.reader(inFile)   
    for i in range(6):
        titles = next(csvReader)


    heartlist = [] 
    heartcol = 0
    found = "false"
    heartlist = [] 
    for i in titles:
        if i == 'Heart Disease Death Rate (2007)':
            #print(i)
            heart = i
            found = "true"
            heartcol+=1 
            
        if found!= "true":

            heartcol +=1
    heartcol -=1

    motorlist = [] 
    motorcol = 0
    found = "false"
    motorlist = [] 
    for i in titles:
        if i == 'Motor Vehicle Death Rate (2009)':
            #print(i)
            motor = i
            found = "true"
            motorcol+=1 
            
        if found!= "true":

            motorcol +=1
    motorcol -=1

    birthlist = [] 
    birthcol = 0
    found = "false"
    birthlist = [] 
    for i in titles:
        if i == 'Teen Birth Rate (2009)':
            birth = i
            found = "true"
            birthcol+=1 
            
        if found!= "true":

            birthcol +=1
    birthcol -=1

    smokelist = [] 
    smokecol = 0
    found = "false"
    smokelist = [] 
    for i in titles:
        if i == 'Adult Smoking (2010)':
            #print(i)
            smoke = i
            found = "true"
            smokecol+=1 
            
        if found!= "true":

            smokecol +=1
    smokecol -=1


    obeselist = [] 
    obesecol = 0
    found = "false"
    obeselist = [] 
    for i in titles:
        if i == 'Adult Obesity (2010)':
            #print(i)
            heart = i
            found = "true"
            obesecol+=1 
            
        if found!= "true":

            obesecol +=1
    obesecol -=1

# Creating a list 
    for aline in csvReader:
        heartlist.append(aline[heartcol])
        motorlist.append(aline[motorcol])
        birthlist.append(aline[birthcol])
        smokelist.append(aline[smokecol])
        obeselist.append(aline[obesecol])
     

    for i in range(0,len(obeselist)):# removing % symbols 
        x = obeselist[i] 
        x = (str(x)).replace("%","")
        obeselist[i] = x


    for i in range(0,len(smokelist)): # removing % symbols 
        x = smokelist[i] 
        x = (str(x)).replace("%","")
        smokelist[i] = x

    obeselist= [float(x) for x in obeselist]
    heartlist= [float(x) for x in heartlist]
    motorlist= [float(x) for x in motorlist]
    smokelist= [float(x) for x in smokelist]
    birthlist= [float(x) for x in birthlist]

    #Finding the mins and maxes of the 
    minheart = (min(heartlist))
    maxheart = (max(heartlist))
    minmotor = (min(motorlist))
    maxmotor = (max(motorlist))
    minbirth = (min(birthlist))
    maxbirth = (max(birthlist))
    minsmoke = (min(smokelist))
    maxsmoke = (max(smokelist))
    minobese = (min(obeselist))
    maxobese = (max(obeselist))
    
    # Creating variables for the min's and max's that I found, so that I can manipulate them later if I choose to. 
    maxheartindex = heartlist.index(maxheart)
    maxheartstate = (statelist[maxheartindex])
    minheartindex = heartlist.index(minheart)
    minheartstate = (statelist[minheartindex])
    maxmotorindex = motorlist.index(maxmotor)
    maxmotorstate = (statelist[maxmotorindex])
    minmotorindex = motorlist.index(minmotor)
    minmotorstate = (statelist[minmotorindex])
    maxbirthindex = birthlist.index(maxbirth)
    maxbirthstate = (statelist[maxbirthindex])
    minbirthindex = birthlist.index(minbirth)
    minbirthstate = (statelist[minbirthindex])
    maxsmokeindex = smokelist.index(maxsmoke)
    maxsmokestate = (statelist[maxsmokeindex])
    minsmokeindex = smokelist.index(minsmoke)
    minsmokestate = (statelist[minsmokeindex])
    maxobeseindex = obeselist.index(maxobese)
    maxobesestate = (statelist[maxobeseindex])
    minobeseindex = obeselist.index(minobese)
    minobesestate = (statelist[minobeseindex])


    print("Indicator:             Min                    Max")
    print("-"*80)
    #Printing the indicators that I am searching for, as well as ensuring that they are formatted properly. 
    l1 = '{:<21}  {:<21}  {:<21} {:<21}'.format(minheartstate, minheart, maxheartstate, maxheart)

    l2 = '{:<21}  {:<21}  {:<21} {:<21}'.format(minmotorstate, minmotor, maxmotorstate, maxmotor)
    l3 = '{:<21}  {:<21}  {:<21} {:<21}'.format(minbirthstate, minbirth, maxbirthstate, maxbirth)
    l4 = '{:<21}  {:<21}  {:<21} {:<21}'.format(minsmokestate, minsmoke, maxsmokestate, maxsmoke)
    l5 = '{:<21}  {:<21}  {:<21} {:<21}'.format(minobesestate, minobese, maxobesestate, maxobese)

    print(l1)
    
    print(l2)
    print(l3)
    print(l4)
    print(l5)
    write(l1,l2,l3,l4,l5)


# Writing the data to the best_and_worst.txt
def write(l1,l2,l3,l4,l5):
    outFile = open("best_and_worst.txt","w")
    outFile.write("Indicator:             Min                    Max")
    outFile.write("\n")
    outFile.write("-"*80)
    outFile.write("\n")
    outFile.write(l1)
    outFile.write("\n")
    outFile.write(l2)
    outFile.write("\n")
    outFile.write(l3)
    outFile.write("\n")
    outFile.write(l4)
    outFile.write("\n")
    outFile.write(l5)
    outFile.close()



dataoperations()
print()
print("A .txt file called best_and_worst.txt was created, ")
print("and the table above was written in it.") 













