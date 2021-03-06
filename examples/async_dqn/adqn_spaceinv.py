from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

try:
    import reinforceflow
except ImportError:
    import os.path
    import sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
    import reinforceflow
from reinforceflow.agents.async_dqn import AsyncDQNAgent
from reinforceflow.envs.env_factory import EnvFactory
from reinforceflow.core.policy import EGreedyPolicy
from reinforceflow.nets import DQNFactory
reinforceflow.set_random_seed(555)

env_name = 'SpaceInvaders-v0'
env = EnvFactory.make(env_name, use_smart_wrap=True)
steps = 80000000
agent = AsyncDQNAgent(env, net_factory=DQNFactory(), use_gpu=True)
policies = [EGreedyPolicy(eps_start=1.0, eps_final=final, anneal_steps=4000000)
            for final in [0.01, 0.01, 0.01, 0.1, 0.1, 0.1, 0.5, 0.5]]
agent.train(num_threads=8,
            render=False,
            steps=steps,
            optimizer='adam',
            learning_rate=0.00005,
            policy=policies,
            target_freq=40000,
            gamma=0.99,
            batch_size=5,
            log_freq=100000,
            log_dir='/tmp/reinforceflow/%s/async_dqn/adam/' % env_name)
