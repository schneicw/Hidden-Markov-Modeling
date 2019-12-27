import pickle
import nltk
import math 
nltk.download('brown')
from nltk.corpus import brown
# 2 dimensional dictionary 
# P(NN|DT) = Acount[DT][NN]/sum(Acount[DT].values())

def build_model(train, test): #list of lists(sentences) of tuples                            
    Acount = {} # 2D dictionary for tag to tag counts
    Bcount = {} # 2d dictionary for tag to word count
    tag_tag_prob = {}
    for sentence in train:
        prevtag = '<s>'
        for w,t in sentence:
            if t not in Bcount:
                Bcount[t] = {}
            if w not in Bcount[t]:
                 Bcount[t][w] = 1
            else:
                 Bcount[t][w] += 1
                    
            if prevtag not in Acount:   
                Acount[prevtag] = {}
            if t not in Acount[prevtag]:
                Acount[prevtag][t] = 1
            else:
                Acount[prevtag][t] += 1
            prevtag = t
    #print(Acount)
    
    
    for sentence in test:
        for word, tag in sentence:
            if tag not in Bcount:
                Bcount[tag] = {}
            if word not in Bcount[tag]:
                if '<UNK' not in Bcount[tag]:
                    word = '<UNK>'
                    Bcount[tag][word] = 1
                else:
                    word = '<UNK>'
                    Bcount[tag][word] += 1

    
    
    for tag1 in Acount.keys():
        count = 0
        for tag2 in Acount[tag1].keys():
            count += Acount[tag1][tag2]
        #print(count)
        for tag2 in Acount[tag1].keys():
            replace = math.log(Acount[tag1][tag2] / count)
            Acount[tag1][tag2] = replace
            
    for tag1 in Bcount.keys():
        count = 0
        for tag2 in Bcount[tag1].keys():
            count += Bcount[tag1][tag2]
        #print(count)
        for tag2 in Bcount[tag1].keys():
            replace = math.log(Bcount[tag1][tag2] / count)
            Bcount[tag1][tag2] = replace
    print (Bcount)
    return Acount, Bcount

def main():
    data = brown.tagged_sents(categories='news')[0:round(len(brown.tagged_sents(categories='news'))*.9)]
    test = brown.tagged_sents(categories='news')[round(len(brown.tagged_sents(categories='news'))*.9):]
    #print(round(len(brown.tagged_sents(categories='news'))*.9))
    print(len(data))
    #test =  brown.tagged_sents(categories='news')[3]
    #print(test)
    tagModel, wordModel = build_model(data, test)
    #sequence_prob(tagModel, wordModel, fp)
    #print(len(tagModel))
    dictlist = [tagModel, wordModel]
    #print(tagModel)
    
    pickle.dump(dictlist,open('model.dat',"wb+"))
   # pickle.dump(wordModel,open('model.dat',"wb"))
    #tagModel = str(tagModel)
   # wordModel = str(wordModel)
    #tagModel = bytes(tagModel,'utf-8')
    #wordModel = bytes(wordModel,'utf-8')
    #file = open('model.dat', "wb+")
    #file.write(tagModel)
    #file.write(bytes("end-of-tagModel",'utf-8'))
    #file.write(wordModel)
    
    
if __name__ == '__main__':
    main()