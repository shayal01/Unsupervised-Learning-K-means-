# Unsupervised-Learning-(K-means)
## Abstract
The project implements the K-means algorithm on a given 2-D dataset ,with two
different strategies for choosing the initial cluster centers and also plot the objective
function value vs. the number of clusters.There are a total of 300 samples and 2 features per sample.
## Methodology
### STRATEGY 1
In this method, the initial centers for all the clusters are picked randomly from the
given samples.Then the centers are updated according to the k-means algorithm.We
are repeating this for a number of clusters ranging from 2-10.The objective function
is calculated and graph is plotted against the number of clusters.The expression for
the objective function is given below


$$ objective function = \Sigma_{i=1}^{k}\Sigma_{x \in D_{i}} ||x -\mu_{i}||^2 $$
![st2](https://user-images.githubusercontent.com/41173314/227815251-c92fb513-778d-44c6-bded-c39a5d069187.png)


Here $x$ is the sample and $D_{i}$ is the $i^{th}$ cluster and $\mu_{i}$ is the centroid of the $i^{th}$ cluster 

### STRATEGY 2
In this method,the initial centers are picked in a different way ,compared to strategy
1.Here the first center is picked randomly and for the $i^{th}$ center (i>1), a sample is 
chosen in such a way that the average distance of this chosen one to all the previous
(i-1) centers is maximal.The next steps are similar to strategy 1

### Results
The centroids are updated iteratively.The number of iteration is defined explicitly.and
it’s value is 9 because after 9 iterations the centroid of the clusters remains the same
.The objective function is calculated and graph is plotted against the number of
clusters for each strategy and is given below
<div align="center">
  <img src="https://user-images.githubusercontent.com/41173314/227815112-f0191b70-eaab-474d-85c3-325dfa0c229e.png" alt="alt text" width="300" height="200">
  <img src="https://user-images.githubusercontent.com/41173314/227815331-a0e102ce-35aa-4371-a678-0b4443365e97.png" alt="alt text" width="300" height="200">
</div>
As we can see from the above graphs,the value of the objective function decreases
with increase in the number of clusters. The value decreases slowly after the number
of clusters is 4.So by the elbow method,we can say that the optimal number of
clusters into which the data is clustered is 4 as per the above graph.

