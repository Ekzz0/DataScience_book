from scripts import download_spam_dataset
import glob
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report

# # Загрузить датасет с данными о спамных сообщениях
# download_spam_dataset()

# Реализуем простойший спам - фильтр:
# Анализируем тему сообщения - она начинается везде с Subject:
path = 'spam_data/*/*'
titles = []
classes = []

# glob.glob - возвращает каждое имя файла по пути указанному
for filename in glob.glob(path):
    is_spam = 'ham' not in filename

    # Т.к в файлах есть мусорные символы -> используем параметр errors='ignore' для пропуска
    with open(filename, errors='ignore') as email_file:
        for line in email_file:
            if line.startswith("Subject:"):
                subject = line.lstrip("Subject: ")
                titles.append(subject)
                classes.append(is_spam)
                break  # заканчиваем работу с данным файлом

# Подготовим Данные для обучения. Переведем сообщения в текст:
vectorizer = CountVectorizer(analyzer='word')
X = vectorizer.fit_transform(titles)

X_train, X_test, y_train, y_test = train_test_split(X, classes, test_size=0.25, train_size=0.75, random_state=50)
N_Bayes = BernoulliNB()
N_Bayes.fit(X_train, y_train)
predict = N_Bayes.predict(X_test)

print("Number of mislabeled points out of a total %d points : %d \n" % (X_test.shape[0], (y_test != predict).sum()))
print("Classification_Report: \n", classification_report(y_test, predict))
