#Written by Alex I. Ramirez @alexram1313
#arcompware.com
import re
import wave
import pyaudio
import _thread
import time

class TextToSpeech:

    CHUNK = 1024

    def __init__(self):
        pass

    # def __init__(self, words_pron_dict:str = 'cmudict-0.7b.txt'):
    #     self._l = {}
    #     self._load_words(words_pron_dict)

    # def _load_words(self, words_pron_dict:str):
    #     with open(words_pron_dict, 'r') as file:
    #         for line in file:
    #             if not line.startswith(';;;'):
    #                 key, val = line.split('  ',2)
    #                 self._l[key] = re.findall(r"[A-Z]+",val)

    def get_pronunciation(self, str_input):
        # list_pron = []
        # for word in re.findall(r"[\w']+",str_input.upper()):
        #     if word in self._l:
        #         list_pron += self._l[word]
        list_pron = list(str_input.lower())
        print(list_pron)
        delay=0
        for pron in list_pron:
            _thread.start_new_thread(self._play_audio, (pron,delay,))
            delay += 0.12

    def _play_audio(self, sound, delay):
        try:
            time.sleep(delay)
            wf = wave.open("usounds-short/"+sound+".wav", 'rb')
            p = pyaudio.PyAudio()
            stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                            channels=wf.getnchannels(),
                            rate=wf.getframerate(),
                            output=True)

            data = wf.readframes(TextToSpeech.CHUNK)

            while data:
                stream.write(data)
                data = wf.readframes(TextToSpeech.CHUNK)

            stream.stop_stream()
            stream.close()

            p.terminate()
            return
        except:
            #time.sleep(delay)
            pass

if __name__ == '__main__':
    tts = TextToSpeech()
    while True:
        astr = input('Enter a word or phrase: ')
        #print(astr)
        tts.get_pronunciation(astr)
