import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
import re
import pickle

file = '/home/prateek/major/onevsrest-SVM/updated_altered_train_100.csv'
df = pd.read_csv(file)
df = df[:80000]

all_tags = []
##for i in range(len(df)):
##	tag_set = (df["Tags"][i]).split(' ')
##	tags = tags + tag_set
##
##tags = nltk.FreqDist(tags)
##tags = tags.most_common(50)
##tags = [tags[i][0] for i in range(len(tags))]

classifier_f = open("tags","rb")
all_tags = pickle.load(classifier_f)
classifier_f.close()

print (len(all_tags))

stopwords = stopwords.words("english")
stopwords.append('.')
stopwords.append(',')
stopwords.append("I")
stopwords.append("'m")

rgx = re.compile('<.*?>\s*')

def body_token(boddy):
	boddy = boddy.lower()
	boddy = rgx.sub('',boddy)
	boddy = word_tokenize(boddy)
	body = []
	for w in boddy:
		if(w not in stopwords):
			body.append(w)
	return body

dic_num = {}
dic_den = {}


print (len(df))
for i in range(len(df)):
	tag_set = (df["Tags"][i]).split(' ')
	f = 0
	for tag in tag_set:
		if (tag in all_tags):
			if (not f == 1):
				f = 1
				words = body_token(df["Title"][i])
			for w in words:
				if((tag,w) in dic_num.keys()):
					dic_num[(tag,w)] += 1
				else:
					dic_num[(tag,w)] = 1
			if(tag in dic_den.keys()):
				dic_den[tag] += 1
			else:
				dic_den[tag] = 1



save_dictionary1 = open("dictionary1","wb")
pickle.dump(dic_num, save_dictionary1)
save_dictionary1.close()

save_dictionary2 = open("dictionary2","wb")
pickle.dump(dic_den, save_dictionary2)
save_dictionary2.close()
