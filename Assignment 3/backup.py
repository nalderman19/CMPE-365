'''
CMPE 365 - Assignment 4 - Huffman Encoding - November 4
Nicholas Alderman - 20060982 - 16naa5
'''
import os, math
from heapq import heappush, heappop, heapify


class Huffman:
    def __init__(self, txt):
        self.initDict()
        self.makeFreq(txt)
        self.codeBuilder()
    # initialize frequency dictionary
    def initDict(self):
        self.asciiFreq = {}
        # Special case for newline character
        self.asciiFreq[chr(10)] = 0
        # loop through rest of characters and increment frenquency
        for i in range(32,127):
            self.asciiFreq[chr(i)] = 0
    def incrementFreq(self, txt):
        for char in txt:
            self.asciiFreq[char] += 1
    
    def codeBuilder(self):
        # implementation of generating huffman dictionary using a heap
        heap = [[wt, [sym, ""]] for sym, wt in self.asciiFreq.items()]
        heapify(heap)
        while len(heap) > 1:
            # takes first two elements of heap, pairs them and pushes the combined element back in
            lo = heappop(heap)
            hi = heappop(heap)
            for pair in lo[1:]:
                pair[1] = '0' + pair[1]
            for pair in hi[1:]:
                pair[1] = '1' + pair[1]
            heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
            
        # converts heap to array to generate actual mapping and reverse mapping
        array = heappop(heap)[1:]
        self.mapping = {char[0]:char[1] for char in array}
        self.reverseMapping = {char[1]:char[0] for char in array}
        
        
    def encode(self, txt):
        # init encoded string
        eTxt = ""
        # loop through the text passed in and applies mapping to it
        for char in txt:
            eTxt += self.mapping[char]
        return eTxt
    def decode(self, txt):
        # init decoded string to be returned and string to check mapping
        dTxt = ""
        dStr = ""
        for char in txt:
            dStr += char
            # check if reverseMapping contains current string and if so, apply reverse Mapping 
            if dStr in self.reverseMapping:
                dTxt += self.reverseMapping[dStr]
                dStr = ""
        return dTxt
    
''' Part 1
use File1ASCII.txt to create a dictionary, then encode and decode File2ASCII.txt using said dictionary
'''
# open File1
inText = open("File1ASCII.txt", "r")
inText = inText.read()
outFile = open("Part1/Part1Encoded.txt", "w")
outFile2 = open("Part1/Part1Mapping.txt", "w")
outFile3 = open("Part1/Part1Decoded.txt", "w")
# Generate dictionary using File1
huff = Huffman(inText)
# Write mapping to "Part1Mapping.txt"
outFile2.write(str(huff.mapping))
# Encode File2 using File1 dictionary
enc = huff.encode(inText)
# Write encoding to "Part1Encoded.txt"
outFile.write(enc)
# Decode "Part1Encoded.txt"
dec = huff.decode(enc)
# Write decoded data to "Part1Decoded.txt
outFile3.write(dec)
outFile.close()
outFile2.close()
outFile3.close()


''' part 2

read in each of the files in canonical folder and use 'codeBuilder' to generate code-string dictionary

concatenate files in folder and generate dictionary with new string, then use it to encode each file in Data

as each file is encoded, write it to a file of name "Encoded-FILENAME.txt


'''
'''
# concatenate text to make dictionary
# dictfiles are arrays containing the files to be used to create the dictionary, this is looped for each test
dictFiles1 = ["words1ASCII.txt"]
dictFiles2 = ["Canonical2/ShortText1.txt", "Canonical2/ShortText2.txt", "Canonical2/ShortText3.txt", "Canonical2/ShortText4.txt", "Canonical2/ShortText5.txt", 
              "Canonical2/ShortText6.txt", "Canonical2/ShortText7.txt", "Canonical2/ShortText8.txt", "Canonical2/ShortText9.txt", "Canonical2/ShortText10.txt"]
dictFiles3 = ["Canonical3/ChestertonASCII.txt", "Canonical3/DickensASCII.txt"]

dictFiles = {"num1": dictFiles1,
         "num2": dictFiles2,
         "num3": dictFiles3}
'''
for i in dictFiles.values():
    inText = ""
    # loop through files in dictFiles array
    for fname in dictFiles:
        # add text from each file to string
        with open(fname, "r") as infile:
            inText += infile.read()
    # make dictionary using concatenated string           
    huff = Huffman(inText)
    # get mapping
    # print (huff.mapping)
    
    
    # encode each file in inFiles array using new huffman encoding using outfile names
    inFiles = ["Data/EarthASCII.txt", "Data/MysteryASCII.txt", "Data/MythsASCII.txt", "Data/SimakASCII.txt", "Data/WodehouseASCII.txt"]
    fLen = []
    # loop throufh files to encode and encode them
    for fname in inFiles:
        f = open(fname, "r")
        inText = f.read()
        enc = huff.encode(inText)
        # add size of encoded file to fileLength array
        fLen.append(math.ceil(len(enc)/8))
        # remove last for characters to add appropriate name
        outF = open(fname[:-4] + "-encoded.txt", "w")
        outF.write(enc)
        outF.close()
        
    # to ensure file gets rewritten and not added to each time the program is run
    open("resultsC3.txt", "w").close()
      
    # get bytes of original file and encoded file, print to outputdata
    for i, fname in enumerate(inFiles):
       oSize = os.path.getsize(fname)
       eSize = fLen[i]
       # the name of this file is changed for each canonical collection, results1 = Collection1, results2 = Collection2...
       outF = open("resultsC3.txt", "a+")
       outF.write("Original  size of: " + str(oSize) + "   Encoded size: " + str(eSize)+'\n')
       if oSize < eSize:
           outF.write("Since the original size is smaller than the encoded size, it is not worth encoding\n")
       else:
           outF.write("Since the original size is larger than the encoded size, it is worth encoding\n")
       outF.close()
    
