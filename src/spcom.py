import numpy as np
import numpy.matlib
import scipy
from scipy import signal

def glottalPulse(fs, T1=0.004, T2=0.002):
    t1 = np.arange(0, T1, 1/fs)
    g1 = 0.5*(1 - np.cos(2*np.pi*t1/2/T1))
    t2 = np.arange(T1, T1 + T2, 1/fs)
    g2 = np.cos(2*np.pi*(t2 - T1)/4/T2)
    return np.hstack((g1, g2))

def freqz_two_tube(f,rL,rG,r1,L,c,L1L2):
    return 0.5*(1+rG)*(1+rL)*(1*r1)*np.exp(-2j*np.pi*f*L/c)/ \
        (1+r1*rG*np.exp(-2j*np.pi*f*2*L1L2/(L1L2+1)*L/c)+ \
         r1*rL*np.exp(-2j*np.pi*f*2/(1+L1L2)*L/c)+ \
         rL*rG*np.exp(-2j*np.pi*f*2*L/c))

def twoTubeSynth(fs, f0=100, L=0.176, c=352, rL=0.7, rG=1, a1a2=1/8, L1L2=1.2):
    r1 = (1-a1a2)/(1+a1a2)
    g = glottalPulse(fs)
    imp_len = 1/f0
    nimp = int(np.round(imp_len*fs/2))*2
    imp = np.zeros(nimp)
    imp[0] = 1
    x_imp = np.matlib.repmat(imp, 1, int(round(1/imp_len)))
    y_glottal = signal.lfilter(g, 1, x_imp)
    f = np.arange(0, int(y_glottal.shape[1]/2))
    V = freqz_two_tube(f,rL,rG,r1,L,c,L1L2)
    S_glottal = np.fft.rfft(y_glottal)
    S = S_glottal*np.append(V, 0)
    return np.fft.irfft(S)[0,:]

def cepstrum(S):
    LS = np.log(np.abs(S))
    return np.fft.irfft(LS)

def liftering(in_ceps, order=14):
    out_ceps = in_ceps.copy()
    out_ceps[order+1:-order] = 0
    return out_ceps

def cepstrumEnvelope(S, order=14):
    return np.real(np.fft.rfft(liftering(cepstrum(S), order)))

def fftCepstrumEnvelope(x, order=14):
    nFFT = len(x)
    S = np.fft.rfft(x*np.hanning(nFFT))
    return cepstrumEnvelope(S)

def hz2mel(freq):
    return 1127*np.log(1 + freq/700)

def mel2hz(mel):
    return (np.exp(mel/1127) - 1)*700

def melbank(fs=16000, nfft=512, nbank=40, lower=0, upper=8000):
#    fs = 16000 if len(args) == 0 else args[0]
#    upper = fs/2 if len(args) < 5 else args[4]
#    lower = 0 if len(args) < 4 else args[3]
#    nbank = 40 if len(args) < 3 else args[2]
#    nfft = 512 if len(args) < 2 else args[1]

    f = np.linspace(0, fs/2, int(nfft/2)+1)

    mel_s_w = np.zeros((nbank, int(nfft/2)+1))
    mel_w_len1 = int(np.floor(400/3/(fs/nfft)))
    mel_w_inc1 = np.linspace(0, 1, int(mel_w_len1/2)+1)
    mel_w_dec1 = np.linspace(1, 0, int(mel_w_len1/2)+1)
    if mel_w_len1 % 2 == 1:
        mel_w_tri1 = np.hstack((mel_w_inc1, mel_w_dec1))
    else:
        mel_w_tri1 = np.hstack((mel_w_inc1, mel_w_dec1[1:]))
    mel_w_tri_n1 = mel_w_tri1/np.sum(mel_w_tri1)
    mel_c_idx1 = np.arange(mel_w_len1/2, 13 * mel_w_len1/2, mel_w_len1/2).astype(int)
    for w_idx1 in np.arange(len(mel_c_idx1)):
        idx1 = int(mel_c_idx1[w_idx1] - mel_w_len1/2)
        mel_s_w[w_idx1, idx1:(idx1 + mel_w_len1 +1)] = mel_w_tri_n1

    mel_upper = hz2mel(upper)
    mel_lower = hz2mel(f[mel_c_idx1[-1]])
    mel_step = (mel_upper - mel_lower)/(nbank + 1 - len(mel_c_idx1))
    mel_c_idx2 = np.round(mel2hz(np.arange(mel_lower, mel_upper+1, mel_step))/(fs/2)*(nfft/2)).astype(int) 
    for w_idx2 in np.arange(len(mel_c_idx2)-2):
        c1 = mel_c_idx2[w_idx2]; c2 = mel_c_idx2[w_idx2 + 1]; c3 = mel_c_idx2[w_idx2 + 2]
        mel_s_w[w_idx2 + w_idx1 + 1, c1:(c2 + 1)] = np.linspace(0, 1, c2 - c1 + 1)
        mel_s_w[w_idx2 + w_idx1 + 1, c2:(c3 + 1)] = np.linspace(1, 0, c3 - c2 + 1)
        mel_s_w[w_idx2 + w_idx1 + 1, :] = mel_s_w[w_idx2 + w_idx1 + 1, :]/np.sum(mel_s_w[w_idx2 + w_idx1 + 1, :])

    # 応急措置 (フィルタバンクを滑らかにする)
    #w_sum = np.sum(mel_s_w, axis=0)
    #idx = np.argwhere(np.append(np.diff(w_sum) > .01, False))
    #mod_idx = idx[idx > mel_c_idx2[0]]
    #for idx in mod_idx:
    #    r_idx = np.argwhere(mel_s_w[:,mod_idx]>0)
    #    mel_s_w[r_idx, mod_idx] = mel_s_w[r_idx, mod_idx + 1]
    #
    
    f_c1 = mel2hz(f[mel_c_idx1])
    f_c2 = mel2hz(np.arange(mel_lower, mel_upper+1, mel_step))
    f_c = np.hstack((f_c1, f_c2[1:-1]))
    return mel_s_w, f_c

def frameindex(framelength, noverlap, signallength):
    sft = framelength - noverlap
    n = int(np.fix((signallength - framelength)/sft + 1))
    findex = np.array([np.arange(0,framelength)]).T \
             + np.array([np.arange(0,n)])*sft
    return(findex)

def formantFFTCeps(S, fs, order):
    env = np.log(np.abs(np.exp(np.fft.rfft(
        liftering(np.fft.irfft(np.log(np.abs(S))),order)))))

def mfcc(x, fs):
    S = np.fft.rfft(x)
    mel_s_w, f_mel_idx = melbank()
    MS = np.log(mel_s_w@np.abs(S))
    order = 13
    MFCC = scipy.fft.dct(MS)
    MFCC[order+1:] = 0
    MFCC[0] = 0
    return MFCC
