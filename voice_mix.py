from pydub import AudioSegment

base_path = "./public/voices"


def read_sound_from_source(path):
    return AudioSegment.from_file(path)


def cut_sound(sound, head, tail):
    return sound[head*1000 : tail*1000]


def combine_voice(s1, s2, export=True, path=base_path+"/mix/combined.mp3"):
    combined = s1.overlay(s2)
    if export:
        combined.export(path, format='mp3')
    return combined


def make_noise(sound, save_to=base_path+"/mix/combined.mp3"):
    noise = read_sound_from_source(base_path + "/noise/radio-noise.wav")
    for i in xrange(1, len(sound)/len(noise)):
        noise.append(noise)
    combine_voice(sound, noise, path=save_to)


def main():
    sound1 = read_sound_from_source(base_path + "/mix/whams.mp3")
    make_noise(sound=sound1)


if __name__ == '__main__':
    main()
