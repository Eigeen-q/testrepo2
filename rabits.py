import random
import pylab
import math

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    Prob_rabbit=1.0-(CURRENTRABBITPOP/MAXRABBITPOP)
    CURRENTRABBITPOP = CURRENTRABBITPOP * Prob_rabbit
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    Prob_fox_eat_rab = CURRENTRABBITPOP/MAXRABBITPOP
    prob_fox_birth=[]
    
    if CURRENTRABBITPOP >=10:
        num_rab_eaten = math.floor(CURRENTFOXPOP * Prob_fox_eat_rab)
        CURRENTRABBITPOP = CURRENTRABBITPOP-num_rab_eaten
        for i in range(CURRENTFOXPOP):
            prob_fox_birth.append(random.choice([1,0,0]))
        CURRENTFOXPOP = CURRENTFOXPOP + sum(prob_fox_birth)
    else:
        CURRENTFOXPOP = math.floor(9/10 * (CURRENTFOXPOP))
    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    for i in numSteps:
        rabbitGrowth()
        foxGrowth()
        
    return (CURRENTRABBITPOP,CURRENTFOXPOP)
