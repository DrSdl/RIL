import numpy as np
from collections import defaultdict

class Agent:

    def __init__(self, nA=6):
        """ Initialize agent.

        Params
        ======
        - nA: number of actions available to the agent
        """
        self.nA = nA
        self.Q = defaultdict(lambda: np.zeros(self.nA))
        self.gamma = 0.7
        self.alpha = 0.9
        self.i_episode = 1

    def select_action(self, state):
        """ Given the state, select an action.

        Params
        ======
        - state: the current state of the environment

        Returns
        =======
        - action: an integer, compatible with the task's action space
        """
        #print(self.Q[state])
        #print(self.i_episode)
        policy_s = self.epsilon_greedy_probs(self.Q[state], self.i_episode, 0.001)
        action = np.random.choice(np.arange(self.nA), p=policy_s)

        #return np.random.choice(self.nA)
        return action
    
    def step(self, state, action, reward, next_state, done):
        """ Update the agent's knowledge, using the most recently sampled tuple.

        Params
        ======
        - state: the previous state of the environment
        - action: the agent's previous choice of action
        - reward: last reward received
        - next_state: the current state of the environment
        - done: whether the episode is complete (True or False)
        """
        # self.Q[state][action] += 1
        policy_s = self.epsilon_greedy_probs(self.Q[next_state], self.i_episode, 0.001)
        self.Q[state][action] = self.update_Q(self.Q[state][action], np.dot(self.Q[next_state], policy_s), reward, self.alpha, self.gamma)
        if done:
            self.i_episode = self.i_episode + 1
        
        
    def epsilon_greedy_probs(self, Q_s, i_episode, eps=None):
        """ obtains the action probabilities corresponding to epsilon-greedy policy """
        epsilon = 1.0 / self.i_episode
        if eps is not None:
            epsilon = eps
        policy_s = np.ones(self.nA) * epsilon / self.nA
        policy_s[np.argmax(Q_s)] = 1 - epsilon + (epsilon / self.nA)
        return policy_s
    
    def update_Q(self, Qsa, Qsa_next, reward, alpha, gamma):
        return Qsa + (alpha * (reward + (gamma * Qsa_next) - Qsa))
