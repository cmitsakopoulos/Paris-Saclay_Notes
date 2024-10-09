# Machine Learning: Why?

* Develop predictive algorithms through machine learning to tackle new data. Use history to analyse the future: **prediction**.  
* Can be used for any bioinformatics requirement; examples include proteomics, protein-protein interactions.

# Next

* **Data** is a set of **objects** which are associated with **variables/attributes**.   
* **Types of attributes**:  
  * **Real value**: ex. A term that is continuous  
  * **Binary**: ex. True or False  
  * **Nominal**: aka categorical, belongs to a category.  
  * **Ordinal**: ex. An attribute which is gradual, low, high.  
* **Machine Learning** is an example of Artificial Intelligence, particularly, **numerical Artificial Intelligence.**  
* Machine learning; **optimise a performance criterion using prior data**:  
  * **Statistical methods to infer numerical patterns**.  
  * Classical methods (mathematical programming), amongst others, are used to train a model and following the generalisation theory, one aims to reduce error if applied to a general set of data  
* To properly teach a machine learning algorithm, the training data contains label data (metadata-the ones we want to predict), slowly and through repeated training with less and less labels in the training data, the model is brought to a level of **unsupervised learning**, where it can now predict label data to a satisfactory level of accuracy.   
* Keywords: **Supervised learning, Semi, Unsupervised, Reinforcement learning.**

# Unsupervised learning

* PCA, aka **Principal Component Analysis**, is a method of **dimensionality reduction** which aims to reduce the cluttering of data; think of it as downsampling a WAV to an MP3. You remove the noise/redundancy/irrelevance in the data.  
* **Clustering**: **Grouping data based on commonalities, subdividing them into groups**.  
  * Clusters have to be compact, aka **be very similar**, and have **distance** with each other, aka each “subgroup” must be **different enough**.  
  * Clustering is useful in order to more **easily uncover relationships between data points**, as well as serve as a point of **pre-processing, collecting data in groups to be fed into another algorithm.**  
    

# Distance functions

Given points A and B (and C), to represent their distance, one would show

d(A, B)

If  d(A, B) \< 0, it's **not possible**.

If  d(A, B) \= 0, SE: **isolation**.

If  d(A, B) \= d(B, A): **symmetry**.

If d(A, B) \<= d(A, C) \+ d(C, A): **triangular inequality**.

* Distance is a measure of **dissimilarity**, of how **far data is from each other**.   
* **Similarity** is a measure of **proximity**.  
* Distance **is inversely related** to **similarity**.  
* Similarity between an object and itself is the maximum, **isolation**.

Look up distance and data matrices. Additionally, brush up calculus basics. 

Look into the k-means algorithm. K represents the number of clusters, using a mean value of k-means, you connect the data points to a **mean** to which they are the most **similar to**. 

Look up the process of the k-mean algorithm, how the updating procedure works and learn to do it by hand.

K-means will **eventually converge** to the **optimum**.

