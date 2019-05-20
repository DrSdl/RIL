## MC methods ##
One of the simplest learning strategy is to use the equiprobable random policy, use it to collect some episodes, and then consolidate the results to arrive at a better policy. The prediction problem in this context is: given a policy, how might the agent estimate the value function for that policy?

In MC prediction many episodes with a simple policy are collected. To populate a Q-table entry, the return (immediate reward plus all future rewards until the episode ends) that followed when the agent was in that state, and chose that action is recorded. In the event that the agent has selected the same action many times from the same state, we need only average the returns.

Every occurrence of a state in an episode is considered a visit to that state-action pair. And, in the event that a state-action pair is visited more than once in an episode, there are two options.

(1) __Every-visit MC Prediction :__
Average the returns following all visits to each state-action pair, in all episodes.

(2) __First-visit MC Prediction :__
For each episode, only the first visit to the state-action pair is considered.
