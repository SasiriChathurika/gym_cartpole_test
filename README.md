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

_In my case I executed all these codes and commands in ```UBUNTU 22.04.4```_
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

_In my case I used the name ```cartpole_test.py```_
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

In most of the places they have just imported gym... But you should defenitely import it as ```import guymnasium as gym``` unless things won't go as expected 
```
from time import sleep
import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.evaluation import evaluate_policy
```
**Create the environments:**

Found that most of the developers used the ```render_mode = rg b_array```. But in my case it properly worked with ```render_mode = "human"```
```
env = gym.make("CartPole-v1", render_mode = "human")
```

**Create the number of Episodes you want to run:**
Change the value according to your preference
```
episodes =30
```
**Write the loops:**
```
for episode in range(1, episodes+1):
    state = env.reset()
    done = False
    score = 0

    while not done:
        
        action = env.action_space.sample()
        n_state, reward, done,trucated, info = env.step(action)
        score += reward
   
    env.render()
	    
    print('Episode:{} Score:{}'.format(episode, score))
	
env.close()
```

In here what is the **tricky part **is you should always wite ```env.render()``` **outside** the _while not done_ loop

**One more special thing** that most of you might have encountered while running CartPole is that you have written   ```n_state, reward, done, info = env.step(action)``` instead of writing ```n_state, reward, done,trucated, info = env.step(action)```

Hence make sure to include ```truncated```  within the elements.


This is how the code looks like when opened the python file in the text editor:
![Screenshot from 2024-03-26 22-32-21](https://github.com/SasiriChathurika/gym_cartpole_test/assets/79395595/1814dba1-101b-4aad-b262-e249f511701d)

# 4. Run your python file in the terminal

```
python3 cartpole_test.py
```
** ENJOY!!!**

You should see a window popped up like below...

![Screencastfrom26-03-24225358-ezgif com-video-to-gif-converter](https://github.com/SasiriChathurika/gym_cartpole_test/assets/79395595/723c6bba-034e-4fb9-aa87-232364b46c7d)
