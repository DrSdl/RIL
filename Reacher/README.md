## Reacher 

**11.07.2019** This folder contains the solution to the "Continuos Control" project of Udacity's deep reinforcement learning nanodegree.

**12.07.2019**

## Project Details ##

The "Reacher Contiuous Control" [project](https://gym.openai.com/envs/Reacher-v2/) is one of OpenAI's benchmarks for reinforcement 
learning.
In its simplest form a single agent is required to follow a moving target with its robotic arm. It is a double-jointed arm which should follow 
as precisely as possible the targel location. The goal is to maintain the arm's position at the target location as many time steps as possible.

In this project the reacher environment is simulated with Unity's ML-Agent [toolkit](https://blogs.unity3d.com/2017/09/19/introducing-unity-machine-learning-agents/).

![](https://github.com/DrSdl/RIL/blob/master/Reacher/one_arm.jpg)

The agent observes 33 variables corresponding to position, rotation, velocity and angular velocities of its arm. Each action state consists
of a vector of dimension 4 corresponding to the torque applied to the two joints of the arm. A reward if +0.1 is given for each step
that the agent's hand is in the target sphere. Unity's original documentation of the Reacher environment can be found [here](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Learning-Environment-Examples.md#Reacher) 
and [here](https://www.youtube.com/watch?v=2N9EoF6pQyE).

Unity's Reacher environment also allows more than one agent being connected to a brain. This version is useful for algorithms that use
multiple copies of the same agent do distribute the task of accumulating experience.

![](https://github.com/DrSdl/RIL/blob/master/Reacher/many_arms.jpg)

In this project we have used a a DDPG (deep deterministic policy gradient) algorithm. Quick facts about DDPG [are](https://spinningup.openai.com/en/latest/algorithms/ddpg.html):

•	DDPG is an off-policy algorithm.

•	DDPG can only be used for environments with continuous action spaces.

•	DDPG can be thought of as being deep Q-learning for continuous action spaces.
 
DDPG is an algorithm which concurrently learns a Q-function and a policy. It uses off-policy data and the Bellman equation 
to learn the Q-function, and uses the Q-function to learn the policy. Overall four neural networks are used: 
a Q network, a deterministic policy network, a target Q network, and a target policy network.

Concerning the Q network the actor directly maps states to actions instead of outputting the probability distribution 
across a discrete action space.  
 
Two more tricks are used:

**Replay buffer:** This is the set of previous experiences. In order for the algorithm to have stable behavior, the replay 
buffer should be large enough to contain a wide range of experiences, but it may not always be good to keep everything. 
If you only use the very-most recent data, you will overfit to that and things will break; if you use too much experience, 
you may slow down your learning. This may take some tuning to get right.

**Target network:** The target networks are time-delayed copies of the mother networks
which slowly track the learned networks. This improves the stability of the whole learning process.
In methods that do not use target networks, the updated networkw weights are interdependent on the values 
calculated by the network itself, which makes it prone to divergence.
 
## Getting started: ##
Download the jupyter [notebook](https://github.com/DrSdl/RIL/blob/master/Reacher/Reacher.ipynb). The original notebook from Udacity's course is [here](https://github.com/udacity/deep-reinforcement-learning/tree/master/p2_continuous-control).

You can also click on the [html version](https://github.com/DrSdl/RIL/blob/master/Reacher/Reacher.html) to see the printout of the executed notebook.

The checkpoints of the trained network is [here (actor)](https://github.com/DrSdl/RIL/blob/master/Reacher/checkpoint_actor.pth).
and [here (critic)](https://github.com/DrSdl/RIL/blob/master/Reacher/checkpoint_critic.pth).

The solution for the DDPG network is based on Udacity's solution for the Bipedal [agent](https://github.com/udacity/deep-reinforcement-learning/tree/master/ddpg-bipedal).

## Instructions: ##
Open the notebook and type “Shift”+”Enter” to execute the notebook’s cells. 

If you have not done yet, please install the Unity ML-Agent environment as described [here](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Installation.md).

Depending on your platform, please download one of the prepared Reacher environments (one agent):

•	Linux: click [here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher_Linux.zip)
•	Mac OSX: click [here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher.app.zip)
•	Windows (32-bit): click [here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher_Windows_x86.zip)
•	Windows (64-bit): click [here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher_Windows_x86_64.zip)
 
 The many agent environments have been prepared here:
 
•	Linux: click [here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Linux.zip)
•	Mac OSX: click [here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher.app.zip)
•	Windows (32-bit): click [here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Windows_x86.zip)
•	Windows (64-bit): click [here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Windows_x86_64.zip)
 

Finally, you need to update the “file_name” for the UnityEnvironment declaration in the second code cell of the notebook:

         •	Mac: "path/to/Reacher.app" 

         •	Windows (x86): "path/to/Reacher_Windows_x86/Reacher.exe" 

         •	Windows (x86_64): "path/to/Reacher_Windows_x86_64/Reacher.exe" 

         •	Linux (x86): "path/to/Reacher_Linux/Reacher.x86" 

         •	Linux (x86_64): "path/to/Reacher_Linux/Reacher.x86_64" 

         •	Linux (x86, headless): "path/to/Reacher_Linux_NoVis/Reacher.x86" 

         •	Linux (x86_64, headless): "path/to/Reacher_Linux_NoVis/Reacher.x86_64"
