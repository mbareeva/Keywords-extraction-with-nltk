# just copied example from https://pypi.org/project/rake-nltk/#description
# import nltk
# from rake_nltk import Rake
# r = Rake() # Uses stopwords for english from NLTK, and all puntuation characters.
# r.extract_keywords_from_text(description)
# result = r.get_ranked_phrases() # To get keyword phrases ranked highest to lowest.
# print(result)

# import operator
import nltk
import RAKE
import operator
import json

stop_dir = "SmartStoplist.txt"
keywords = ""
rakeObj = RAKE.Rake(stop_dir)
openingdata = open("csvjson.json", encoding="utf8")
with open('csvjson.json', encoding="utf8") as f:
  jobs = json.load(f)

  
def Sort_Tuple(tup) :
    tup.sort(key = lambda x: x[1])
    return tup

def Extract_Keywords(): 
  for job in jobs:
    separate_job_descr = job['description_text']
    filtered_data = separate_job_descr.replace("\n", " ")
    keywords = Sort_Tuple(rakeObj.run(filtered_data))[-10:]
    print("keywords: ", keywords)

Extract_Keywords()
openingdata.close()