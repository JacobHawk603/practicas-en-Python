import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":

    #comenzamos por cargar el audio
    # audio_file = librosa.example("src/audio el quijote reconocimiento de voz.mp3")

    y, sr = librosa.load("src/audio el quijote reconocimiento de voz.mp3")

    #calculamos el espectograma
    spectogram = librosa.amplitude_to_db(librosa.stft(y), ref=np.max)

    #Calculamos los coeficientes cepstrales en escala de Mel
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    print(type(mfcc))
    print(mfcc)

    #calculamos la envolvente espectral(spectral_centroids)
    envolvente = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
    print("\n\nenvolvente espectral:\n\n")
    print(type(envolvente))
    print(envolvente)

    #calculando la constante espectral      <- Revisar esto, ya que no parece ser lo que buscamos
    fmin = librosa.midi_to_hz(36)
    c = librosa.cqt(y=y, sr=sr, fmin=fmin, n_bins=72)
    logC = librosa.amplitude_to_db(abs(c))

    #Visualizar el espectograma
    plt.subplot(2,2,1)
    librosa.display.specshow(spectogram, sr=sr, x_axis='time', y_axis='log')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Espectograma')

    #visualizar el diagrama de ondas del audio
    plt.subplot(2,2,2)
    librosa.display.waveshow(y=y, sr=sr)

    #visualizar la envolvente espectral
    plt.subplot(2,2,3)
    frames = range(len(envolvente))
    frames_to_time = librosa.frames_to_time(frames, sr=sr, hop_length=552)
    print("\n\nframes to time\n\n")
    print(frames_to_time)
    plt.semilogy(frames_to_time, envolvente, label="envolvente espectral")
    plt.ylabel("hz")
    plt.xticks()
    plt.xlim([frames_to_time.min(), frames_to_time.max()])
    plt.legend()
    plt.title("envolvente")

    #visualizar la constante espectral
    plt.subplot(2,2,4)
    librosa.display.specshow(logC, sr=sr, x_axis="time", y_axis="cqt_note", fmin=fmin)
    plt.colorbar(format='%+2.0f dB')
    plt.title('constante espectral')
    plt.show()