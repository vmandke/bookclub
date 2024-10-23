from matplotlib import pyplot as plt



def plot_the_iterations(iterations_graph, xlim, ylim, c, file_name):
    # Plot and save the graph
    plt.imshow(iterations_graph, cmap="gray", extent=(xlim[0], xlim[1], ylim[0], ylim[1]))
    plt.colorbar()
    plt.title(f"Julia Set for c = {c}")
    plt.savefig(file_name, dpi=300)
    plt.show()
