import scipy.stats as scs
import numpy as np
import matplotlib.pyplot as plt
import sys

def y_axis_func(x, vids_no, mean_v, dev_v):
    scaling = vids_no / scs.norm.pdf(mean_v, loc=mean_v, scale=dev_v)
    return scs.norm.pdf(x, loc=mean_v, scale=dev_v) * scaling

if __name__ == '__main__':
    plt.rc('figure', figsize=(10, 8), dpi=100)
    plt.rc('axes', labelpad=18, facecolor="#ffffff", linewidth=0.4, grid=False, labelsize=24)
    fig, ax = plt.subplots()
    x = np.linspace(0, 3.5e6, 200)

    vids_full = 6351
    views_full = 1.963852e+06
    dev_full = 7.061186e+06

    vids_sci = 6351
    views_sci = 8.507945e+05
    dev_sci = 2.723119e+06

    vids_hotel = 6351
    views_hotel = 1.150065e+06
    dev_hotel = 2.020408e+06

    ax.plot(x, y_axis_func(x, vids_full, views_full, dev_full), color='xkcd:dark teal', lw=2, 
            alpha=0.6, label='All Data Mean Views')
    ax.plot(x, y_axis_func(x, vids_sci, views_sci, dev_sci), color='xkcd:plum', lw=2, 
            alpha=0.6, label='Sci Tech Mean Views')
    ax.plot(x, y_axis_func(x, vids_hotel, views_hotel, dev_hotel), color='xkcd:magenta', lw=2, 
            alpha=0.6, label='Hotel Travel Data Mean Views')
    ax.axvline(views_full, color='xkcd:dark teal', alpha=0.6)
    ax.axvline(views_sci, color='xkcd:plum', alpha=0.6)
    ax.axvline(views_hotel, color='xkcd:magenta', alpha=0.6)
    ax.set(xlabel='Views')
    ax.tick_params(labelsize=16)
    ax.set_ylim(0, 8500.)
    plt.yticks([])
    plt.legend(fontsize='x-large')
    plt.tight_layout(pad=1.)
    # plt.show()
    plt.savefig("images/comp_means_dist.png")