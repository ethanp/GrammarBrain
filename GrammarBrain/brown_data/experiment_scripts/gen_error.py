from GrammarBrain.BrownGrammarTrainer import BrownGrammarTrainer
from GrammarBrain.brown_data.util.Experiments import default_dict

gen_dict = default_dict.copy()
gen_dict['title'] = 'Gen Error 4 to 8'
gen_dict['minim'] = 4
gen_dict['maxim'] = 8
gen_dict['include_punctuation'] = False
gen_dict['include_numbers'] = False
gen_dict['gen_len'] = 20
gen_dict['train_time'] = 40

def gen_error_1():
    gen_dict_1 = gen_dict.copy()
    gen_dict_1['part'] = 1
    gt = BrownGrammarTrainer(**gen_dict_1)
    gt.timed_train(s=4)
    gt.make_csv_and_pickle()

def gen_error_2():
    gen_dict_2 = gen_dict.copy()
    gen_dict_2['part'] = 2
    gen_dict_2['include_punctuation'] = True
    gen_dict_2['include_numbers'] = True
    gt = BrownGrammarTrainer(**gen_dict_2)
    gt.timed_train(s=4)
    gt.make_csv_and_pickle()

def gen_error_3():
    gen_dict_3 = gen_dict.copy()
    gen_dict_3['part'] = 3
    gen_dict_3['medium'] = True
    gt = BrownGrammarTrainer(**gen_dict_3)
    gt.timed_train(s=4)
    gt.make_csv_and_pickle()

def gen_error_4():
    gen_dict_4 = gen_dict.copy()
    gen_dict_4['part'] = 4
    gen_dict_4['medium'] = True
    gen_dict_4['include_punctuation'] = True
    gen_dict_4['include_numbers'] = True
    gen_dict_4['gen_len'] = 30
    gt = BrownGrammarTrainer(**gen_dict_4)
    gt.timed_train(s=4)
    gt.make_csv_and_pickle()

if __name__ == '__main__':
    gen_error_4()
