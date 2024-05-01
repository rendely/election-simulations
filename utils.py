import matplotlib.pyplot as plt

def histogram_plot( x, title, lean_1, lean_2, result):
    fig = plt.figure()
    ax = fig.add_subplot(len(fig.axes)+1, 1, len(fig.axes)+1)
    ax.hist(x, 40, density=True, facecolor='C0', alpha=0.75)
    ax.axvline(x=lean_1, color='blue')
    ax.axvline(x=lean_2, color='red')
    ax.set_title(result)

def show_plot():
    plt.tight_layout()
    plt.show()