from keystrokes import keystroke_starts
from features import extract_features
import csv
from features import *
import numpy
from matplotlib import pyplot as plt

TIMING_MATCH_THRESHOLD = 2200

def get_training_set(wav_file, truth_file):

	key_idx = keystroke_starts(wav_file)

	
	truth = []
	expected_idx = []
	with open(truth_file, 'r') as f:
		reader = csv.reader(f)
		first_row = next(reader)
		truth.append(first_row[0])
		offset_idx = float(first_row[1])/1000*SAMPLE_RATE - key_idx[0]
		expected_idx.append(key_idx[0])
		
		for row in reader:
			truth.append(row[0])
			expected_idx.append(float(row[1])/1000*SAMPLE_RATE - offset_idx)

		
	key_idx_pruned = []
	truth_pruned = []
	exp_idx_pruned = []
	key_offset = 0
	exp_offset = 0
	for i in range(0,len(key_idx)):
		delta = key_idx[i+key_offset]-expected_idx[i+exp_offset]
		if delta > TIMING_MATCH_THRESHOLD:
			key_offset-=1
		elif delta < -TIMING_MATCH_THRESHOLD:
			exp_offset-=1
		else:
			key_idx_pruned.append(key_idx[i+key_offset])
			truth_pruned.append(truth[i+exp_offset])
			exp_idx_pruned.append(expected_idx[i+exp_offset])
	
	"""
	print(len(key_idx))
	print(len(key_idx_pruned))
	print(len(expected_idx))
	print(len(exp_idx_pruned))
	
	for i in range(0,len(key_idx_pruned)):
		print(exp_idx_pruned[i])
		print(key_idx_pruned[i])
		print('-')
	"""
		
	features = extract_features(wav_file, key_idx_pruned)
	return features, truth_pruned
	
