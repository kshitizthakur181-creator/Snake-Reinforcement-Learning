import torch 
import random 
import numpy as np 
from snake import SnakeGameAI,Direction,Point
from collections import deque


MAX_MEMORY = 100_000 
bATCH_SIZE = 1000
LR = 0.001



class Agent:
           
    def __init__(self):
           pass
    
    def get_state(self,game):
        pass
