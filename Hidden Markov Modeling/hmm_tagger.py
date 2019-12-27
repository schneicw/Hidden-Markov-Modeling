import pickle
import nltk
import math 
import sys
import numpy as np

nltk.download('brown')
from nltk.corpus import brown


def viterbi(A(a_ij),B(b_j(o_t)),Obs(words w_1...w_T)):
    viterbi_matrix = [N+2][T]  #+2 for start and end state, T for length of sentence(timesteps), N for tag possibilities
    backpointer_matrix = [N+2][T]
    for state s in [1....,N]   # for each word in the sentence
        viterbi[s,1] = A[0][s] * B[s][o_j]
        backpointer[s,1] = 0
    for t in 2, ...T:   # for each time step
        for s in [1,...N]:  # for each potential tag in each time step 
            viterbi_matrix[s][t] = -inf
            for sprev in [1,...N]:
                vtj = viterbi_matrix[sprev][t-1] * A[sprev][s] * B[s][o_t]
                if vtj > viterbi_matrix[s][t]:
                    viterbi_matrix[s][t] = vtj
                    backpointer[s][t] = sprev
                    
    #termination step
    #F: Numeric index of final state (end of sentence)
    vit[T][F] = -inf
    for s in [1...N]:
        vf = vit[T-1][S]* a[S][F]
        if vf > vit[T][F]
            vit[T][F] = vf
            backpointer[T][F] = s
            
    # rebuilt most likely sequence using backpointers
    #return path
    


def viterbi(tagtagModel,wordtagModel, sentence):
    starttag = '<S>'
    viterbi_matrix = np.zeros((len(tagtagModel) + 2, len(sentence)))
    backpointer_matrix = np.zeros((len(tagtagModel) + 2, len(sentence)))
    for word in sentence:
        
    print (viterbi_matrix)



def main():
   # test = brown.tagged_sents(categories='news')[round(len(brown.tagged_sents(categories='news'))*.9):]
    sent = brown.tagged_sents(categories='news')[1]
    print(sent)
    fp = open(sys.argv[1],'rb')
    model = fp.read()
    a = pickle.loads(model)
    tagtag = a[0]
    tagword = a[1]
    viterbi(tagtag, tagword, sent)
    
if __name__ == '__main__':
    main()