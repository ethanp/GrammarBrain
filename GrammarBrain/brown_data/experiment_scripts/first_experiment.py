from GrammarBrain.BrownGrammarTrainer import BrownGrammarTrainer
from GrammarBrain.brown_data.util.Experiments import default_dict


''' test the effect of including numbers and/or punctuation '''
# TODO note that this doesn't include questions or exclamations


def both():
    both_dict = default_dict.copy()
    both_dict['title'] = 'First Real Experiment'
    both_dict['part'] = '1'
    both_dict['maxim'] = 20
    both_dict['train_time'] = 200
    both_gt = BrownGrammarTrainer(**both_dict)
    both_gt.timed_train(s=4)
    both_gt.make_csv_and_pickle()

def no_punct():
    num_dict = default_dict.copy()
    num_dict['title'] = 'First Real Experiment'
    num_dict['part'] = '2'
    num_dict['maxim'] = 20
    num_dict['train_time'] = 200
    num_dict['include_punctuation'] = False
    num_gt = BrownGrammarTrainer(**num_dict)
    num_gt.timed_train(s=4)
    num_gt.make_csv_and_pickle()

def no_num():
    punct_dict = default_dict.copy()
    punct_dict['title'] = 'First Real Experiment'
    punct_dict['part'] = '3'
    punct_dict['maxim'] = 20
    punct_dict['train_time'] = 200
    punct_dict['include_numbers'] = False
    punct_gt = BrownGrammarTrainer(**punct_dict)
    punct_gt.timed_train(s=4)
    punct_gt.make_csv_and_pickle()

def none():
    none_dict = default_dict.copy()
    none_dict['title'] = 'First Real Experiment'
    none_dict['part'] = '4'
    none_dict['maxim'] = 20
    none_dict['train_time'] = 200
    none_dict['include_punctuation'] = False
    none_dict['include_numbers'] = False

    none_gt = BrownGrammarTrainer(**none_dict)
    none_gt.timed_train(s=4)
    none_gt.make_csv_and_pickle()
