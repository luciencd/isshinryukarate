from markovstructure import *
from loader import *
import unittest
from gtts import gTTS

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
        m2d.getProbability("Normal")
        m2d.getProbability("Broken")
        m2d.getChain("Normal",2)



    ##Hard to add deterministic tests to a probability model.

if __name__ == '__main__':
    unittest.main()
