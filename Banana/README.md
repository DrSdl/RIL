**18.05.2019** This folder contains the solution to the "Banana Collector" project of Udacity's deep reinforcement learning nanodegree.

**19.05.2019**

## Project Details: ##
The “Banana Collector” [project](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Learning-Environment-Examples.md#banana-collector) consists of a single agent who must learn to move to as many as possible yellow bananas and avoid blue ones. The agent can move in two dimensions in a large but finite square world. It receives a reward of +1 for interaction with a yellow banana and -1 for hitting a blue one.

![](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/images/banana.png)

Watch this [video](https://www.youtube.com/watch?v=m7aOodyDlkk) to see how the agent experiences the environment or this [video](https://www.youtube.com/watch?v=heVMs3t9qSk) to see a multi-agent banana environment.

The state space of the agent consists of 37 continuous variables: the agent’s velocity (2) and its ray-based perception signals in the forward direction (35). The action space size is discrete and has four possibilities: move forward, move backward, move left or move right. The task is treated as an episodic task and if the average reward over 100 consecutive episodes is higher than +13 the task is solved. 

The “Banana Collector” environment is part of Unity’s [machine learning](https://unity3d.com/machine-learning) example [environments](https://github.com/Unity-Technologies/ml-agents). Agents can be trained using reinforcement learning, imitation learning, neuro-evolution, or other machine learning methods through a Python API.

In this repository we use a Q-network for reinforcement learning. This means that the agent is trained model-free; it solves the learning task directly using observations from within Unity’s environment without explicitly estimating the reward and transition dynamics from state to state. The algorithm also is off-policy by using an epsilon-greed policy that follows the greedy policy with probability (1-epsilon) and selects a random action with probability epsilon. Hence the agent explores the environment and only later updates the target policy after a batch of experiences have been collected.    

Firstly, our algorithm uses a technique called experience replay by storing a set of experiences in a replay memory and uses random sampling from it to create independent batches for Q-learning updates. This is best practice because owing to the strong correlations between consecutive samples learning would be inefficient. Randomizing the experiences breaks their correlations and therefore reduces the variance of the updates.

Secondly, our algorithm uses two independent neural networks as the function approximator for the Q-values. Initially, two Q networks: Q_target and Q_local are created and initialized with random weights. Every k updates Q_local is cloned to obtained Q_target. The latter is then kept constant and used as a reference for updating the weights of Q_local during the next k steps. Generating Q_target using an older set of parameters adds a delay between the time an update to Q_local is made and the time the update affects the targets, making oscillations much more unlikely.

The above-mentioned deep reinforcement techniques have first been successfully demonstrated in [“Human-level control through deep reinforcement learning”](https://web.stanford.edu/class/psych209/Readings/MnihEtAlHassibis15NatureControlDeepRL.pdf).


## Getting started: ##
Download the jupyter [notebook](https://github.com/DrSdl/RIL/blob/master/Banana/Navigation.ipynb).

You can also click on the [html version](https://github.com/DrSdl/RIL/blob/master/Banana/Navigation.html) to see the printout of the executed notebook.

The checkpoint of the trained network is [here](https://github.com/DrSdl/RIL/blob/master/Banana/checkpoint.pth).

## Instructions: ##
Open the notebook and type “Shift”+”Enter” to execute the notebook’s cells. 

If you have not done yet, please install the Unity ML-Agent environment as described [here](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Installation.md).

Depending on your platform, please download one of the prepared Banana environments:

•	Linux: click [here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux.zip)
•	Mac OSX: click [here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana.app.zip)
•	Windows (32-bit): click [here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86.zip)
•	Windows (64-bit): click [here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86_64.zip)
 
Finally, you need to update the “file_name” for the UnityEnvironment declaration in the second code cell of the notebook:

         •	Mac: "path/to/Banana.app" 

         •	Windows (x86): "path/to/Banana_Windows_x86/Banana.exe" 

         •	Windows (x86_64): "path/to/Banana_Windows_x86_64/Banana.exe" 

         •	Linux (x86): "path/to/Banana_Linux/Banana.x86" 

         •	Linux (x86_64): "path/to/Banana_Linux/Banana.x86_64" 

         •	Linux (x86, headless): "path/to/Banana_Linux_NoVis/Banana.x86" 

         •	Linux (x86_64, headless): "path/to/Banana_Linux_NoVis/Banana.x86_64"
