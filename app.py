import requests
from matplotlib import pyplot as plt


def get_cat_fact():
    res = requests.get("https://catfact.ninja/fact")
    if res.ok:
        return res.json()["fact"]
    else:
        raise Exception(f"{res.status_code}: {res.reason}")


def plot_cat(color):
    with plt.xkcd():
        plt.plot([0, 1], [0, 0], color)
        plt.plot([0, 1], [1, 1], color)
        plt.plot([0, 0], [0, 1], color)
        plt.plot([1, 1], [0, 1], color)

        for ear in [0.2, 0.8]:
            plt.plot([ear - 0.1, ear, ear + 0.1], [1, 1.2, 1], color)
        for whisker in [[0.3, 0.45], [0.5, 0.5], [0.7, 0.55]]:
            plt.plot([0.2, 0.4], whisker, color)
        for whisker in [[0.45, 0.3], [0.5, 0.5], [0.55, 0.7]]:
            plt.plot([0.6, 0.8], whisker, color)

        plt.axis('off')
        plt.show()


if __name__ == "__main__":
    print(get_cat_fact())
    plot_cat('k')
