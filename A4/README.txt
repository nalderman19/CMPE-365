CMPE 365 Assignment 3
Nicholas Alderman - 20060982
I certify that this submission contains my own work, except as
 noted.

Part 1
The results of part 1 can be seen in the part1 folder. This folder
contains the encoded file, the decoded file (to prove the decoded
version is identical to the original), and the mapping file which
is the dictionary mapping written to a file. This 'Part1Mapping.txt'
is the code-string dictionary generated in Part 1 that was asked for in the instructions.

Part 2
Each 'resultsCX.txt' contains the file size of the original file
and encoded file. The size of the encoded file is the length of
the encoded string/8bits. 'X' corresponds to which canonical 
collection was used to create the code-string dictionary.  In
each text file for every input file it is determined whether or
not the code-string dictionary was efficient. As seen in the 
files, collection 1, is not efficient, and collections 2 and 3 
are efficient.  

It may seem like the quantity of characters is proportional to the
efficiency of the encoding. Just looking at the size of the 
dictionary files, collection 1 is 398KB, and the encoded size is an
average of 261.6% of the original size. Whereas, for collection 2,
the original files are a total of 7 KB and the encoded size is an
average of 59.9% of the original. This is far lower than the 
first collection even thoughthe size of the original files is 
also lower.  The next hypothesis as to why thedictionaries are 
more efficient could have somethingto do with the type of 
content included in the dictionary files.The first collection is 
just an english dictionary, this doesn't Create anefficient 
encoding because the code-string dictionary 'isn't created based
on how the alphabet is actually used in practice. Since 
collections 2 and 3 are made up of more 'natural'english, they
can more properly create a code-string dictionary based on 
frequency. While collection 3 is the largest, it alsocontains
the frequency of characters that would be similar to 
the frequency of characters in the files being encoded. This
is made obvious by the fact that the size of the encoded 
files are 58% the size of the original files.