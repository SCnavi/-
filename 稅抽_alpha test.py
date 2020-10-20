#!/usr/bin/env python
# coding: utf-8

# In[29]:


import numpy as np
import pandas as pd


# In[30]:


popu = pd.read_excel('明細帳.xlsx')


# In[31]:


sample = popu[popu.PL == 'Y']


# In[32]:


sample["Abs amount"] = np.abs(sample["Amount"])


# In[33]:


sample.sort_values(by=["Account Number", "Abs amount"],ascending= [True, False], inplace= True)


# In[34]:


outcome = sample.groupby(by="Account Number").apply(lambda x:x.nlargest(3, "Abs amount", keep="first"))


# In[36]:


outcome.to_excel("sample.xlsx")

