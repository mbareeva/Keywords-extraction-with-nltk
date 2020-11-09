
# import operator
import nltk
import RAKE
import operator
import csv

stop_dir = nltk.corpus.stopwords.words('english') + ['arggis', 'others', 'us', 'plus', 'like']
keywords = []
rakeObj = RAKE.Rake(stop_dir)

def Sort_Tuple(tup) :
    tup.sort(key = lambda x: x[1])
    return tup

def Extract_Keywords(job_descrip): 
    filtered_data = job_descrip.replace("\n", " ")
    keywords = Sort_Tuple(rakeObj.run(filtered_data))[-10:]


with open('csv.csv', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            #find only job description info.
            filtered_data = row[8].replace("\n", " ")
            #list of all keywords per row.
            keys = Sort_Tuple(rakeObj.run(filtered_data))[-10:]
            tuple_elements = []
            #extract keywords from list of tuples w/o scores
            for a_tuple in keys:
                tuple_elements.append(a_tuple[0])
            keywords.append(tuple_elements)
      
csvfile = open('new_csv.csv','w', encoding ="utf8", newline='')
fieldnames = ["job_title", "job_location", "company_name", "job_summary", "post_date", "extract_date", "job_salary", "posting_url", "description_text", "keys"]
obj = csv.DictWriter(csvfile, fieldnames = fieldnames)
#write in the row "Keys" the keywords for each row
for k in keywords:
    print('Groups: ', k)
    obj.writerow({"keys" : k})
csvfile.close()
#Error: The keys will be appended to the next rows, and dont write it in
#existent entries.