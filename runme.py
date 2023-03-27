# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 10:18:09 2022

@author: shayal
"""
from scipy import io
import numpy as np

from scipy.spatial.distance import cdist 
from matplotlib import pyplot as plt
def stratergy_1(samples):       #function where all the centroids are randomly initiallized
    cost=[]
    for K in range(2,11):      #k is number of clusters and it ranges from 2 to 10
 
        mean=np.zeros((K,2),float)
       
    
        randomRow = np.random.randint(len(samples), size=K) #randomly selecting the initial centroids
        mean=samples[randomRow,:]                           #from the given samples
  
        dist=cdist(samples, mean ,'euclidean')    #calculating the distance between every sample and every centroid
                                                   
        samp = np.array([np.argmin(i) for i in dist]) #clustering each sample to it's corresponding means
        #loop for updating the centroids of the cluster
        for i in range(iter1):
           new_mean = []
           for j in range(K):
               temp = np.mean(samples[samp==j],axis=0,dtype=float) 
               new_mean.append(temp)
           new_mean = np.vstack(new_mean)
       
           dist=cdist(samples, new_mean ,'euclidean')    
           samp = np.array([np.nanargmin(i) for i in dist])
        #calculating the objective function
        s=0
        for j in range(K):
          dist=cdist(samples[samp==j], new_mean ,'euclidean')   
          dist=dist[:,j]
          dist=np.sum(np.square(dist)) 
          s+=dist
        cost.append(s)
    return cost     #returning the values of the objective function for different values of number of clusters

    
def stratergy_2(samples):  #function for strategy 2
    cost=[]
    for K in range(2,11):  
        
        mean=np.zeros((K,2),float)
       
    
        randomRow = np.random.randint(len(samples), size=1) #randomly selecting the first centroid from the given samples
        mean[0]=samples[randomRow,:]
       
        for i in range(1,K):
          dist=cdist(samples, mean[0:i,:] ,'euclidean')  #initializing the rest of the centroids using the strategy 2
          avg_dist=np.mean(dist,axis=1) 
          mean[i]=samples[np.argmax(avg_dist)]
        #the rest of the algorithm is same ad strategy 1
        dist=cdist(samples, mean ,'euclidean')    
    
        samp = np.array([np.argmin(i) for i in dist])
        for i in range(15):
           new_mean = []
           for j in range(K):
               temp = np.mean(samples[samp==j],axis=0,dtype=float) 
               new_mean.append(temp)
           new_mean = np.vstack(new_mean)
       
           dist=cdist(samples, new_mean ,'euclidean')    
           samp = np.array([np.nanargmin(i) for i in dist])

        s=0
        for j in range(K):
          dist=cdist(samples[samp==j], new_mean ,'euclidean')   
          dist=dist[:,j]
          dist=np.sum(np.square(dist)) 
          s+=dist
        cost.append(s)
    return cost      
    


data=io.loadmat(r"F:\sml\PROJ 2\AllSamples.mat")  #loading data from .mat file
all_samples=data["AllSamples"]    #loading data samples from the data file given


cost=[]
iter1=9                 #total number of iterations for updating the centroids

cost1=stratergy_1(all_samples)   #calling the function for inmplementing strategy 1
cost2=stratergy_2(all_samples)   #and 2
k=np.linspace(2,10,9)

#plotting the objective function v/s number of samples for both the strategies
a=plt.figure(1)
plt.plot(k,cost1)
plt.xlabel('NUMBER OF CLUSTERS')
plt.ylabel('OBJECTIVE FUNCTION')
plt.title('STRATEGY 1')

b=plt.figure(2)
plt.plot(k,cost2)
plt.xlabel('NUMBER OF CLUSTERS')
plt.ylabel('OBJECTIVE FUNCTION')
plt.title('STRATEGY 2 ')
a.show()
b.show()
