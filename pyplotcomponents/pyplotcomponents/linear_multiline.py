# -*- coding: utf-8 -*-

'''
Multiple lines plot.
'''

import matplotlib.pyplot as plt


class LinearMultiline(object):
    '''
    Wrapper used to draw a plot containing single pyplot axis with multiple
    lines.
    Scale on both x and y axes is linear.
    '''

    def __init__(
            self,
            figure,
            title=None,
            xtitle=None,
            ytitle=None,
            xlimits=None,
            ylimits=None,
            axis_size_rectangle=None,
            grid=False):
        '''
        Plot config.
        '''
        if title is not None:
            figure.suptitle(title)
        if axis_size_rectangle is None:
            axis_size_rectangle = [0.1, 0.1, 0.85, 0.8]
        self.axis = figure.add_axes(axis_size_rectangle)
        if xtitle is not None:
            self.axis.set_xlabel(xtitle)
        if ytitle is not None:
            self.axis.set_ylabel(ytitle)
        if xlimits is not None:
            self.axis.set_xlim(xlimits)
        if ylimits is not None:
            self.axis.set_ylim(ylimits)
        self.axis.grid(grid)

    def plot(self, xvalues, yvalues, *args, **kw):
        '''
        Add line.
        '''
        self.axis.plot(xvalues, yvalues, *args, **kw)

    def add_legend(self):
        '''
        Add legend. Has to be called after all lines were added.
        '''
        self.axis.legend(loc='upper right')

    def show_or_save(self, output_path=None, *args, **kw):
        '''
        Save figure to a file.
        '''
        if output_path is None:
            plt.show()
        else:
            plt.savefig(output_path, *args, **kw)


def draw(output_path=None):
    '''
    Test function.
    '''
    import random
    fig = plt.figure(figsize=(10, 10))
    linear_multiline = LinearMultiline(
        fig, 'Test', 's', 'm/s', [0, 100], [-100, 100], grid=False)
    linear_multiline.plot([i for i in range(100)],
                          [random.randint(80, 90) for _ in range(100)],
                          'o', label='one')
    linear_multiline.plot([i for i in range(100)],
                          [random.randint(0, 50) for _ in range(100)],
                          '-', label='two')
    linear_multiline.plot([i for i in range(0, 100, 5)],
                          [random.randint(-20, -10) for _ in range(0, 100, 5)],
                          '--', label='three')
    linear_multiline.plot([i for i in range(0, 100, 5)],
                          [random.randint(-80, -60) for _ in range(0, 100, 5)],
                          ':', label='four')
    linear_multiline.add_legend()
    linear_multiline.show_or_save(output_path)


if __name__ == '__main__':
    draw('output.png')
