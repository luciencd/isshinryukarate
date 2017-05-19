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

        m2d = MarkovArray2D(loadStates("moves.json"))
        states = m2d.getStates()
        m2d.importFromFile("array2.json")

        m2d.printMatrix()

        for i in range(20):
            state1,state2 = m2d.getStates()[random.randrange(0,len(states))],m2d.getStates()[random.randrange(0,len(states))]
            print state1,state2
            key = raw_input("Is this a good move chain? [Y/N]")
            if(key == "Y"):
                m2d.rateChain([state1,state2],3)
            else:
                m2d.rateChain([state1,state2],0)

        m2d.exportToFile("array2.json")
        m2d.printMatrix()

        #for i in range(10):
        #   print m2d.randomChain()


if __name__ == '__main__':
    unittest.main()
