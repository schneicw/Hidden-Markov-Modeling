import pickle
import nltk
import math 
import sys
nltk.download('brown')
from nltk.corpus import brown


def sequence_prob(tagtagModel,wordtagModel, sentence):
    prevtag = '<s>'
    prob = 0 
    for word,tag in sentence:
        #print (prevtag,'p', tag, 't', tagtagModel[prevtag][tag])
        prob = prob + tagtagModel[prevtag][tag]
        #print (tag, 't', word, 'w', wordtagModel[tag][word])
        prob = prob + wordtagModel[tag][word]
        prevtag = tag
    return prob



def main():
    test = brown.tagged_sents(categories='news')[1]
    fp = open(sys.argv[1],'rb')
    model = fp.read()
    a = pickle.loads(model)
    tagtag = a[0]
    tagword = a[1]
    prob = sequence_prob(tagtag, tagword, test)
    print('The probability of the tag sequence for sentence 1 is :',prob)
    
if __name__ == '__main__':
    main()