## Taxi-v2 ##

OpenAI's taxi-v2 environment is described [here](https://github.com/openai/gym/blob/master/gym/envs/toy_text/taxi.py). The challenge is based on a publication by [Tom Dietterich](https://arxiv.org/pdf/cs/9905014.pdf).

    The Taxi Problem
    from "Hierarchical Reinforcement Learning with the MAXQ Value Function Decomposition"
    by Tom Dietterich.
    
    Description:
    There are four designated locations in the grid world indicated by R(ed), B(lue), G(reen), and Y(ellow). When the episode starts, 
    the taxi starts off at a random square and the passenger is at a random location. The taxi drive to the passenger's location,
    pick up the passenger, drive to the passenger's destination (another one of the four specified locations), and then drop off 
    the passenger. Once the passenger is dropped off, the episode ends.
    
    Observations: 
    
    There are 500 discrete states since there are 25 taxi positions, 5 possible locations of the passenger (including the case when 
    the passenger is the taxi), and 4 destination locations. 
    
    Actions: 
    There are 6 discrete deterministic actions:
    - 0: move south
    - 1: move north
    - 2: move east 
    - 3: move west 
    - 4: pickup passenger
    - 5: dropoff passenger
    
    Rewards: 
    There is a reward of -1 for each action and an additional reward of +20 for delievering the passenger. 
    There is a reward of -10 for executing actions "pickup" and "dropoff" illegally.
    
    Rendering:
    - blue: passenger
    - magenta: destination
    - yellow: empty taxi
    - green: full taxi
    - other letters (R, G, B and Y): locations for passengers and destinations
    actions:
    - 0: south
    - 1: north
    - 2: east
    - 3: west
    - 4: pickup
    - 5: dropoff
    
    state space is represented by:
        (taxi_row, taxi_col, passenger_location, destination)

The environment looks like this:
![](https://github.com/DrSdl/RIL/blob/master/Taxi/taxi-v2-environment.png)
    
My solution on Udacity's workspace looked like this:
![](https://github.com/DrSdl/RIL/blob/master/Taxi/taxi-v2-solution.png)
