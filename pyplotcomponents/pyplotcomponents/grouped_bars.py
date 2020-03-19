# -*- coding: utf-8 -*-

'''
Grouped bars plot.
'''

import matplotlib.pyplot as plt
import numpy as np


class GroupedBars(object):

    def __init__(
            self,
            figure,
            group_size,
            title=None,
            xtitle=None,
            ytitle=None,
            labels=[],
            axis_size_rectangle=None,
            grid=False):
        self.group_size = group_size
        self.load = 0
        self.width = 0.95 / group_size
        self.x = np.arange(len(labels)) + 1
        if title is not None:
            figure.suptitle(title)
        if axis_size_rectangle is None:
            axis_size_rectangle = [0.1, 0.1, 0.85, 0.8]
        self.axis = figure.add_axes(axis_size_rectangle)
        if xtitle is not None:
            self.axis.set_xlabel(xtitle)
        if ytitle is not None:
            self.axis.set_ylabel(ytitle)
        self.axis.set_xticks(self.x)
        self.axis.grid(grid)
        self.axis.set_xticklabels(labels)

    def add_data(self, values, annotate=True, *args, **kw):
        if self.load == self.group_size:
            print('WARNING: GroupedBars chart is full!')
            return

        rects = self.axis.bar(self.x - 0.95 / 2 + self.load * self.width,
                              values, self.width, align='edge', *args, **kw)
        self.load += 1

        if not annotate:
            return
        for rect in rects:
            height = rect.get_height()
            self.axis.annotate(
                '{}'.format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')

    def add_legend(self):
        '''
        Add legend. Has to be called after all lines were added.
        '''
        self.axis.legend(loc='upper right')

    def show_or_save(self, output_path=None, *args, **kw):
        '''
        Show or save figure to a file.
        '''
        if output_path is None:
            plt.show()
        else:
            plt.savefig(output_path, *args, **kw)


def draw(output_path=None):
    '''
    Args:
        output_path: path to output file, if the output_path is
                     None than graph will be shown inside a window
    '''
    plt.rc('font', family="Open Sans")
    fig = plt.figure(figsize=(6, 6))
    labels = ['G1', 'G2', 'G3', 'G4', 'G5']
    grouped_bars = GroupedBars(
        fig, 5,
        'Title',
        'x title',
        'y title',
        labels=labels)
    grouped_bars.add_data([20, 34, 30, 35, 27], annotate=False, label='1')
    grouped_bars.add_data([25, 32, 34, 20, 25], label='2')
    grouped_bars.add_data([30, 50, 10, 15, 25], label='3')
    grouped_bars.add_data([15, 13, 50, 2, 34], label='4')
    grouped_bars.add_data([15, 13, 50, 2, 34], label='5')
    grouped_bars.add_data([15, 13, 50, 2, 34], label='6')
    grouped_bars.add_legend()
    grouped_bars.show_or_save(output_path)


if __name__ == "__main__":
    draw()
