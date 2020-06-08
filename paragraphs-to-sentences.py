#Sentence segmentation
# input = In the third category he included those Brothers (the majority) who saw nothing in Freemasonry but the external forms and ceremonies, and prized the strict performance of these forms without troubling about their purport or significance. Such were Willarski and even the Grand Master of the principal lodge. Finally, to the fourth category also a great many Brothers belonged, particularly those who had lately joined. These according to Pierre's observations were men who had no belief in anything, nor desire for anything, but joined the Freemasons merely to associate with the wealthy young Brothers who were influential through their connections or rank, and of whom there were very many in the lodge.Pierre began to feel dissatisfied with what he was doing. Freemasonry, at any rate as he saw it here, sometimes seemed to him based merely on externals. He did not think of doubting Freemasonry itself, but suspected that Russian Masonry had taken a wrong path and deviated from its original principles. And so toward the end of the year he went abroad to be initiated into the higher secrets of the order.What is to be done in these circumstances? To favor revolutions, overthrow everything, repel force by force?No! We are very far from that. Every violent reform deserves censure, for it quite fails to remedy evil while men remain what they are, and also because wisdom needs no violence. "But what is there in running across it like that?" said Ilagin's groom. "Once she had missed it and turned it away, any mongrel could take it," Ilagin was saying at the same time, breathless from his gallop and his excitement. 

#Solution:
#from nltk import tokenize
#p = input()
#sentence = tokenize.sent_tokenize(p)
#for i in sentence:
#    print(i)

#Alternate solution
text = input()

def add_spaces(t):
    t_list = []
    for i in range(len(t)-1):
        if t[i] in ['.', '?', '!'] and t[i+1] not in [' ', '"']:
            t_list.append(t[i])
            t_list.append(' ')
        else:
            t_list.append(t[i])
    t_list.append(t[-1])
    return ''.join(t_list)
 

def identify_dot(t):
    i = 0
    sentences = [[]]
    citation = False
    for j, word in enumerate(t[:-1]):
        if word[-1] in ['.', '?', '!']:
            if not citation:
                sentences[i].append(word)
                i += 1
                sentences.append([])
            else:
                sentences[i].append(word)
                citation = False
        else:
            #print word
            sentences[i].append(word)
            if word[-2:] == ",'":
                citation = True
    sentences[i].append(str(t[-1]))
    return sentences

text = add_spaces(text)
text_list = text.split()
sentences = identify_dot(text_list)
print(sentences)

for sentence in sentences:
    print(' '.join(sentence))