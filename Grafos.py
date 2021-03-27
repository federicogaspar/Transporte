# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 23:04:48 2018

@author: feder
"""

import pickle
import matplotlib.pyplot as plt
import matplotlib.colors
from matplotlib.collections import LineCollection
import matplotlib.ticker as mticker


dataBase = pickle.load(open("db.p", "rb"))
solapamiento = pickle.load(open("solapamiento.p", "rb"))


def plot_linea(grafo, name=False, overlap=False):

    fig,  ax = plt.subplots(1, 1)
    if name is not False: plt.title(name)

    if overlap is True:
        z = solapamiento[grafo]
        colormap = plt.cm.jet  # plt.cm.hsv
        normalize = matplotlib.colors.Normalize(vmin=1, vmax=30)
        lc = LineCollection(zip(grafo[:-1], grafo[1:]), array=z, cmap=colormap,
                            norm=normalize)
        ax.add_collection(lc)
        ax.margins(0.5, 0.1)
        plt.grid()
        plt.colorbar(lc,ticks=mticker.MultipleLocator(5))
        plt.xlim([-5, 32]), plt.ylim([32, 72])

    else:
        x, y = [k[0] for k in grafo], [k[1] for k in grafo]
        plt.plot(x, y, '-', linewidth=2, color="b")
        plt.grid()




def global_plot(dic = dataBase, name = False, overlap=False):

    if name is not False: plt.title(list(dic.keys()))

    fig,  ax = plt.subplots(1, 1, figsize=(16, 16), dpi=180)

    if overlap is True:
        for linea in dic.keys():
            grafo, z = dic[linea], solapamiento[linea]
            colormap = plt.cm.jet  # plt.cm.hsv
            normalize = matplotlib.colors.Normalize(vmin=1, vmax=22)
            lc = LineCollection(zip(grafo[:-1], grafo[1:]), array=z,
                                cmap=colormap, norm=normalize)
            ax.add_collection(lc)
            ax.margins(0.5, 0.1)
        ax.xaxis.set_major_locator(mticker.MultipleLocator(5))
        ax.yaxis.set_major_locator(mticker.MultipleLocator(5))
        ax.xaxis.set_minor_locator(mticker.AutoMinorLocator(5))
        ax.yaxis.set_minor_locator(mticker.AutoMinorLocator(5))
        ax.grid(which='major', color='#CCCCCC', linestyle='--')
        ax.grid(which='minor', color='#CCCCCC', linestyle=':')
        # plt.grid()
        plt.colorbar(lc, ticks=mticker.MultipleLocator(5), aspect=50)
        plt.xlim([-5, 32]), plt.ylim([32, 72])

    else:
         for linea in dic.keys():
            x, y = [k[0] for k in grafo], [k[1] for k in grafo]
            plt.plot(x, y, '-', linewidth=2, color="b")
            plt.grid()


global_plot(overlap=False)










