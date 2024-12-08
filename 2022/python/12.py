#!/usr/bin/env python3

import sys
import collections
elevations = open("input/day_12.txt", "r").read().splitlines()

ascii_elevations = []
for line in elevations:
    tmp = []
    for character in line:
        #if character == "S":
        #    character="a"
        #if character == "E":
        #    character="z"
        tmp.append(ord(character))
    ascii_elevations.append(tmp)

START=ord("S")
END=ord("E")
print(ascii_elevations, START, END)

graph={}
## buld graph
for row in range(len(ascii_elevations)):
    for gollum in range(len(ascii_elevations[row])):

        current = ascii_elevations[row][gollum]
        graph[(row, gollum)] = []

        if current == START:
            current=ord("a")
            START=(row, gollum)
        if current == END:
            current=ord("z")
            END=(row, gollum)
        # up
        if row-1 >= 0:
            if ascii_elevations[row-1][gollum] == current+1 or ascii_elevations[row-1][gollum] <= current:
                graph[(row, gollum)].append((row-1, gollum))

        # down
        if row+1 < len(ascii_elevations):
            if ascii_elevations[row+1][gollum] == current+1 or ascii_elevations[row+1][gollum] <= current:
                graph[(row, gollum)].append((row+1, gollum))


        # left
        if gollum-1 >= 0:
            if ascii_elevations[row][gollum-1] == current+1 or ascii_elevations[row][gollum-1] <= current:
                graph[(row, gollum)].append((row, gollum-1))

        # right
        if gollum+1 < len(ascii_elevations[row]):
            if ascii_elevations[row][gollum+1] == current+1 or ascii_elevations[row][gollum+1] <= current:
                graph[(row, gollum)].append((row, gollum+1))

#graph = {"P":["Q", "R", "S"], "Q":["P", "R"], "R":["P", "Q", "T"], "T":[], "S":[]}


#print(graph)
print(START)

def dijkstra(G:dict, start:list=START):
    dist = {}
    prev = {}
    Q = []
    for vertex in G.keys():
        dist[vertex]=100000000000000
        prev[vertex]=""
        Q.append(vertex)

    while Q:
        current = min(dist, key=dist.get)
        row, gollum = current
        if elevations[row][gollum] == "E":
            return dist, prev
        Q.remove(current)

        for neighbour in G[current]:
            if not neighbour in Q:
                continue
            alt = dist[current] + 1
            if alt < dist[neighbour]:
                dist[neighbour] = alt
                prev[neighbour] = current
    return dist, prev

print(dijkstra(graph))
