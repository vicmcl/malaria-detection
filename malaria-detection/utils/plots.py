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


def plot_training(histories, figsize=(10, 5)):
    fig = plt.figure(figsize=figsize)
    keys = ['loss', 'accuracy']
    colors = sns.color_palette("husl", n_colors=len(histories))

    for i, key in enumerate(keys):
        fig.add_subplot(1, len(keys), i + 1)

        for hist, color in zip(histories, colors):
            plt.plot(
                range(1, len(hist.epoch) + 1),
                hist.history[key],
                label=f'Training {hist}',
                color=color,
                linestyle='--'
            )
            plt.plot(
                range(1, len(hist.epoch) + 1),
                hist.history['val_' + key],
                label=f'Validation {hist}',
                color=color
            )

            # Axis parameters
            plt.xlabel('Epoch')
            plt.legend()
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