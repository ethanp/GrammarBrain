from numpy import argmax, array
from pybrain.tools.validation import ModuleValidator, SequenceHelper, Validator


def testOnSequenceData(module, dataset):
    """
    Fetch targets and calculate the modules output on dataset.
    Output and target are in one-of-many format. The class for each sequence is
    determined by argmax OF THE LAST ITEM IN THE SEQUENCE.
    """
    target = dataset.getField("target")
    output = ModuleValidator.calculateModuleOutput(module, dataset)

    # determine last indices of the sequences inside dataset
    ends = SequenceHelper.getSequenceEnds(dataset)

    class_output = array([argmax(output[end]) for end in ends])
    class_target = array([argmax(target[end]) for end in ends])

    return Validator.classificationPerformance(class_output, class_target)
