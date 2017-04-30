import numpy
import matplotlib.pyplot as plt
import scipy.io
import struct
import librosa.feature
import librosa.display
import wave


#FFT Parameters

#frequency range: 400Hz to 12,000Hz
SAMPLE_RATE = 44100 #Hz
NYQUIST_RATE = SAMPLE_RATE//2
LOW_FREQ = 400 #lowest frequency we care about (Hz)
HIGH_FREQ = 12000 #highest freqeuncy we care about (Hz)

NUM_BINS = 16

FFT_WINDOW_SIZE = SAMPLE_RATE//100
MFCC_STEP = SAMPLE_RATE//400
MFCC_NUM_STEPS = 16
MFCC_NUM_COEFF = 16
MEL_BANDS = 32

#returns a list containing one feature vector for each key press
#key_idx is a list of indices marking the start of a key press
def extract_features(wav_file, key_idx):
	audio = wave.open(wav_file, 'rb')
	key_vectors = []
	for idx in key_idx:
		audio.setpos(int(idx))
		sample_bytes = audio.readframes(MFCC_NUM_STEPS*MFCC_STEP+FFT_WINDOW_SIZE)
		samples = decode_bytes(sample_bytes,0)
		key_vectors.append(MFCC_vector(samples))
	return key_vectors
		
#returns a feature vector list of lists of MFCC coefficients over time
def MFCC_vector(samples):
	length = len(samples)
	samples -= sum(samples)//length
	m = librosa.feature.mfcc(y=samples, sr=SAMPLE_RATE, n_mfcc=MFCC_NUM_COEFF, n_fft=FFT_WINDOW_SIZE, hop_length=MFCC_STEP, n_mels=MEL_BANDS, fmin=400, fmax=12000)
	
	"""
	plt.figure(figsize=(10, 4))
	librosa.display.specshow(m, x_axis='time')
	plt.colorbar()
	plt.title('MFCC')
	plt.tight_layout()
	plt.show()
	"""
	return m


#takes audio data samples (integer) and computes FFT features
#byte data should be in the format returned by Wave_read.readframes(n)
def FFT_vector(samples):
	fft = numpy.fft.rfft(samples)
	fft_mag = numpy.absolute(fft)
	fft_len = len(fft_mag)
	
	#convert bins to discrete time
	dt_bins = [0]*NUM_BINS
	dt_delta = int((HIGH_FREQ - LOW_FREQ)/NYQUIST_RATE * fft_len/NUM_BINS)
	dt_low = int(LOW_FREQ/NYQUIST_RATE * fft_len)
	
	fft_features = [0]*NUM_BINS
	fft_sum = 0
	for i in range(0,NUM_BINS):
		start_idx = dt_low + i * dt_delta
		dt_bins[i] = start_idx
		fft_features[i] = sum(fft_mag[start_idx:start_idx + dt_delta])
		fft_sum += fft_features[i]
	
	for i in range(0,NUM_BINS):
		fft_features[i] /= fft_sum
	
	plt.plot(fft_mag)
	plt.show()
	return fft_features
	
	
#converts a byte array (16bit stereo) into numpy array (16 bit mono)
#channel is 0 or 1
#byte array should be in the format returned by Wave_read.readframes(n)
def decode_bytes(byte_array, channel):
	length = len(byte_array)//4
	data = numpy.zeros(length, dtype=numpy.int16)
	for i in range(0,length):
		frame = byte_array[i*4 + channel*2:i*4+2+channel*2]
		sample = struct.unpack("<h", frame)[0]
		data[i] = sample
	return data
	
	
def test_FFT():
	len = 4000
	audio = wave.open('C:/Users/Owen/Documents/GitHub/Hackathon 2017/Audio Keylogger/resources/single_key.wav', 'rb')
	sample_bytes = audio.readframes(len)
	samples = decode_bytes(sample_bytes,0)
	FFT_vector(samples)
	
def test_MFCC():
	len = 4000
	audio = wave.open('C:/Users/Owen/Documents/GitHub/Hackathon 2017/Audio Keylogger/resources/single_key.wav', 'rb')
	sample_bytes = audio.readframes(len)
	samples = decode_bytes(sample_bytes,0)
	print(MFCC_vector(samples[100:2000]))
	audio.close()
