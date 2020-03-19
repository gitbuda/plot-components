# -*- coding: utf-8 -*-

'''
http://en.wikipedia.org/wiki/Radar_chart

Based on http://stackoverflow.com/questions/24659005/radar-chart-with-multiple-scales-on-multiple-axes.
'''

import pylab as pl
import numpy as np


class Radar(object):

    def __init__(self, fig, titles, labels, rect=None):

        if rect is None:
            rect = [0.1, 0.1, 0.8, 0.8]

        self.n = len(titles)
        self.angles = np.arange(90, 90+360, 360.0/self.n) % 360
        self.axes = [fig.add_axes(rect, projection="polar",
                                  label="axes%d" % i)
                     for i in range(self.n)]

        self.ax = self.axes[0]
        self.ax.set_thetagrids(self.angles, labels=titles, fontsize=12)

        for ax in self.axes[1:]:
            ax.patch.set_visible(False)
            ax.grid("off")
            ax.xaxis.set_visible(False)

        for ax, angle, label in zip(self.axes, self.angles, labels):
            ax.set_rgrids(range(1, 6), angle=angle, labels=label)
            ax.spines["polar"].set_visible(False)
            ax.set_ylim(0, 5)

    def plot(self, values, *args, **kw):
        angle = np.deg2rad(np.r_[self.angles, self.angles[0]])
        values = np.r_[values, values[0]]
        self.ax.plot(angle, values, *args, **kw)
        self.ax.fill(angle, values, facecolor=kw['color'], alpha=kw['alpha']/3)


def draw(output_path=None):
    '''
    Plot a radar from the plot object.

    Args:
        output_path: path to output file, if the output_path is
                     None than graph will be shown inside a window
    '''

    # font setup
    pl.rc('font', family="Open Sans")

    titles = list("ABCDE")

    labels = [
        list("abcde"), list("12345"), list("uvwxy"),
        ["one", "two", "three", "four", "five"],
        list("jklmn")
    ]

    fig = pl.figure(figsize=(6, 6))

    titles = ["AAA", "BBB", "CCC", "DDD", "EEE"]

    labels = [
        ['10k', '100k', '1M', '10M', '100M'], list("12345"), list("uvwxy"),
        ["one", "two", "three", "four", "five"],
        list("jklmn")
    ]

    radar = Radar(fig, titles, labels)
    radar.plot([1, 3, 2, 5, 4], "-", lw=3, color="b", alpha=0.6, label="first")
    radar.plot([2, 2, 3, 3, 2], "-", lw=3, color="r", alpha=0.6, label="secon")
    radar.plot([3, 4, 3, 4, 2], "-", lw=3, color="#006633", alpha=0.6,
               label="third")
    radar.plot([3, 2, 3, 4, 2], "-", lw=3, color="y", alpha=0.6, label="fourt")
    radar.plot([3, 5, 3, 4, 2], "-", lw=3, color="m", alpha=0.6, label="fifth")
    lgd = radar.ax.legend(loc='center right', bbox_to_anchor=(1.3, 0.9))

    if output_path is None:
        pl.show()
    else:
        pl.savefig(output_path, format='png', bbox_extra_artists=(lgd,),
                   bbox_inches='tight')


if __name__ == "__main__":
    draw()
