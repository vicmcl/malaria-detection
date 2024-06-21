import matplotlib.pyplot as plt
import random

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

    fig.tight_layout()
    plt.show()