import string
from collections import Counter
import matplotlib.pyplot as plt
text=open('Text.txt',encoding='utf-8').read()
#print(text)
lowercase=text.lower()
#print(lowercase)
cleaned_text=lowercase.translate(str.maketrans('','',string.punctuation))
#print(cleaned_text)
tokenized_words=cleaned_text.split()
#print(tokenized_words)
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
final_words=[]
for word in tokenized_words:
    if word not in stop_words:
        final_words.append(word)
#print(final_words)
emotions_list=[]
with open('emotion.txt','r') as file:
    for lines in file:
        clear_lines=lines.replace("\n",'').replace("'",'').strip()
        word,emotion=clear_lines.split(':')

        if word in final_words:
            emotions_list.append(emotion)
#print(emotions_list)
w=Counter(emotions_list)
print(w)
fig,ax1=plt.subplots()
ax1.bar(w.keys(),w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()
