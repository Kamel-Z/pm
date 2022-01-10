import json
from urllib.request import urlopen
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame()

# import json
test = {}
df = pd.DataFrame()
df2=pd.DataFrame()

# store the URL in url as 
# parameter for urlopen


mois  = ["01","02","03","04","05","06","07","08","09","10","11","12"]
jour  = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
r = ["1","2","3",'4','5','6','7','8',"9"]
c = ["1","2","3",'4','5','6','7','8',"9"]

for i in mois:
  for ii in jour:
    for rr in r:
      for cc in c:
        url = "https://offline.turfinfo.api.pmu.fr/rest/client/7/programme/{}{}2021/R{}/C{}/participants".format(ii,i,rr,cc)
        try:
          response = urlopen(url)
          data_json = json.loads(response.read())
          df = pd.json_normalize(data_json['participants'])

          df2 = df2.append(df, ignore_index=True)
        except ValueError:
          print("course inconnu R{}/C{}".format(rr,cc))
