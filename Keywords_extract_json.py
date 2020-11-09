import nltk
import RAKE
import operator
import json

stop_dir = nltk.corpus.stopwords.words('english')
keywords = ""
rakeObj = RAKE.Rake(stop_dir)

# Opening & loading  json file. Define the encoding. Otherwise, you may get an error that some chars are undefined.
with open('csvjson.json', encoding="utf8") as f:
  jobs = json.load(f)

def Sort_Tuple(tup) :
    tup.sort(key = lambda x: x[1])
    return tup

# Gets each job object. Iterate through the job's description and 
# filters the keywords for us. Only 10 most relevant are chosen.
# The special character \n is replaced with white space because 
# the webcrawled data contained this chars and keywords did not look good.
def Extract_Keywords(): 
  for job in jobs:
    separate_job_descr = job['description_text']
    filtered_data = separate_job_descr.replace("\n", " ")
    keywords = Sort_Tuple(rakeObj.run(filtered_data))[-10:]
    print("keywords: ", keywords, "\n")

Extract_Keywords()
# To do
# add the column for keywpos
# write this column in Florian's file
# rewrite it for csv file
f.close()