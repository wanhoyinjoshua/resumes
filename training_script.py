


import spacy
from tqdm import tqdm

import csv
import random
import math
import json


mastertextlist=[]
DATASET=[]

import os
count=0

for item in tqdm(os.listdir("C:/Users/wanho/PycharmProjects/sssssssssssssss/resumecontentfolder/resumes_corpus")):

   
   split_tup = os.path.splitext(item)

   if split_tup[1] =='.txt':

       with open(os.path.join("C:/Users/wanho/PycharmProjects/sssssssssssssss/resumecontentfolder/resumes_corpus", item), 'r') as f:
           text = f.read()

           mastertextlist.append(text)







print(len(mastertextlist))

###########################################################################################################

def train_test_split(data, test_size, random_state):

    random.Random(random_state).shuffle(data)
    test_idx = len(data) - math.floor(test_size * len(data))
    train_set = data[0: test_idx]
    test_set = data[test_idx: ]

    return train_set, test_set

train_data, test_data = train_test_split(mastertextlist, test_size = 0.3, random_state = 100)


print(len(train_data))

print(len(test_data))


###########################################################################################################





def entityclassify(TRAIN_DATA):
    # Load a pipeline and create the nlp object
    DATASET=[]
    ##point it to the model last folder in github0405
    nlp = spacy.load("/github_04_05/model/last")
    masterskill=[]
    for i in tqdm(range(len(TRAIN_DATA))):

        print("entry")
        tempinfo=[]
        try:
            doc = nlp(TRAIN_DATA[i])
        except:
            try:
                doc = nlp(TRAIN_DATA[i])
            except:
                continue
        dict={}
        skills=[]
        entities=[]
        results=[]

        for ent in doc.ents:
            if ent.label_=='SKILL':


                entities.append((ent.start_char,ent.end_char,ent.label_))
            if len(entities)>0:
                try:
                    results=[TRAIN_DATA[i],{"entities":entities}]
                except:
                    results = [TRAIN_DATA[i], {"entities": entities}]

        if results!= []:
            print(results)
            print(doc.ents)
            tempent=[]
            for b in doc.ents:
                b= b.text.lstrip()
                b=b.rstrip()
                tempent.append(b)

            print (tempent)
            entss= list(set(tempent))
            print(entss)
            skilldict={"Skills": "{}".format(entss)}

            y = json.dumps(skilldict)


            DATASET.append([results,y,TRAIN_DATA[i]])



    print(len(DATASET))
    return DATASET


train_data=entityclassify(train_data)
test_data=entityclassify(test_data)

resultslist=[]
for result, ent, doc in train_data:
    resultslist.append([doc,ent])
for result, ent, doc in test_data:
    resultslist.append([doc,ent])



print(len(train_data))
print(len(test_data))
traindatalist=[]
devdatalist=[]
for i in train_data:
    print(i[0])
    traindatalist.append(i[0])

for i in test_data:
    print(i[0])
    devdatalist.append(i[0])


with open('githubcompiledresume.csv', 'w', encoding='UTF8', newline='') as f:
    # using csv.writer method from CSV package
    write = csv.writer(f)


    write.writerows(resultslist)






from spacy.tokens import DocBin



nlp=spacy.blank(("en"))

def create_trainingdata(TRAIN_DATA):
    db = DocBin()



    for text, annot in tqdm(TRAIN_DATA):
        # print("spancount")
        doc = nlp.make_doc(text)
        ents = []
        for start, end, label in annot["entities"]:
            span = doc.char_span(start, end, label=label, alignment_mode="contract")

            print("actual span {}", format(span))
            if span is None:
                pass
            else:
                ents.append(span)
        doc.ents = ents

        db.add(doc)
    return (db)





newtrain = create_trainingdata(traindatalist)
newdev= create_trainingdata(devdatalist)

newtrain.to_disk("C:/Users/wanho/PycharmProjects/sssssssssssssss/attempttrain1/newnew/github/traindata1.spacy")
newdev.to_disk("C:/Users/wanho/PycharmProjects/sssssssssssssss/attempttrain1/newnew/github/devdata1.spacy")











