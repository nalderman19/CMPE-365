"""
CMPE 365 - Assignment 4 - LCS
Nicholas Alderman - 20060982 - 16naa5
"""


# f1 takes in line from array and returns ascii sum
def f1(s):
    result = 0
    for c in s:
        result = (7*result + ord(c))%100000
    return result


# hash1 builds hash table of ints like f1Dict
def hash1(s):
    array1=[]
    for line in s:
        array1.append(f1(line))
    return array1


# lcs algorithm, takes in arrays of lines of files and returns 2D array
def lcs(a1, a2):
    # gets hash table for faster computations
    h1 = hash1(a1)
    h2 = hash1(a2)

    # builds empty array of size x*y using lengths of arrays passed into lcf method 
    x = len(a1)
    y = len(a2)
    vals = [[None]*(y+1) for i in range(x+1)]

    # LCS algorithm
    for i in range(x+1):
        for j in range(y+1):
            # Base case
            if i == 0 or j == 0:
                vals[i][j] = 0
            # Check from lab 9 - "when two lines have matching function numbers you will 
            #                     have to compare them to see if they actually match"
            elif (h1[i-1] == h2[j-1]):
                if (a1[i-1] == a2[j-1]):
                    vals[i][j] = vals[i-1][j-1]+1
            else:
                vals[i][j] = max(vals[i-1][j] , vals[i][j-1])
    return vals

# traverse takes a 2D lcs array and dimensions and returns 3D array containing a substrings of either matched or mismatched lines
def traverse(vals, x, y):
    # traversal 1: going left or up in the 2D array
    # traversal 2: going diagonally left and up in the 2D array

    xval = []
    yval = []
    tmp3dArray =[[],[]]
    # flag is used to check between two cases, must be none initially
    flag = None

    while(x>-2 and y>-2 ):
        # traversal 1
        # checks if value to left is the same
        if (vals[x-1][y] == vals[x][y]):
            # checks if theres a case change
            if (flag == 0):
                # creates a tmp 2D array and adds it to output array
                tmp=[xval, yval]
                tmp3dArray.append(tmp)
                # x and yvalues are reset
                xval=[]
                yval=[]
            # store value and move location to left
            xval.append(x)
            x= x-1
            flag = 1
        # checks if value above is the same
        elif (vals[x][y-1] == vals[x][y]):
            if (flag == 0):
                tmp=[xval, yval]
                tmp3dArray.append(tmp)
                xval=[]
                yval=[]
            yval.append(y)
            y= y-1
            flag = 1

        # traversal 2
        # checks if value diagonally top and to the left is one less
        else:
            if (flag ==1):
                tmp=[xval, yval]
                tmp3dArray.append(tmp)
                xval=[]
                yval=[]
            xval.append(x)
            yval.append(y)
            flag = 0
            x -= 1
            y -= 1
    
    # only need to return values from index 2 and up
    final3d = tmp3dArray[2:]
    return final3d


# main method
if __name__ == "__main__":
    # gets 2 inputs and creates array consisting of lines for each file
    try:
        name1 = input("Enter File Name 1: ")
        name2 = input("Enter File Name 2: ")
        F1 = open(name2, "r")
        f2 = open(name1, "r")
    except:
        print ("Incorrect File Name(s); please try again.")
    else:
        a1=[]
        a2=[]
        # adds each line to index into array
        for l in F1:
            a1.append(l)
        for l in f2:
            a2.append(l)
        F1.close()
        f2.close()
    
        # creates 2D memory array
        stored = lcs(a1, a2)
        # creates final array with substrings of either matched or mismatched lines
        final3d = traverse(stored, len(a1), len(a2))
        # write to output file and ensure it has .txt
        nO = input("Enter output file name: ")
        if ".txt" not in nO:
            nO += ".txt"
        fO = open(nO, "w")
        dO = ""
    
    
        # checks if initial match or mismatch to calibrate output
        if (a1[0]==a2[0]):
            flag = True
        else:
            flag = False
    
        # for loop iterates and prints out final3d array by checking flag each iteration
        for i in range(len(final3d)-1,-1,-1):
            column1 = final3d[i][0]
            column2 = final3d[i][1]
            if (flag):
                try:
                    print(f'Match:  \t{name1}: \t<{column1[-1:][0]}...{column1[:1][0]}>\t\t{name2}: \t<{column2[-1:][0]}...{column2[:1][0]}>\n')
                    dO+=(f'Match:  \t{name1}: \t<{column1[-1:][0]}...{column1[:1][0]}>\t\t{name2}: \t<{column2[-1:][0]}...{column2[:1][0]}>\n')
                except IndexError:
                    if (column1[-1:] == []):
                        print(f'Match:  \t{name1}: \t<none>\t\t{name2}: \t<{column2[-1:][0]}...{column2[:1][0]}>\n')
                        dO+=(f'Match:  \t{name1}: \t<none>\t\t{name2}: \t<{column2[-1:][0]}...{column2[:1][0]}>\n')
                    else:
                        print(f'Match:  \t{name1}: \t<{column1[-1:][0]}...{column1[:1][0]}>\t\t{name2}: \t<none>\n')
                        dO+=(f'Match:  \t{name1}: \t<{column1[-1:][0]}...{column1[:1][0]}>\t\t{name2}: \t<none>\t\t\n')
                flag = False
            else:
                try:
                    print(f'Mismatch:  \t{name1}: \t<{column1[-1:][0]}...{column1[:1][0]}>\t\t{name2}: \t<{column2[-1:][0]}...{column2[:1][0]}>\n')
                    dO+=(f'Mismatch:  \t{name1} : \t<{column1[-1:][0]}...{column1[:1][0]}>\t\t{name2}: \t<{column2[-1:][0]}...{column2[:1][0]}>\n')
                except IndexError:
                    if (column1[-1:] == []):
                        print(f'Mismatch:  \t{name1}: \t<none>\t\t{name2}: \t<{column2[-1:][0]}...{column2[:1][0]}>\n')
                        dO+=(f'Mismatch:  \t{name1}: \t<none>\t\t{name2}: \t<{column2[-1:][0]}...{column2[:1][0]}>\n')
                    else:
                        print(f'Mismatch:  \t{name1}: \t<{column1[-1:][0]}...{column1[:1][0]}>\t\t{name2}: \t<none>\n')
                        dO+=(f'Mismatch:  \t{name1}: \t<{column1[-1:][0]}...{column1[:1][0]}>\t\t{name2}: \t<none>\t\t\n')
                flag = True
        fO.write(dO)
        fO.close()

