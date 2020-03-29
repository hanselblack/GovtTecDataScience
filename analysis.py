#!/usr/bin/env python3
import csv
import pandas as pd
import numpy as np

df = pd.read_csv('mrt_trips_sampled.csv')
df_agg = df.groupby(['origin', 'destination']).median()

g = df_agg['secondsDiff'].groupby(level=0, group_keys=False)
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    res = g.nsmallest(1000000)
    print (res, file=open("output.txt", "a"))

# class A:
#     def __key(self):
#         return (self.origin, self.destination, self.diff)

#     def __hash__(self):
#         return hash(self.__key())

#     def __eq__(self, other):
#         if isinstance(other, A):
#             return self.__key() == other.__key()
#         return NotImplemented

# with open('mrt_trips_sampled.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     station_trip_set = set();
#     station_set = set();

#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         else:
#             stationObject = A()
            
#             stationObject.origin = row[3],
#             stationObject.destination = row[1],
#             stationObject.diff = row[5]

#             station_trip_set.add(stationObject)

#             station_set.add(row[1]);
#             #print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')

#             line_count += 1
#     print(f'Processed {len(station_set)} lines.')
    

#     stationStart = "Clementi"#list(station_set)[0];

#     station1Set = set();
#     print("Origin is from " + stationStart);
#     for row in station_trip_set:
#       if stationStart == row.origin[0]:
#         stationObject = A() 
#         stationObject.origin = row.origin[0],
#         stationObject.destination = row.destination[0],
#         stationObject.diff = row.diff
#         station1Set.add(stationObject)

#     sorted_stations = sorted(station1Set, key=lambda x: x.diff)
#     sortedStationSet = list();
#     originDestinationDict = dict();

    
#     for row in sorted_stations:
#       concatStr = row.origin[0] + " to " + row.destination[0]
#       originDestinationSet.add(concatStr)
#       print (row.origin[0] + " " + row.destination[0] + " " + row.diff, file=open("output.txt", "a"))
#       sortedStationSet.append(row.destination[0])

#     sortedStationList = list(dict.fromkeys(sortedStationSet).keys())
#     train_network = ""
#     for row in sortedStationList:
#       stringToAdd = row +" -> "
#       train_network += stringToAdd
      
#     print (train_network)

