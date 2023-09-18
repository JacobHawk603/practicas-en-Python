import librosa      #<- importamos librosa unicamente para obtener el ndArray con los elemtnos de la honda para los calculos
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

def mfcc(y, sr):
    '''y es nuestra señal discretizada a la cual le aplicamos la transformada de Fourier en tiempo corto'''

    f, t, zxx = signal.stft(x=y)

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
    

if __name__ == "__main__":
    
    #vamos a asumir que las series de tiempo que devuelve librosa, es la señal en tiempo discreto
    #obteniendo la señal en tiempo discreto para realizar las operaciones

    y, sr = librosa.load("src/audio el quijote reconocimiento de voz.mp3")

    mfcc(y, sr)