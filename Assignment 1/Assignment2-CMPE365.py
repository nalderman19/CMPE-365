#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nicholas Alderman
Assignment 2 - CMPE 365 - Flight Paths with Dijkstras Algorithm
I certify that this submission contains my own work, except as noted.
"""

import io
import math
from urllib.request import urlopen

#download text file into bytes then converts bytes into string
fileOpen = urlopen("http://sites.cs.queensu.ca/courses/cisc365/Labs/Week%202/2019_Lab_2_flights_real_data.txt").read().decode('UTF-8') 

#converts fileOpen to format that is ready for processing - 'dataIn'
def processData(fileOpen):
    dataIn = [s for s in fileOpen.split('\n')]
    dataIn = dataIn[1:-1]
    dataIn = [t.split('\t') for t in dataIn]
    for i in range(len(dataIn)):
            for j in range(len(dataIn[i])):
                dataIn[i][j] = int(dataIn[i][j])
    return dataIn

#initializing graph dictionary
graph = {}


def dijkstras(graph,start,end):
    #create infinity variable
    infinity = math.inf
    
    #initialize dictionaries, bestAT = best arrival time
    bestAT = {}
    for vert in graph:
        if vert != start:
            bestAT[vert] = infinity
    bestAT[start] = 0
    
    parent = {}
    reached = {}
    reached[start] = True
    candidate = [start]
    
    while candidate:
        minArrival = candidate[0]
        #minArrival is the earliest node arrival time in candidate dinctionary
        
        for vert in candidate[1:]:
            #find best arrival time
            if bestAT[vert] < bestAT[minArrival]:
                minArrival = vert
        
        if minArrival == end:
            break
        else:
            for z, dTime, aTime in graph[minArrival]: #loop through all elements in input graph
                if z not in reached: #check if vertex has been reqched
                    if dTime > bestAT[minArrival]: #check if new time is valid
                        if (bestAT[z] == infinity)  or (aTime < bestAT[z]): #check if new time is better than previous
                            bestAT[z] = aTime
                            parent[z] = minArrival
                            if z not in candidate:
                                candidate.append(z)
            candidate.remove(minArrival)
            reached[minArrival] = True
    if minArrival == end: #check if end vertex has been reached
        Route = [end]
        minArrival = end
        # get optimal route by backtracking through parent dictionary
        while minArrival != start:
            Route.append(parent[minArrival])
            minArrival = parent[minArrival]
        Route.reverse()
        print ("Optimal route from node " + str(start) + " to node " + str(end))
        for i in range(len(Route)-1):
            print ("Fly from " + str(Route[i]) + " to " + str(Route[i+1]) + " arriving at " + str(bestAT[Route[i+1]]))
        print("Arrival time at " + str(end) + " at time " + str(bestAT[end]))
    else:
        print("There is not valid path from " + str(start) + " to " + str(end))

#process array into dictionary format to be used in the algorithm
graph = processData(fileOpen)
graphFinal = {}
for row in graph:
    index = row[0]
    row.pop(0)
    try:
        graphFinal[index].append(tuple(row))
    except:
        graphFinal[index] = [tuple(row)]
        
dijkstras(graphFinal,9,82)