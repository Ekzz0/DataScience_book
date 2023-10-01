import requests


if __name__ == "__main__":
    data = requests.get("https://archive.ics.uci.edu/ml/datasets/iris/iris.zip")
    print(data)
    with open('iris.data', 'w') as file:
        file.write(data.text)
        print(file)