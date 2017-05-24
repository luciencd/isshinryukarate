import sys
from markovstructure import *
from loader import *
import unittest
from gtts import gTTS
def training(iters):
    m2d = MarkovArray2D(loadStates("JSONMoves/simplemoves.json"))
    states = m2d.getStates()
    m2d.importFromFile("CachedArrays/array4.json")

    for i in range(iters):
        first_state1,second_state1 = m2d.getStates()[random.randrange(0,len(states))],m2d.getStates()[random.randrange(0,len(states))]
        first_state2,second_state2 = m2d.getStates()[random.randrange(0,len(states))],m2d.getStates()[random.randrange(0,len(states))]

        print first_state1,second_state1, "OR",first_state2,second_state2
        key = raw_input("Which state is better, [1] or [2]?")

        if(key == "1"):
            m2d.rankChain([first_state1,second_state1],[first_state2,second_state2])
        elif(key == "2"):
            m2d.rankChain([first_state2,second_state2],[first_state1,second_state1])
        elif(key == "wq"):
            break
        elif(key == "q"):
            return


    m2d.exportToFile("CachedArrays/array4.json")

def chain(length,power):

    m2d = MarkovArray2D(loadStates("JSONMoves/simplemoves.json"))
    states = m2d.getStates()
    m2d.importFromFile("CachedArrays/array4.json")
    m2d.raiseMatrixPower(power)

    chainstart = m2d.randomChain()
    giantstring = "Hello, I am the first AI Isshinryu Karate Helper. Rei... Hajime."
    for i in range(length):
        chainstart = m2d.getChain(chainstart[1],2)
        giantstring += str(chainstart[0])+"     "

    return giantstring



def main():
    if(sys.argv[0] == "-t"):
        training(sys.args[1])
    elif(sys.argv[0] == "-c"):
        print chain(sys.argv[1],sys.argv[2])
    elif(sys.argv[0] == "-s"):
        gs = chain(sys.argv[1],sys.argv[2])
        tts = gTTS(text=gs, lang='en', slow=False)
        tts.save(sys.argv[3])
    elif(sys.argv[0] == "-p"):
        printing()
    else:
        print chain(10,1)



if __name__=="__main__":
    main()
