
# coding: utf-8

# In[2]:

def a(): #moves to s' with reward 0
    states.append(1)
    rewards.append(0)
    actions.append("a")
    
def b(): #keeps it in s with reward 1
    states.append(0)
    rewards.append(1)
    actions.append("b")
    
def s_prime(): #moves from s' to s with reward 10
    states.append(0)
    rewards.append(10)
    actions.append("c")

#logic: since a rational agent would want to maximise the rewards
# it's much better to go from s to s' because the reward is 10.
# but if the time is close to T and it is at state 0 (beginning)
# it's better to take action b to get one more point
def action(current_state, time, T):
    if current_state == 1:
        s_prime()
    elif time == (T - 1):
        b()
    else:
        a()
                  
def run(time, T):
    while time < T:
        action(states[time], time, T)
        time += 1
        
    print "states:", states
    print "actions:", actions
    print "total reward:", sum(rewards)

#running the code:

time = 0
states = [0]
rewards = [0]
actions = []
run(time, 10)

time = 0
states = [0]
rewards = [0]
actions = []
run(time, 11)

# Q1: the two times when the rational action sequence differs is when the time 
# is odd or even. If it is odd, the sequence ends at action b; whereas an 
# even time would end at action c.

# Q2: the rational action sequence would depend on whether the T provided is odd
# or even: if it is even, it oscillates between a & c; if odd, it oscillates 
# between a & c but always ends at b.

#Q3: Maybe a possible system would be automated sellers at an entertainment park.
# Say said park closes at 6pm, and has 2 rides that last 30 minutes, and 1 that 
# lasts 5 minutes. After 5.30pm, the park may no longer open the 30 minute rides
# but still have the 5 minute one available to generate more profit.


# In[ ]:




# In[ ]:



