import matplotlib.pyplot as plt

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie( values, labels= labels)
    ax.axis("equal")
    plt.show()

if __name__ == "__main__":
    lables = ["a","b","c"]
    values = [10,40,100]
    generate_pie_chart(labels, values)