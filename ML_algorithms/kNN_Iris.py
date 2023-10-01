import pandas
from ucimlrepo import fetch_ucirepo
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import precision_score, accuracy_score


def plot_scattering_diagram(X: pandas.DataFrame, n_rows: int, n_cols: int, metrics: list[str], marks: list[str],
                            classes: list[str]):
    fig, ax = plt.subplots(n_rows, n_cols, figsize=(10, 6))
    fig.subplots_adjust(hspace=0.5, wspace=0.5)
    pairs = [(i, j) for i in range(len(metrics) - 1) for j in range(len(metrics) - 1) if i < j]

    for row in range(n_rows):
        for col in range(n_cols):
            i, j = pairs[3 * row + col]
            # print(i, j)
            ax[row][col].set_title(f"{metrics[i]} vs {metrics[j]}", fontsize=8)
            ax[row][col].set_xlabel(f"{metrics[i]}", fontsize=8)
            ax[row][col].set_ylabel(f"{metrics[j]}", fontsize=8)
            ax[row][col].set_xticks = ([])
            ax[row][col].set_yticks = ([])

            # Отрисуем каждую метку отдельно:
            for mark, cluster_class in [i for i in zip(marks, classes)]:
                ax[row][col].scatter(X[X['class'] == cluster_class][metrics[i]],
                                     X[X['class'] == cluster_class][metrics[j]],
                                     marker=mark)
    plt.show()


if __name__ == "__main__":
    # fetch dataset
    iris = fetch_ucirepo(id=53)

    # data (as pandas dataframes)
    X = iris.data.features
    Y = iris.data.targets

    # variable information
    # print(iris.variables)
    X_for_diag = X.copy()
    X_for_diag['class'] = Y
    classes = list(set(X_for_diag['class']))
    num_of_class = len(classes)

    # Отрисуем Диаграмму рассеяния для цветков ириса
    metrics = X_for_diag.columns.tolist()
    marks = ['+', '.', 'x']
    plot_scattering_diagram(X_for_diag, 2, 3, metrics, marks,
                            classes)  # Видим, что классы действительно могут разделиться на три кластера.

    # Приступим к созданию и обучению модели:
    # Разделим данные на тестовую выборку и тренировочную
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, train_size=0.7, random_state=51)

    kNN = KNeighborsClassifier(n_neighbors=5)
    kNN.fit(X_train, y_train.values.ravel())
    predict = kNN.predict(X_test)
    precision = precision_score(predict, y_test.values.ravel(), average=None)
    accuracy = accuracy_score(predict, y_test.values.ravel())
    print("precision:", precision)
    print("accuracy:", accuracy)
