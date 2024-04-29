import matplotlib.pyplot as plt

def histogram_plot( x, title):
    fig = plt.figure()
    ax = fig.add_subplot(len(fig.axes)+1, 1, len(fig.axes)+1)
    ax.hist(x, 40, density=True, facecolor='C0', alpha=0.75)
    ax.set_title(title)

def show_plot():
    plt.tight_layout()
    plt.show()