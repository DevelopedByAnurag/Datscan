
# coding: utf-8

# In[3]:


def RUNN3R(S4V3):
    
    import tweepy
    import csv
    import pandas as pd
    ####input your credentials here
    C0NSUM3R_K3Y = input("Enter Consumer Key: ")
    C0NSUM3R_S3CR37 = input("Enter Consumer Secret Key: ")
    ACC3SS_T0K3N = input("Enter Access Token: ")
    ACCESS_T0KEN_S3CR3T = input("Enter Secret Access Token: ")

    AU7H = tweepy.OAuthHandler(C0NSUM3R_K3Y, C0NSUM3R_S3CR37)
    AU7H.set_access_token(ACC3SS_T0K3N, ACCESS_T0KEN_S3CR3T)
    API = tweepy.API(AU7H,wait_on_rate_limit=True)
    file = ST4ND4R7IS3_CSV(S4V3)
    csvFile = open(file, 'a')
    #Use csv Writer
    temp = input("Enter the tags you want to scrape and diffrencitate with help of spaces")
    temp0 = temp.split(" ")
    for temp1 in temp0:
        csvWriter = csv.writer(csvFile)
        for tweet in tweepy.Cursor(api.search,q=temp1,count=10, lang="en", since="2001-04-03").items():
            print (tweet.created_at, tweet.text)
            csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

