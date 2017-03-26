# Townland_Names
Processes the names of Irish Townlands for openstreetmap.org (OSM). Tries to identify typos and consolidate Townland names. 

Main goal is to identify typos in Townland names by comparing to other databases and identifing 'unique' entries in OSM.

Firstly, I'm a python noob, so don't be surprised if my code is dumb or inefficient. Suggestions and improvements are welcome.

I will not do any mass improt to OSM as there can be many reasons for 'unique' entries.
This resulting list of unique entries in OSM should be manually checked if it is a typo, hopefully with help of OSM community.
I also created a Wiki section for guidelines about this:
ttps://wiki.openstreetmap.org/wiki/Ireland/Mapping_Townlands#Guidelines_for_Correcting_Typos_in_Boundary_Names:

Program also identifies some of the reasons why a unique entry may occur.
For exampple, It can identify X_North townlands and (I hope to add) checking for Xnorth and so on.
This should reduce the list of 'unique' entries.

TO DO:
Input databases that I am using are old (Logainm 2014, and OSM 2016). Need to update with better import data.
(Would like to) 'feed' it multiple sources of townland names.
placenames.ie data is needed to stop NI townlands from being identified as 'unique'
