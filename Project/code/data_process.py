import pandas as pd
import numpy as np 
#import
df = pd.read_csv("Hotel_Reviews.csv")
#print(df.shape) ##(515738, 17)
print("Total number of observations:", df.shape[0], "Number of observed features:", df.shape[1])
print(df.columns) ###list of observed features
##Index([u'Hotel_Address', u'Additional_Number_of_Scoring', u'Review_Date',
       #u'Average_Score', u'Hotel_Name', u'Reviewer_Nationality',
       #u'Negative_Review', u'Review_Total_Negative_Word_Counts',
       #u'Total_Number_of_Reviews', u'Positive_Review',
       #u'Review_Total_Positive_Word_Counts',
       #u'Total_Number_of_Reviews_Reviewer_Has_Given', u'Reviewer_Score',
       #u'Tags', u'days_since_review', u'lat', u'lng'],
       #dtype='object')
print(df.head())
print(sum(df.duplicated()))
df = df.drop_duplicates()
print(df.shape)
print("After removing duplicated data, the total number of observations is:", df.shape[0], 
      "the total number of features is:", df.shape[1])
##process missing values
print(df.isnull().any().any())
nans = lambda df: df[df.isnull().any(axis = 1)]
nans_df = nans(df)[["Hotel_Name", "lat", "lng"]]
print(nans_df.shape)
print("Total number of missing values:", nans_df.shape[0])
print(nans_df.Hotel_Name.describe())
print(nans_df.Hotel_Name.value_counts())
#latitude information of Hotels
loc_lat = {'Fleming s Selection Hotel Wien City':48.209270,
       'Hotel City Central':48.2136,
       'Hotel Atlanta':48.210033,
       'Maison Albar Hotel Paris Op ra Diamond':48.875343,
       'Hotel Daniel Vienna':48.1888,
       'Hotel Pension Baron am Schottentor':48.216701,
       'Austria Trend Hotel Schloss Wilhelminenberg Wien':48.2195,
       'Derag Livinghotel Kaiser Franz Joseph Vienna':48.245998,
       'NH Collection Barcelona Podium':41.3916,
       'City Hotel Deutschmeister':48.22088,
       'Hotel Park Villa':48.233577,
       'Cordial Theaterhotel Wien':48.209488,
       'Holiday Inn Paris Montmartre':48.888920,
       'Roomz Vienna':48.186605,
       'Mercure Paris Gare Montparnasse':48.840012,
       'Renaissance Barcelona Hotel':41.392673,
       'Hotel Advance':41.383308}
#longitude information of Hotels
loc_lng ={'Fleming s Selection Hotel Wien City':16.353479,
       'Hotel City Central':16.3799,
       'Hotel Atlanta':16.363449,
       'Maison Albar Hotel Paris Op ra Diamond':2.323358,
       'Hotel Daniel Vienna':16.3840,
       'Hotel Pension Baron am Schottentor':16.359819,
       'Austria Trend Hotel Schloss Wilhelminenberg Wien':16.2856,
       'Derag Livinghotel Kaiser Franz Joseph Vienna':16.341080,
       'NH Collection Barcelona Podium':2.1779,
       'City Hotel Deutschmeister':16.36663,
       'Hotel Park Villa':16.345682,
       'Cordial Theaterhotel Wien':16.351585,
       'Holiday Inn Paris Montmartre':2.333087,
       'Roomz Vienna':16.420643,
       'Mercure Paris Gare Montparnasse':2.323595,
       'Renaissance Barcelona Hotel':2.167494,
       'Hotel Advance':2.162828}
df['lat'] = df['lat'].fillna(df['Hotel_Name'].apply(lambda x: loc_lat.get(x)))
df['lng'] = df['lng'].fillna(df['Hotel_Name'].apply(lambda x: loc_lng.get(x)))
###save filling file
df.to_pickle('Filling_nans')
df = pd.read_pickle("Filling_nans")
print(df.shape)
print(df.Hotel_Name.describe())
