# NOTE: n.reset() will clear the history of the network

###########################################################################################
''' -- SAVING AND RELOADING TRAINED PYBRAINS -- '''
# http://stackoverflow.com/questions/6006187/how-to-save-and-recover-pybrain-traning/6009051
# "PyBrain's Neural Networks can be saved and loaded using either
#     python's built in pickle/cPickle module,
#            or
#     by using PyBrain's XML NetworkWriter."
'''
# Using pickle

from pybrain.tools.shortcuts import buildNetwork
import pickle

net = buildNetwork(2,4,1)

fileObject = open('filename', 'w')

pickle.dump(net, fileObject)

fileObject.close()

fileObject = open('filename','r')
net = pickle.load(fileObject)

Note cPickle is implemented in C, and therefore should be much faster than pickle.
Just import and use cPickle instead.

# Using NetworkWriter

from pybrain.tools.shortcuts import buildNetwork
from pybrain.tools.xml.networkwriter import NetworkWriter
from pybrain.tools.xml.networkreader import NetworkReader

net = buildNetwork(2,4,1)

NetworkWriter.writeToFile(net, 'filename.xml')
net = NetworkReader.readFrom('filename.xml')
'''
