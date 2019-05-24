 ## MC Methods ##
One of the simplest learning strategy is to use the equiprobable random policy, use it to collect some episodes, and then consolidate the results to arrive at a better policy. The prediction problem in this context is: given a policy, how might the agent estimate the value function for that policy?

In MC prediction many episodes with a simple policy are collected. To populate a Q-table entry, the return (immediate reward plus all future rewards until the episode ends) that followed when the agent was in that state, and chose that action is recorded. In the event that the agent has selected the same action many times from the same state, we need only average the returns.

Every occurrence of a state in an episode is considered a visit to that state-action pair. And, in the event that a state-action pair is visited more than once in an episode, there are two options.

(1) __Every-visit MC Prediction :__
Average the returns following all visits to each state-action pair, in all episodes.

(2) __First-visit MC Prediction :__
For each episode, only the first visit to the state-action pair is considered.

Some more definitions:

A deterministic policy π(S) is a mapping from state S to action A. For each state it yields the action that the agent will choose while in state. In stochastic policy for each state S and action A there is a probability π(A∣S) that the agent chooses action A while in state S.

The state-value function for a policy π is denoted v(π). For each state it yields the expected return if the agent starts in state 
S and then uses the policy to choose its actions for all time steps: v(π,S)≐Eπ\[G(t)∣S(t)=S\].

The __Bellman expectation equation__ for v(π) is: v(π,S(t))=Eπ\[R(t+1)+γv(π,S(t+1))∣S(t)=S].

The __action-value function__ for a policy π is denoted q(π). For each state and action it yields the expected return if the agent starts in state S, takes action A and then follows the policy for all future time steps. That is, q(π,S,A)=Eπ\[G(t)∣S(t)=S,A(t)=A].

We refer to q(π,S,A) as the value of taking action A in state S under a policy π. G(t) is the return (discounted return) of all future actions after t, i.e. G(t)=R(t+1)+γR(t+2)+γγR(t+3)+...

When working with finite Markov decision process (MDP), the action-value function q(π) corresponding to a policy π can be estimated in a table known as a Q-table. This table has one row for each state and one column for each action. The entry in the s-th row and a-th column contains the agent's estimate for expected return that is likely to follow, if the agent starts in state s=S, selects action  a=A and then henceforth follows the policy π.

A policy is greedy with respect to an action-value function estimate Q if for every state it is guaranteed to select an action such that 
a=argmax(a∈A(S),Q(S,A)). A policy is ϵ-greedy with respect to an action-value function estimate Q if for every state with probability 
1−ϵ the agent selects the greedy action, and with probability ϵ, the agent selects an action uniformly at random from the set of available (non-greedy AND greedy) actions.

The constant-alpha method uses the following update for Q-table estimation: Q(S,A) <- Q(S,A) + α(G(t)-Q(S,A)).
If α=0, then the action-value function estimate is never updated by the agent. If α=1, then the final value estimate for each state-action pair is always equal to the last return that was experienced by the agent (after visiting the pair).

Smaller values for α encourage the agent to consider a longer history of returns when calculating the action-value function estimate. Increasing the value of α ensures that the agent focuses more on the most recently sampled returns.

## Temporal Difference Methods ##

Monte Carlo control methods require to complete an entire episode of interaction before updating the Q-table. Temporal Difference methods will instead update the Q-table after every time step. 

Sarsa(0) (or Sarsa) is an on-policy TD control method. It is guaranteed to converge to the optimal action-value function as long as the step-size parameter α is sufficiently small and ϵ is chosen to satisfy the Greedy in the Limit with Infinite Exploration (GLIE) conditions.

Sarsamax (or Q-Learning) is an off-policy TD control method. It is guaranteed to converge to the optimal action value function under the same conditions that guarantee convergence of the Sarsa control algorithm.

Expected Sarsa is an on-policy TD control method. It is guaranteed to converge to the optimal action value function under the same conditions that guarantee convergence of Sarsa and Sarsamax.

Sarsa and Expected Sarsa are both on-policy TD control algorithms. In this case, the same policy that is evaluated and improved is also used to select actions. Sarsamax is an off-policy method, where the (greedy) policy that is evaluated and improved is different from the policy that is used to select actions.

On-policy TD control methods (like Expected Sarsa and Sarsa) have better online performance than off-policy TD control methods (like Q-learning). Expected Sarsa generally achieves better performance than Sarsa.

__Sarsa__

Q(S(t),A(t)) <- Q(S(t),A(t)) + α( R(t+1) + γ Q(S(t+1),A(t+1)) - Q(S(t),A(t)) )

__Sarsamax__

Q(S(t),A(t)) <- Q(S(t),A(t)) + α( R(t+1) + γ max(A) Q(S(t+1),A) - Q(S(t),A(t)) )

__Expected Sarsa__

Q(S(t),A(t)) <- Q(S(t),A(t)) + α( R(t+1) + γ  Sum(A)π(A|S(t+1)) Q(S(t+1),A) - Q(S(t),A(t)) )


 ## Q-Networks ##
 
 How to use neural networks for reinforcement learning it not obvious. Overall, a Q-table is a table and not a network. Here comes
 the idea of function approximation: approximating a Q-table with the help of a NN. In [practice](https://storage.googleapis.com/deepmind-data/assets/papers/DeepMindNature14236Paper.pdf) this might look like this:
 As input to the network the representation of a state (i.e. pixels on a screen) is given. The NN outputs values for all the potential
 actions and the one with the highest value is chosen. [Here](https://deepmind.com/blog/deep-reinforcement-learning/) are more details from DeepMind. Also OpenAI has created a nice [webpage](https://openai.com/blog/spinning-up-in-deep-rl/) explaining deep reinforcement learning.
 
Training such a deep Q-table is prone to blow-ups. In principle a series of mini-episodes or (state,action,reward,next state) sequences are generated and are used for batch-wise training of the network. 
