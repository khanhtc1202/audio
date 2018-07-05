import matplotlib.pyplot as plt
import numpy as np
import wave


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
                           list_file_data=['chorus_1.wav', 'chorus_2.wav'])

    # 00:00:59 -> 00:01:14 | 00:02:44 -> 00:02:59

    # visualize_compare_plot(plot_position=111,
    #                        plot_title='Original clean',
    #                        list_file_data=['new_record.wav', 'record.wav'])

    # visualize_compare_plot(plot_position=222,
    #                        plot_title='original record',
    #                        list_file_data=['new_record.wav'])
    #
    # visualize_compare_plot(plot_position=224,
    #                        plot_title='record 29',
    #                        list_file_data=['record_29.wav'])

    # visualize_compare_plot(plot_position=222,
    #                        plot_title='SOX clean 0db',
    #                        list_file_data=['dataset/noise/sp10_car_sn0.wav', 'dataset/clean/sp10_sn0_clean.wav'])

    # visualize_compare_plot(plot_position=223,
    #                        plot_title='SOX clean 10db',
    #                        list_file_data=['dataset/noise/sp10_car_sn10.wav', 'dataset/clean/sp10_sn10_clean.wav'])
    #
    # visualize_compare_plot(plot_position=224,
    #                        plot_title='SOX clean 15db',
    #                        list_file_data=['dataset/noise/sp10_car_sn15.wav', 'dataset/clean/sp10_sn15_clean.wav'])

    plt.show()


if __name__ == '__main__':
    main()
