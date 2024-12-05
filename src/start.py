import sounddevice as sd
import soundfile as sf
import numpy as np
import threading
import keyboard
from datetime import datetime

class AudioRecorder:
    def __init__(self, sample_rate=44100):
        self.sample_rate = sample_rate
        self.recording = False
        self.audio_chunks = []
        self.channels = 2

    def start_recording(self, output_file="reuniao.wav"):
        """
        Inicia a gravação contínua do áudio
        """
        self.recording = True
        self.output_file = output_file

        # Lista todos os dispositivos
        print("\nDispositivos de áudio disponíveis:")
        print(sd.query_devices())

        try:
            # Configura o dispositivo de entrada padrão
            device_info = sd.query_devices(kind='input')
            print(f"\nUsando dispositivo: {device_info['name']}")

            # Inicia a gravação
            print("\nIniciando gravação... Pressione 'q' para parar.")
            print("Gravando...")

            with sf.SoundFile(
                self.output_file,
                mode='w',
                samplerate=self.sample_rate,
                channels=self.channels,
                subtype='PCM_16'
            ) as file:
                with sd.InputStream(
                    samplerate=self.sample_rate,
                    channels=self.channels,
                    dtype=np.int16
                ) as stream:
                    while self.recording:
                        audio_data, overflowed = stream.read(1024)
                        if not overflowed:
                            file.write(audio_data)

        except Exception as e:
            print(f"Erro durante a gravação: {e}")

    def stop_recording(self):
        """
        Para a gravação
        """
        self.recording = False
        print(f"\nGravação finalizada! Arquivo salvo como {self.output_file}")

def main():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"reuniao_{timestamp}.wav"

    recorder = AudioRecorder()
    recording_thread = threading.Thread(target=recorder.start_recording, args=(output_file,))
    recording_thread.start()

    keyboard.wait('q')
    recorder.stop_recording()
    recording_thread.join()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Erro durante a gravação: {e}")