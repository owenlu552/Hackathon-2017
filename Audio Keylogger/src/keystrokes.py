from scipy.io import wavfile
from scipy import signal
from numpy import mean, std

from matplotlib import pyplot as plt

def keystroke_starts(wav_filename):
	
	c_minFreqHz = 400
	c_maxFreqHz = 12000

	freq, data = wavfile.read(wav_filename)
	
	# select only the left channel for now
	leftData = data[:,0]
	numSamples = len(data)

	#

	# coefficients = abs(fft.rfft(data))
	# frequencies = fft.rfftfreq(numSamples, 1/freq)
	# frequencies = [(i,f) for i,f in enumerate(frequencies) if c_minFreqHz < f < c_maxFreqHz]
	# plt.plot([f[1] for f in frequencies], coefficients[[f[0] for f in frequencies]])
	# plt.show()
	# energy = sum(coefficients[[f[0] for f in frequencies]])

	# print(energy)

	f, t, Sxx = signal.spectrogram(leftData, fs=freq, nperseg=440)

	freqs = [(index, freq) for index, freq in enumerate(f) if c_minFreqHz < freq < c_maxFreqHz]
	energies = [sum(col) for col in zip(*Sxx[[f[0] for f in freqs]])]
	threshold = mean(energies) + 1.5*std(energies)
	#plt.plot(t, energies)
	energies = [(i,e) for i, e in enumerate(energies) if e > threshold]
	print(len(energies))
	print(t[[e[0] for e in energies]])

	#plt.plot(t[[e[0] for e in energies]],[e[1] for e in energies])
	#plt.show()

	return (freq*(t[[e[0] for e in energies]])).tolist()




	# for e in energies:
	# 	wavfile.write(str(e[0]) + '.wav', freq, data[range(freq*t[e[0]], freq*t[e[0]])])
	# 	print(t[e[0]])
	# #for i in range(100,200):
	#	plt.plot([f[1] for f in freqs], Sxx[[f[0] for f in freqs], i])
	#lt.show()





if __name__=="__main__":
	wav_filename = "../resources/abc.wav"
	starts = keystroke_starts(wav_filename)
	print(starts)

