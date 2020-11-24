#!/usr/bin/env python
# coding: utf-8

# In[2]:


from pulp import *


# In[6]:


customer =[1,2,3,4,5]
FACTORY=['FAC 1','FAC 2','FAC 3']
#parameters

demand ={ 1:80,
        2:270,
        3:250,
        4:160,
        5:180 }
actcost ={ 'FAC 1': 1000,
         'FAC 2':1000,
         'FAC 3':1000}

maxam ={ 'FAC 1': 500,
         'FAC 2':500,
         'FAC 3':500}
transp ={ 'FAC 1': {1:4,2:5,3:6,4:8,5:10},
         'FAC 2':{1:6,2:4,3:3,4:5,5:8},
         'FAC 3':{1:9,2:7,3:4,4:3,5:4}}


# In[8]:


prob=LpProblem("FacilityLocation",LpMinimize)


# In[11]:


serv_vars =LpVariable.dicts("service",
                           [(i,j) for i in customer
                                  for j in FACTORY],
                            0)


# In[12]:


use_var =LpVariable.dicts("UseLocation",FACTORY,0,1,LpBinary)


# In[14]:


prob +=lpSum(actcost[j]*use_var[j] for j in FACTORY) +lpSum(transp[j][i]* serv_vars[(i,j)] for j in FACTORY for i in customer)


# In[17]:


for i in customer:
    prob += lpSum(serv_vars[(i,j)] for j in FACTORY)== demand[i]
for j in FACTORY:
    prob+= lpSum(serv_vars[(i,j)] for i in customer) <=maxam[j]*use_var[j]


# In[19]:


for i in customer:
    for j in FACTORY:
        prob+= serv_vars[(i,j)] <=demand[i]*use_var[j]


# In[20]:


prob.solve()
print("STATUS",LpStatus[prob.status])


# In[25]:


TOL =0.00001
for i in FACTORY:
    if use_var[i].varValue > TOL:
        print("establish Facility at site",i)


# In[29]:


for v in prob.variables():
    print(v.name,"=",v.varValue)

#print optimal solution
print("cost of production in USD for 1 year ", value(prob.objective))


# In[ ]:




