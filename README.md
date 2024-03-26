# How To Properly Run and Render Your First Open AI GYM CartPole Test
I've created this repository **for the Open AI Gym beginners who feel troubled while running the CartPole Test**. 👌️
It is not promised that this codes would properly work on the Jupyter Notebook. While I was running the same code on the Notebook only the Episodes and the respective Scores were printend, it did not render 🥲️

Keywords: how to fix gym cartpole no render 

**After lots of errors and hard encounters I rendered it finally 🥳️**

** You don't have to feel that pain..  I've got your back 🤗️**

_**The code can be found within the files above..._

I will guide you step by step how to run the code and try this test...

# 1. First things first
**You should have a Linux OS in a Dual-Boot or within a Virtual Environment**. 

_In my case I executed all these codes and commands in **UBUNTU 22.04.4**_
In your terminal run the following commands.

**Install Stable Baselines3:**
```
pip install stable-baselines3[extra]
```

**Install Open AI Gymnasium:**
```
pip install "gymnasium[all]"
```

# 2. Prepare your environment
**Create your python file:**

_In my case I used the name "cartpole_test.py"_
```
mkdir my_first_project
cd my_first_project
touch cartpole_test.py
```

**Open your python file and edit it:**
```
nano cartpole_test.py
```

# 3. Write the code in your python file

**Imports:**

In most of the places they have just imported gym... But you should defenitely import it as **import guymnasium as gym** unless things won't go as expected 
```
from time import sleep
import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.evaluation import evaluate_policy
```
**Create the environments:**

Found that most of the developers used the **render_mode = rgb_array** . But in my case it properly worked with **render_mode = "human"**
```
env = gym.make("CartPole-v1", render_mode = "human")
```

**Create the number of Episodes**
