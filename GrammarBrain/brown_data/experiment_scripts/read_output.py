import csv
from GrammarBrain.brown_data.experiment_scripts import EXPERIMENT_RESULT_PATH

epoch, train, test, validation = None, None, None, None


for i in range(1,5):
    input_path = EXPERIMENT_RESULT_PATH + ('First Real Experiment/part_%d.txt' % i)
    with open(input_path, 'rb') as txt:
        lines = txt.readlines()

        # get list of total errors
        total_errors = ['BPTT Errors']
        for line in lines:
            if 'Total error:' in line:
                total_errors.append(float(line.split(' ')[2]))

        # get list of (epoch, train, test, validation) errors
        train_errors = [('Epoch', 'Training Error', 'Test Error', 'Validation Error')]
        for line in lines:

            if 'epoch' in line:
                epoch = int(line.split(' ')[1])

            if 'TRAINING' in line:
                train = float(line.split(' ')[2])

            if 'TEST' in line:
                test = float(line.split(' ')[2])

            if 'VALIDATION' in line:
                validation = float(line.split(' ')[2])

                assert epoch and train and test and validation, 'What??'

                train_errors.append((epoch, train, test, validation))
                epoch, train, test, validation = None, None, None, None



    output_path = EXPERIMENT_RESULT_PATH + ('First Real Experiment/part_%d.csv' % i)
    with open(output_path, 'wb') as output:
        w = csv.writer(output)

        for e in total_errors:
            w.writerow([e])

        w.writerow([''])

        for e in train_errors:
            w.writerow(e)
