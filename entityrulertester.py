


import time

start = time.time()


import spacy


import csv

mastertextlist=[]
DATASET=[]

testtext=[]
#for a quick test, put a resume onto the txt file and run this program.
with open('/test.txt', 'r', encoding='UTF8') as f:
    # using csv.writer method from CSV package
    read = csv.reader(f)

    for jj in read:
        if jj is not None:
            print(jj)
            for i in jj:
                if i is not None:
                    testtext.append(i)

print(testtext)
testtext=("").join(testtext)


##if you wish to test the trained mdel, load the model from here by pointint it to github_04-05 last model folder.


# point it to the rulebase_ner , this is the rule based pipeline(unoptimiised)
nlp = spacy.load("/rulebase_ner")

masterskill=[]

doc = nlp(testtext)

dict={}
skills=[]
entities=[]
results=[]




print(doc.ents)


##for visualisation purposes.
colors = {"skill": "linear-gradient(90deg, #aa9cfc, #fc9ce7)"}
options = { "ents": ["SKILL"], "colors": colors}
html=spacy.displacy.render(doc, style="ent", options=options,page="true")
file = open("C:/Users/wanho/PycharmProjects/sssssssssssssss/testingperformancescript/htmlentityruler.html","w",encoding='UTF8')
file.write(html)
file.close()



end = time.time()
print(end - start)




