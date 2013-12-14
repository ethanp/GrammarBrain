GrammarBrain
============

### A Recurrent Neural Network for Classifying English Sentence Grammaticality

The Paper
---------

#### Link to the paper [Building an English Grammar-Checker with a Recurrent Neural Network](https://www.dropbox.com/s/ps6qixxkoaljb74/Ethan%20Petuchowski%20%E2%80%94%20Neural%20Networks%20Project%20Paper%20GrammarBrain.pdf)

**Abstract**

In the face of the numerous theoretical challenges in training a neural network
to classify any given English sentence as being either grammatical or
ungrammatical, we train and compare a few configurations of Recurrent Neural
Networks on exactly that task. Sentences are encoded as sequences of vectors,
each denoting one word’s part of speech. The resulting network is surprisingly
effective at differentiating between grammatical and shuffled “word salad”
sentences double the length of those on which it is trained.

The Code
--------

### Dependencies

* [PyBrain](http://pybrain.org/)
* [SciPy](http://www.scipy.org/)
* [NLTK](http://nltk.org/)

### Experimenting

#### Make sure dependencies and installation is correct

`$ python GrammarBrain/brown_data/util/Experiments.py`

#### Write your own experiment

Follow the example of `GrammarBrain/brown_data/experiment_scripts/gen_error.py`,
which uses the dictionary from `GrammarBrain/brown_data/util/Experiments.py`

#### License

GrammarBrain can be downloaded, used, modified, etc., for any purpose.
