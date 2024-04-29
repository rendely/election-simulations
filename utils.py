import matplotlib.pyplot as plt

def start_plot():
    return plt.figure()

def histogram_plot(fig, x, title):
    ax = fig.add_subplot(len(fig.axes)+1, 1, len(fig.axes)+1)
    ax.hist(x, 40, density=True, facecolor='C0', alpha=0.75)
    ax.set_title(title)

def show_plot():
    plt.show()