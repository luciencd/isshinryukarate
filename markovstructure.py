import numpy as np
import random
import json
import pickle

class Item:
    def __init__(self):
        self.string = ""
        pass

class MarkovChain:
    def __init__(self):
        self.chain = []
        pass

##TODO: allow for n length chains in a new subclass.
##Should be possible using graph structure without changing interface
class MarkovArray:
    def __init__(self,list_of_states):
        self.array_of_states = []

    ##TODO: allow for n length chains
    def getChain(self,length):
        pass

    #Rating a given chain with a rating, to change the markov array.
    def rateChain(self,markov_chain,rating):
        pass

class MarkovArray2D(MarkovArray): #if randomly assigned, decay rate should make the thing stable
    def __init__(self,list_of_states):
        MarkovArray.__init__(self,list_of_states)
        self.dict_of_states = {}
        for i in range(len(list_of_states)):
            self.array_of_states.append(list_of_states[i])
            self.dict_of_states[list_of_states[i]] = i

        self.markovarray = np.ndarray(shape=(len(self.array_of_states),len(self.array_of_states)), dtype=float)

        for i in range(len(self.array_of_states)):
            for j in range(len(self.array_of_states)):
                self.markovarray[i][j] = 1.0


    def getStates(self):
        return self.array_of_states

    def getProbability(self,state):
        #get index of the state
        index = self.dict_of_states[state]
        return self.markovarray[index]

    def randomChain(self,length=2):
        return self.getChain(self.array_of_states[random.randrange(0,len(self.array_of_states))],length)


    def getChain(self,state,length=2):
        probabilities_array = self.getProbability(state)

        prob_sum = sum(probabilities_array)
        r = random.random()*prob_sum


        #print r
        low = 0
        high = probabilities_array[1]
        for i in range(len(probabilities_array)):
            low = high
            high = low+probabilities_array[i]
            if r >= low and r < high:
                break

        #print i
        return [state,self.array_of_states[i]]

    def rateChainAdd(self,markov_chain,rating):
        index1 = self.dict_of_states[markov_chain[0]]
        index2 = self.dict_of_states[markov_chain[1]]
        self.markovarray[index1][index2] += rating

    #Rating a given chain with a rating, to change the markov array.
    def rateChainMul(self,markov_chain,rating):
        index1 = self.dict_of_states[markov_chain[0]]
        index2 = self.dict_of_states[markov_chain[1]]

        self.markovarray[index1][index2] *= rating

    def rankChain(self,markov_chain_1,markov_chain_2):
        self.rateChainMul(markov_chain_1,1.5)
        self.rateChainMul(markov_chain_2,0.5)

    #TODO:make this return new markovstructure?
    #fear that making this permanent might screw stuff up later, but also cant just return naked array.
    def raiseMatrixPower(self,n):
        for i in range(n):
            self.markovarray = np.multiply(self.markovarray,self.markovarray)


    def exportToFile(self,filename):
        with open(filename, "w") as data_file:
            serialized = pickle.dump(self.markovarray, data_file) # protocol 0 is printable ASCII

    def importFromFile(self,filename):
        try:

            with open(filename) as data_file:
                data = pickle.load(data_file)
            self.markovarray = data
            return True
        except EOFError:
            print "EOFError"
            return False

    def printMatrix(self):
        np.set_printoptions(threshold='nan')
        #print self.markovarray
        for i in range(len(self.markovarray)):
            for j in range(len(self.markovarray[i])):
                print self.markovarray[i][j], " ",
            print "\n",
        np.set_printoptions(threshold=6)
