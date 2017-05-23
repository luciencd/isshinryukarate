from markovstructure import *
from loader import *
import unittest


class TestStringMethods(unittest.TestCase):

    def test_car_example(self):
        #create MarkovArray
        #create items
        print "test1"
        m2d = MarkovArray2D(["Normal","Broken"])
        #print m2d.getProbability("Normal")
        #print m2d.getProbability("Broken")
        #for i in range(10):
        #    print m2d.getChain("Normal",2)


    def test_single_move(self):
        print "test2"
        m2d = MarkovArray2D(["Normal","Broken"])
        m2d.rateChain(["Normal","Normal"],1)
        #print m2d.getProbability("Normal")
        #print m2d.getProbability("Broken")

        #for i in range(10):
        #    print m2d.getChain("Normal",2)


    def test_two_moves(self):
        print "test2"

        m2d = MarkovArray2D(loadStates("JSONMoves/simplemoves.json"))
        states = m2d.getStates()
        m2d.importFromFile("CachedArrays/array4.json")

        m2d.printMatrix()

        for i in range(0):
            first_state1,second_state1 = m2d.getStates()[random.randrange(0,len(states))],m2d.getStates()[random.randrange(0,len(states))]
            first_state2,second_state2 = m2d.getStates()[random.randrange(0,len(states))],m2d.getStates()[random.randrange(0,len(states))]

            print first_state1,second_state1, "OR",first_state2,second_state2
            key = raw_input("Which state is better, [1] or [2]?")

            if(key == "1"):
                m2d.rankChain([first_state1,second_state1],[first_state2,second_state2])
            else:
                m2d.rankChain([first_state2,second_state2],[first_state1,second_state1])

        m2d.exportToFile("array3.json")
        m2d.printMatrix()


        chainstart = m2d.randomChain()

        for i in range(10):
            chainstart = m2d.getChain(chainstart[1],2)
            print chainstart[0],", ",


if __name__ == '__main__':
    unittest.main()
