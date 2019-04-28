from pydub import AudioSegment
import sys

source_audio = sys.argv[1]
export_audio = sys.argv[2]

print source_audio
print export_audio

sound = AudioSegment.from_mp3(source_audio)
sound.export(export_audio, format="wav")
