# Twitter Sentiment Analysis using Python
### This is a project that analyses tweets for their sentiments(positive and negative). The tweets are downloaded using the Twitter API. The Model used in this project is a support-vector-machine(SVM) with a linear kernel.

Flow of the project:
* Downloading the training set
* Creating the test set based on the hashtag provided by the user
* Preprocessing all the tweets in test and training sets to remove unwanted portions like hashtags, urls, stopwords etc.
* Getting the finished datasets
* Vectorizing the tweets for analysing
* Creating a model that learns from the training set
* Pickling the model and vectorizer so that each time the project runs, the model does not have to be created each time and hence a lesser runtime.
* Predicting the sentiments of tweets present in the test set
* Getting the final results


