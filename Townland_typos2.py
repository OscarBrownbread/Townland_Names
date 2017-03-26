import pandas as pd

df = pd.read_csv("Logainm townlands CSV.csv")
#print(df.head())
#print(df.loc[:,'NAME_EN'])

#Word Structure of Names
#Structure Words contain spaces '_North' so won't capture North X.
Words_geography = [' North', ' South', ' East', ' West', ' More', ' Beg' ,' Lower', ' Upper', ' Middle', ' Near' , ' Far', ' Long', ' Great', ' Big', ' Little',' Small']
Words_type = [' Island', ' Isle' ' Point', ' Head', ' Glebe', ' Park', ' Common', ' Commons', ' Castle', ' Demesne', 'Demense', ' Bog', ' Hill', ' Mountain', ' Lot', 'Burrow']
#' Gap'
Words_irish = [' Eighter', ' Oughter', ' Barr', 'Gob ', ' Thuaidh'] #' Kill' ??, Gob = Point, Bal= part of ???, 
Words_time = [' Old', ' New', ' English', ' Irish']
StructureWords=Words_time + Words_irish + Words_type + Words_geography

#Further check: Xmore, X (East), 
for TL in df.loc[0:2300,'NAME_TAG1']:

    #Check name ANYWHERE in column
    #found= df['Logainm_name'].str.find(TL) ; #print(found)
    #if max(found) == -1:)
        #Print('Duplicate')
    
    #Check EXACT Name is duplicated in Logainm Column or is Unique. Unique = possible typo
    if TL in list(df['Logainm_name']):
        #print ("Duplicate", TL)
        pass
    else:
        #print ("Unique ", TL)
        df.loc[df.NAME_TAG1==TL,"Unique"]="Not in Logainm"

    #Check for Townland with two names i.e. alt_name
    if  " or " in TL:
        #print ("X or Y Townland with two names")
        df.loc[df.NAME_TAG1==TL,"Two Names"]="X or Y"
        
    #Check for exclave    
    if "part of" in TL:
        #print ("possible exclave")
        df.loc[df.NAME_TAG1==TL,"Exclave"]="(part of), exclave?"

    #Check for 'Structure' Words 
    for StW in StructureWords:
        if StW in TL:
            #print ("Structure Words")
            df.loc[df.NAME_TAG1==TL,"Structure Words?"]="N S E W etc."

    #Check for 'X (Landowner name)' or 'X (Parish)' or other e.g. (E.D. 
    if "(" and ")" in TL:
        #print ("Brackets")
        df.loc[df.NAME_TAG1==TL,"Brackets"]="(  )"

    #Dash can get converted to space or removed.
    if "-" in TL:
        #print ("dash - ")
        df.loc[df.NAME_TAG1==TL,"Dash"]=" Dash - "
        
    # Apostrophe for proper nouns etc.
    if "\'" in TL: # 141 " ' " and 116 " 's "
        #print ('Apostrophe \' ')
        df.loc[df.NAME_TAG1==TL,"Apostrophe"]=" ' "
    


print('Processing complete')
Export_Cols4=['NAME_TAG1', 'Unique']
Export_Cols3=['Logainm_name', 'NAME_TAG1', 'Unique']
Export_Cols2=['Logainm_name', 'NAME_TAG1', 'Unique', 'Two Names', 'Structure Words?']
Export_Cols=['Logainm_name', 'NAME_TAG1', 'Unique', 'Two Names', 'Exclave', 'Structure Words?','Brackets', 'Dash', 'Apostrophe']
#df[Export_Cols].to_csv("Townlands_Formatted.csv")
df.loc[df.Unique=="Unique",['NAME_TAG1', 'CO_NAME']].to_csv("Townlands_Formatted.csv")
raise SystemExit()
