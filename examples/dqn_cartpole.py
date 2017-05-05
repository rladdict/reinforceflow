from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

import tensorflow as tf
import reinforceflow
from reinforceflow.agents.dqn_agent import DQNAgent
from reinforceflow.nets import mlp
from reinforceflow.envs import EnvFactory
from reinforceflow.core.policy import EGreedyPolicy
from reinforceflow.core.experience import ExperienceReplay
reinforceflow.set_random_seed(321)


env = EnvFactory.make('CartPole-v0')
# or:
# env = gym.make('CartPole-v0')
opt = tf.train.RMSPropOptimizer(learning_rate=0.0001)
steps = 2000000
agent = DQNAgent(env, net_fn=mlp, opt=opt)
agent.train(max_steps=steps,
            log_dir='/tmp/reinforceflow/%s/rms/' % env.spec.id[:-3],
            render=True,
            target_freq=5000,
            experience=ExperienceReplay(size=5000, batch_size=32, min_size=500),
            policy=EGreedyPolicy(eps_start=1.0, eps_final=0.1, anneal_steps=30000))
