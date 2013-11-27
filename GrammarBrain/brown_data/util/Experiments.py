from pybrain import TanhLayer, LSTMLayer
from GrammarBrain.BrownGrammarTrainer import BrownGrammarTrainer

default_dict = {
        'title'               : 'default dict title',
        'part'                : 'default part',
        'minim'               : 3,
        'maxim'               : 4,
        'outdim'              : 2,
        'hiddendim'           : [50],
        'train_time'          : 2,
        'medium'              : False,
        'hidden_type'         : LSTMLayer,
        'output_type'         : TanhLayer,
        'include_punctuation' : True,
        'include_numbers'     : True
}

def test_experiment_setup():
    test_dict = default_dict.copy()
    test_dict['hiddendim'] = [3]
    test_dict['maxim'] = 3
    gt = BrownGrammarTrainer(**default_dict)
    gt.timed_train()
    gt.make_csv_and_pickle()



if __name__ == '__main__':
    test_experiment_setup()
