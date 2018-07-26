from pydub import AudioSegment


base_path = "./public/voices"


def read_sound_from_source(path):
    return AudioSegment.from_file(path)


def cut_sound(sound, head, tail):
    return sound[head*1000 : tail: 1000]


def combine_voice(s1, s2, export=True, path=base_path+"/mix/combined.wav"):
    combined = s1.overlay(s2)
    if export:
        combined.export(path, format='wav')
    return combined


def main():
    sound1 = read_sound_from_source(base_path + "/for_visual/chorus_1.wav")
    sound2 = read_sound_from_source(base_path + "/noise/radio-noise.wav")
    noise = cut_sound(sound2, 36, 51)
    combine_voice(sound1, noise)


if __name__ == '__main__':
    main()
