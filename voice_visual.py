import matplotlib.pyplot as plt
import numpy as np
import wave

base_path = "./voices/for_visual/"

def get_signal_from_file(file_name):
    spf = wave.open(file_name, 'r')
    signal = spf.readframes(-1)
    signal = np.fromstring(signal, 'Int16')
    return signal


def visualize_in_same_plot(plot_position, plot_title, items):
    plt.figure(1)
    plt.subplot(plot_position)
    plt.title(plot_title)
    for item in items:
        plt.plot(item)


def visualize_compare_plot(plot_position, plot_title, list_file_data):
    items = []
    for _file in list_file_data:
        items.append(get_signal_from_file(_file))
    visualize_in_same_plot(plot_position=plot_position, plot_title=plot_title, items=items)


def main():
    visualize_compare_plot(plot_position=111,
                           plot_title='showing',
                           list_file_data=[base_path + 'chorus_1.wav', base_path + 'chorus_2.wav'])

    plt.show()


if __name__ == '__main__':
    main()
