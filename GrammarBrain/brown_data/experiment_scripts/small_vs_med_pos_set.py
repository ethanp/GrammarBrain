from GrammarBrain.BrownGrammarTrainer import BrownGrammarTrainer
from GrammarBrain.brown_data.util.Experiments import default_dict

def small_set():
    small_dict = default_dict.copy()
    small_dict['title'] = 'SvsM1'
    small_dict['part'] = 'small'
    small_dict['maxim'] = 7
    small_dict['train_time'] = 50
    small_dict['include_punctuation'] = False
    small_dict['include_numbers'] = False
    small_gt = BrownGrammarTrainer(**small_dict)
    small_gt.timed_train(s=2)
    small_gt.make_csv_and_pickle()

def med_set():
    med_dict = default_dict.copy()
    med_dict['title'] = 'SvsM1'
    med_dict['include_punctuation'] = False
    med_dict['include_numbers'] = False
    med_dict['maxim'] = 7
    med_dict['train_time'] = 50

    #### THE PART THAT'S DIFFERENT ###
    ##################################
    med_dict['part'] = 'med'
    med_dict['medium'] = True
    ##################################

    med_gt = BrownGrammarTrainer(**med_dict)
    med_gt.timed_train(s=2)
    med_gt.make_csv_and_pickle()


def small_set_flex():
    small_dict = default_dict.copy()
    small_dict['title'] = 'SvsM1'
    small_dict['part'] = 'small_flex'
    small_dict['maxim'] = 7
    small_dict['train_time'] = 40
    small_gt = BrownGrammarTrainer(**small_dict)
    small_gt.timed_train(s=2)
    small_gt.make_csv_and_pickle()

def med_set_flex():
    med_dict = default_dict.copy()
    med_dict['title'] = 'SvsM1'
    med_dict['maxim'] = 7
    med_dict['train_time'] = 40

    #### THE PART THAT'S DIFFERENT ###
    ##################################
    med_dict['part'] = 'med_flex'
    med_dict['medium'] = True
    ##################################

    med_gt = BrownGrammarTrainer(**med_dict)
    med_gt.timed_train(s=2)
    med_gt.make_csv_and_pickle()

if __name__ == '__main__':
    med_set_flex()