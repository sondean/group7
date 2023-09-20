#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[7]:


url = "https://raw.githubusercontent.com/sondean/group7/main/BankChurners.csv"
df = pd.read_csv(url,encoding = 'unicode_escape')
df.head()


# In[ ]:




