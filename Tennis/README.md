## Tennis 

**14.07.2019** This folder contains the solution to the "Collaboration" project of Udacity's deep reinforcement learning nanodegree.

**15.07.2019**

## Project Details ##

The "Tennis collaboraton" [project](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Learning-Environment-Examples.md#Tennis) 
is one of Unity's example environments for deep reinforcement learning. For the purpose of the Udacity nanodegree program the environment
has been slightly adapted. For more information about Unity's ML-agents please see [here](https://blogs.unity3d.com/2017/09/19/introducing-unity-machine-learning-agents/).

It is a two-player game where agents control rackets to bounce a ball over a net. The objective is 
to bounce ball between one another while not dropping or sending the ball out of bounds.

![](https://github.com/DrSdl/RIL/blob/master/Tennis/tennis.png)

Each agent has access to 8 variables corresponding to position and velocity of ball and the racket. Overall 24 observations are available
for each agent. The action space consists of 2 variables for each agent: movement toward net or away from net, and jumping.
A video of the agents playing can be found [here](https://www.youtube.com/watch?v=tr3Vv3ya0UQ), for example.

If an agent hits the ball over the net, it receives a reward of +0.1. If an agent lets a ball hit the ground or hits the ball
out of bounds, it receives a reward of -0.01. Thus the goal of each agent is to keep the ball in play. The task is
episodic and learning is considered completed if the agents get an average score of +0.5 (over 100 consecutive episodes). Specifically,
after each episode the sum of rewards of each agent is calculated and the maximum of the two sums is taken. This is defined
as the score per episode.

In this project we have used a Mulit-agent DDPG (deep deterministic policy gradient) algorithm. 
Quick facts about DDPG are explained [here](https://spinningup.openai.com/en/latest/algorithms/ddpg.html)
and about MADDPG [here](https://arxiv.org/abs/1706.02275) or [here](https://arxiv.org/abs/1509.02971). OpenAI also release
a sample code for MADDPG [here](https://github.com/openai/maddpg).
 
## Getting started: ##
Download the jupyter [notebook](https://github.com/DrSdl/RIL/blob/master/Tennis/Tennis.ipynb). The original notebook from Udacity's course is [here](https://github.com/udacity/deep-reinforcement-learning/tree/master/p3_collab-compet).

You can also click on the [html version](https://github.com/DrSdl/RIL/blob/master/Tennis/Tennis.html) to see the printout of the executed notebook.

The checkpoints of the trained network is [here (actor)](https://github.com/DrSdl/RIL/blob/master/Tennis/checkpoint_actor1.pth).
and [here (critic)](https://github.com/DrSdl/RIL/blob/master/Tennis/checkpoint_critic1.pth).

The original implementation of the DDPG network is based on Udacity's solution for the Bipedal [agent](https://github.com/udacity/deep-reinforcement-learning/tree/master/ddpg-bipedal).

## Instructions: ##
In order to run the Tennis environment standalone on your PC or Laptop the following steps are necessary:

(1) Download Udacity's deep-reinforcement-learning repository from github [here](https://github.com/udacity/deep-reinforcement-learning).

(2) Download the Tennis environment, depending on your operating system as follows:

•	Linux: click [here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis_Linux.zip)
•	Mac OSX: click [here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis.app.zip)
•	Windows (32-bit): click [here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis_Windows_x86.zip)
•	Windows (64-bit): click [here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis_Windows_x86_64.zip)

(3) You now have the following two files:

![](https://github.com/DrSdl/RIL/blob/master/Tennis/download_files.jpg)

(4) Unzip the drlnd master and go to the p3_collab-compet directory in the drlnd directory. Also, unzip the "Tennis_Windows_x86_64.zip", for example and put it into this director, too. You should now see the following files and directory:

![](https://github.com/DrSdl/RIL/blob/master/Tennis/tennis_dir.jpg)

(5) You need to install a couple of dependencies. Go to the directory with name "python" in drlnd:

![](https://github.com/DrSdl/RIL/blob/master/Tennis/dir_python.jpg)

(6) I am using the Anaconda environment. From an anaconda shell execute "pip install ." in this directory. Specifically this
will install the Unity environment needed by the Tennis environment.

![](https://github.com/DrSdl/RIL/blob/master/Tennis/anaconda_install.jpg)

(7) Finally, we need to create a python drlnd kernel for this particular dependency. This is done with 

"python -m ipykernel install --user --name drlnd --display-name "drlnd""

![](https://github.com/DrSdl/RIL/blob/master/Tennis/drlnd_kernel.jpg)

(8) We now activate the drlnd environment from an anaconda shell with "activate drlnd"

(9) Please open a jupyter nodebook: type "jupyter notebook". A browser window opens. Under menu "Kernel" do "Change Kernel" to drlnd.

![](https://github.com/DrSdl/RIL/blob/master/Tennis/drlnd_notebook.jpg)

(10) You can now start executing the code cells by typing “Shift”+”Enter”. In the second code cell of the notebook you still must insert the path to the Tennis environment exe-file downloaded above:

![](https://github.com/DrSdl/RIL/blob/master/Tennis/2ndcell_notebook.jpg)

(11) Now, let's start coding!

![](https://github.com/DrSdl/RIL/blob/master/Tennis/coding_notebook.jpg)


