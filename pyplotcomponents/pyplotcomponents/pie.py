# -*- coding: utf-8 -*-

'''
Basic pie plot.
'''

import matplotlib.pyplot as plt


class Pie(object):
    '''
    Wrapper used to draw a plot containing basic pie chart.
    '''

    def __init__(self, figure, title, axis_size_rectangle=None):
        if title is not None:
            figure.suptitle(title)
        if axis_size_rectangle is None:
            axis_size_rectangle = [0.1, 0.1, 0.85, 0.8]
        self.axis = figure.add_axes(axis_size_rectangle)

    def add_data(self, sizes, labels, *args, **kw):
        '''
        Add pie data.
        '''
        self.axis.pie(sizes, labels=labels, *args, **kw)

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
    Test function.
    '''
    fig = plt.figure(figsize=(6, 6))
    basic_pie = Pie(fig, 'Test', axis_size_rectangle=[0, 0, 1, 1])
    basic_pie.add_data([10, 20, 30], ['One', 'Two', 'Three'], colors=[
                       'Red', 'Green', 'Blue'], autopct='%1.1f%%')
    basic_pie.show_or_save(output_path)


if __name__ == '__main__':
    draw()
