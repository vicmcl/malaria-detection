import matplotlib.pyplot as plt
import random
import seaborn as sns


def plot_images(images, labels, n):
    # Set the figure size
    fig = plt.figure(figsize = (n * 2, 2))

    # Generate a list of random indexes
    random_index = [random.randint(0, len(images) + 1) for _ in range(n)]

    # From the random indexes, plot a row of n images with their associated label
    for i in range(n):
        label = "Uninfected" if labels[random_index[i]] == 0 else "Parasitized"
        ax = fig.add_subplot(int("1" + str(n) + str(i)) + 1)
        plt.imshow(images[random_index[i]])
        ax.set_xlabel(label)

    plt.tight_layout()
    plt.grid(False)
    plt.show()


def plot_training(hist):
    fig = plt.figure(figsize=(10, 5))

    for i, key in enumerate(hist.history.keys()):
        fig.add_subplot(1, 2, i + 1)
        plt.plot(range(1, len(hist.epoch) + 1), hist.history[key])
        plt.ylabel(key)
        plt.xlabel('Epoch')

        # Axis parameters
        plt.ylim(0, 1)
        plt.ylabel('Loss')
        plt.xlabel('Epoch')
        plt.legend(['Training', 'Validation'])
        plt.tight_layout()
        plt.show()


def settings():
    plt.rcdefaults()
    sns.set_style('whitegrid')

    # Set custom figure parameters
    plt.rcParams.update({
        'axes.labelcolor':      '#4C4C4C',   # label parameters
        'axes.labelpad':        20, 

        'axes.spines.top':      False,       # border parameters
        'axes.spines.right':    False,     
        'axes.spines.bottom':   False,    
        'axes.spines.left':     False,    

        'axes.titlecolor':      '#4C4C4C',   # title parameters
        'axes.titlepad':        20,            
        'axes.titlesize':       20,           

        "figure.dpi":           200,         # figure parameter

        'grid.linewidth':       0.5,         # grid parameter

        'xtick.color':          "#89939C",   # ticks parameters
        'xtick.labelcolor':     "#89939C",  
        'xtick.major.width':    1,
        'ytick.color':          "#89939C",
        'ytick.labelcolor':     "#89939C",
        'ytick.major.width':    1,
    })