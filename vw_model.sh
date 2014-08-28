#!/usr/bin/env bash
# The first argument is assumed to be the training file, and the second is assumed to be the test/validation file.
# Both files need to be in the label/feature format expected by vowpal wabbit for training and testing
# Example:
#     ./vw_model.sh train.txt test.txt

MODEL_OUTPUT='logreg.model'
TEST_PREDICTIONS=${2}.pred

# train the model
time vw -d $1 -f $MODEL_OUTPUT --loss_function logistic -c --power_t 0.5 --passes 5

# run it on a test/validation set and output the predictions
# this will output the log loss if run on the validation set (ie, if the 2nd argument has labels for each example)
# ignore the log loss output if run on a test set (ie, a file without labels)
# NOTE: the saved predictions need to be run through logit(.) to get probabilities!
time vw -t $2 -i $MODEL_OUTPUT --loss_function logistic -p $TEST_PREDICTIONS
