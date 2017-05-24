# Isshinryu Markov Matrix Assistant.


## What is Isshinryu Karate?

Isshinryu Karate is a Japanese martial art developed in 1956 on the island of Okinawa by Master Tatsuo Shimabuku. He was an innovator who made a bunch of logical improvements to the Karate styles of the time. He taught this new style to many, including 5 American marines stationed at the island after World War 2. Today, Isshinryu Karate is a karate style taught in many Dojos in America.

I have studied under Sensei Rimmer, Taylor and Etzel at the Isshinryu Karate Klub of Troy at RPI. I am currently a brown belt.

## What does Alexa Isshinryu Karate Assistant do?

Alexa Isshinryu Karate Assistant creates a string of moves that flow well together, which can be vocalized, for you to practice sparring.

The skill is useful for people who want randomness included in their training. Currently, I have taught the model through a reinforcement training interface on the command line. In the future, I would like to connect the interface to an Alexa to improve the accuracy of the Markov Matrix.

I want to make it clear that this project should not be taken too seriously in your martial arts training, and a Sensei is always best for teaching you their style of martial arts.

## What is a Markov Chain?

"A Markov chain is a type of Markov process that has either discrete state space or discrete index set (often representing time), but the precise definition of a Markov chain varies.[3] For example, it is common to define a Markov chain as a Markov process in either discrete or continuous time with a countable state space (thus regardless of the nature of time),[4][5][6][7] but it is also common to define a Markov chain as having discrete time in either countable or continuous state space (thus regardless of the state space)"
-Wikipedia

(Someone make a pull request that adds an actual good markov chain definition)

## What is a Markov Matrix?

"In mathematics, a Markov Matrix is a square matrix used to describe the transitions of a Markov chain. Each of its entries is a nonnegative real number representing a probability. It has found use throughout a wide variety of scientific fields, including probability theory, statistics, mathematical finance and linear algebra, as well as computer science and population genetics. The stochastic matrix was first developed by Andrey Markov at the beginning of the 20th century."
-Wikipedia

(Again, sorry that these definitions are so dense.)

## The Rules Of Isshinryu Karate.

In Isshinryu Karate, there are many "Rules" which guide the fighting, stance and motion aspects of the style. These range from optimal foot position, how blocking should be done, what type of attacks should follow others. The major ones are listed below.

An arm blocking should block on the lead leg side.
Attacks must alternate between right and left side.
The leg responsible for a kick must start from the back position.
There must be an economy of motion; moves that take less energy, less motion are preferred.
Fancy attacks are discouraged, but a diversity of simple moves is optimal.

Many rules include how you should act if an opponent is sparring with you, but because this is for self training, they are not included in the model(they would also be very difficult to implement).

## Subclassing.
Someone needs to do a pull request to create a new N-length markov matrix.

## Linear Algebra stuff

I got a C in linear Algebra, which is a good sign: it means I know enough to not implement the matrix math on my own. It will be all done using numpy.


-In order to skip ahead some of the training time, you can use a function to take the dot power of the matrix, to accentuate the probabilities and get better results sooner.
