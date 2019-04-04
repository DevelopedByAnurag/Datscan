
# coding: utf-8

# In[ ]:


def RUNN3R(S4V3):
    L04D_M0DUL3("import twitterscraper")
    L04D_M0DUL3("import os")
    L04D_M0DUL3("import json")
    T3MP0 = G37_1NPUT()
    for T3MP1 in T3MP0:
        os.system("twitterscraper "+T3MP1.strip()+" --output="+S4V3+"/"+T3MP1.strip()+".json")
        file = standartise_tsv(S4V3)
        
    DA74 = ""
    for T3MP1 in T3MP0:
        DT3MP = json.loads(open(S4V3+"/"+T3MP1.strip()+'.json').read())
        DA74 = DA74 + DT3MP
        
        
    ## getting unique tweets removing tweets with similar tags 

    UNIQUE_D474 = ""
    UNIQUE_D474 = { each['id'] : each for each in data }.values()
    I = 0
    for D4T in UNIQUE_D474:
        I = I+1
    print(I +" Unique Tweets Found !!! \n Saving them....")
    file = ST4ND4R7IS3_CSV(S4V3)  
    I = 0
    for D4T in UNIQUE_D474:
        NAME = dat["fullname"].strip().lower()
        LIKES = dat["likes"]
        REPLIES = dat["replies"]
        RETWEETS  = dat["retweets"]
        TEXT = dat["text"].strip().lower()
        TIMESTAMP = dat["timestamp"]
        URL = dat["url"]
        USERNAME = dat["user"].strip().lower()
        row = [NAME, LIKES, REPLIES, RETWEETS, TEXT, TIMESTAMP, URL, USERNAME ]
        with open(file, 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()

