## MC methods ##
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

We refer to q(π,S,A) as the value of taking action A in state S under a policy π.
