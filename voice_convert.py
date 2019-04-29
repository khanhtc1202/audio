from pydub import AudioSegment
import sys

source_audio = sys.argv[1]
export_audio = sys.argv[2]

def main():
    sound = AudioSegment.from_mp3(source_audio)
    sound.export(export_audio, format="wav")

if __name__ == '__main__':
    main()