from io import BytesIO  # Необходимо трактовать байты как файл
import requests
import tarfile  # Обработка файлов в формате tar.bz


def download_spam_dataset():
    BASE_URL = "https://spamassassin.apache.org/old/publiccorpus/"
    FILES = ["20021010_easy_ham.tar.bz2",
             "20021010_hard_ham.tar.bz2",
             "20021010_spam.tar.bz2"]
    OUTPUT_DIR = 'spam_data'

    for filename in FILES:
        content = requests.get(f"{BASE_URL}{filename}").content

        # Обернуть файлы в памяти, чтобы использовать их как "файл"
        fin = BytesIO(content)

        # Извлечь все файлы в указанный выходной каталог
        with tarfile.open(fileobj=fin, mode='r:bz2') as tf:
            tf.extractall(OUTPUT_DIR)
