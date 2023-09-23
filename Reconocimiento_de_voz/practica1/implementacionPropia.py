import librosa      #<- importamos librosa unicamente para obtener el ndArray con los elemtnos de la honda para los calculos
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import speechpy

def mfcc(y, sr):
    '''y es nuestra señal discretizada a la cual le aplicamos la transformada de Fourier en tiempo corto'''

    f, t, zxx = signal.stft(x=y, nperseg=2048)

    #ahora que tenemos la transformada en tiempo corto, hay que elevarla al cuadrado
    zxx_2 = zxx**2

    #sacamos el logaritmo de lo calculado anteriormente

    log_zxx_2 = np.log10(zxx_2)

    #volvemos a sacar la stft
    f2, t2, zxx2 = signal.stft(x=log_zxx_2, fs=sr)

    #finalmente elevamos al cuadrado
    cepstrum = zxx2**2

    print("\n\n stft:\n\n", zxx)

    print("\n\ncepstrum\n\n", cepstrum)

    #imprimamos el espectograma que se obtiene por calcular zxx
    spectogram = librosa.amplitude_to_db(zxx, ref=np.max)
    plt.subplot(1,2,1)
    librosa.display.specshow(spectogram, sr=sr, x_axis='time', y_axis='log')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Espectograma')

    spectogram = librosa.amplitude_to_db(librosa.stft(y), ref=np.max)
    plt.subplot(1,2,2)
    librosa.display.specshow(spectogram, sr=sr, x_axis='time', y_axis='log')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Espectograma')
    plt.show()

    plt.show()

    #dejaremos los espctogramas computados por librosa, ya que es probable que otra librería no tenga esa información

def graficarEspectograma(zxx, sr):
    '''zxx: np.ndarray  -> Es la stft de un audio\n\n
        sr: sampling rate obtenido de librosa.load
    '''
    spectogram = librosa.amplitude_to_db(zxx, ref=np.max)
    # plt.subplot(1,2,1)
    librosa.display.specshow(spectogram, sr=sr, x_axis='time', y_axis='log')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Espectograma')

if __name__ == "__main__":
    
    #vamos a asumir que las series de tiempo que devuelve librosa, es la señal en tiempo discreto
    #obteniendo la señal en tiempo discreto para realizar las operaciones

    y, sr = librosa.load("src/audio el quijote reconocimiento de voz.mp3")

    #para obtener la stft
    f, t, zxx = signal.stft(x=y, nperseg=2048)  #<- Esta parte con estos parametros permite obtener la misma stft que librosa
    
    plt.subplot(1,2,1)
    graficarEspectograma(zxx=zxx, sr=sr)

    #comparar con librosa
    # plt.subplot(1,2,2)
    # graficarEspectograma(librosa.stft(y), sr=sr)
    # plt.show()
    #obtener los mfcc
    f1, t1, espectograma = signal.spectrogram(x=y, fs=sr, nfft=2048)
    print("\n\nespectograma sin convercion a DB\n\n", espectograma)

    mel_coeficients = speechpy.feature.mfcc(signal=y, sampling_frequency=sr)
    print("\n\nMFCC's\n\n", mel_coeficients)

    librosa_mfcc = librosa.feature.mfcc(y=y, sr=sr)

    plt.subplot(1,2,2)
    plt.pcolormesh(t1, f1[0:20], espectograma[0:20], shading='gouraud')
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.show()

    #visualizar los coeficientes de mel
    plt.subplot(1,2,1)
    librosa.display.specshow(librosa_mfcc)
    plt.colorbar(format='%+2.0f dB')
    plt.title("MFCC's librosa")

    plt.subplot(1,2,2)
    librosa.display.specshow(mel_coeficients)
    plt.colorbar(format='%+2.0f dB')
    plt.title("MFCC's speechpy")

    plt.show()
    
    # mfcc(y, sr)