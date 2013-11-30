from GrammarBrain.BrownGrammarTrainer import BrownGrammarTrainer
from GrammarBrain.brown_data.util.Experiments import default_dict


def try_gen_error():
    gen_dict = default_dict.copy()
    gen_dict['title'] = 'Gen Error Trial'
    gen_dict['minim'] = 4
    gen_dict['maxim'] = 4
    gen_dict['include_punctuation'] = False
    gen_dict['include_numbers'] = False
    gen_dict['gen_len'] = 8
    gt = BrownGrammarTrainer(**gen_dict)
    gt.timed_train()
    gt.make_csv_and_pickle()


if __name__ == '__main__':
    try_gen_error()
