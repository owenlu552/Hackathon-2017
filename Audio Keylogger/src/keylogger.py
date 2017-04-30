#!/usr/bin/env python3

import argparse
import string
from features import *
from keystrokes import *
from data_labeler import *

from sklearn import svm

def keylogger(args):
	
	#training_keystrokes = keystroke_starts(args.training_wav)
	#training_features = extract_features(args.training_wav, training_keystrokes)
	training_features, training_keystrokes = get_training_set(args.training_wav, args.training_truth)
	input_keystrokes = keystroke_starts(args.input_wav)
	input_features = extract_features(args.input_wav, input_keystrokes)

	classifier = svm.SVC()
	classifier.fit(training_features, training_keystrokes)
	prediction = classifier.predict(input_features)

	print('Predicted sample: {}'.format(str(prediction)))


	


if __name__=="__main__":
	parser = argparse.ArgumentParser(description='Acoustic keylogger utility')
	parser.add_argument('training_wav')
	parser.add_argument('training_truth')
	parser.add_argument('input_wav')

	keylogger(parser.parse_args())