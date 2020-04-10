import json
import xml.etree.ElementTree as ET


def sort_by_length(inputstr):
    return len(inputstr)


def find_words_json():
    with open('newsafr.json') as f:
        json_data = json.load(f)
        all_news = []
        sort_words = []
        words_count = {}

        for item in json_data['rss']['channel']['items']:
            all_news.append(item['description'])

        for news in all_news:
            news = news.split()
            for word in news:
                if len(word) > 6:
                    sort_words.append(word)

        for word in sort_words:
            words_count.setdefault(word, 1)
            words_count[word] += 1

        sort_words = sorted(words_count, key=words_count.get, reverse=True)[0:10]
        print(f'Наиболее часто встречающиеся слова в новостях:      File format - JSON')

        for word in sort_words:
            print(f'Слово "{word}" встречается {words_count[word]} раз.')


def find_words_xml():
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse('newsafr.xml', parser)
    root = tree.getroot()
    channel = root.find('channel')
    items = channel.findall('item')
    all_news = []
    sort_words = []
    words_count = {}

    for item in items:
        all_news.append(item.find('description').text)

    for news in all_news:
        news = news.split()
        for word in news:
            if len(word) > 6:
                sort_words.append(word)

    for word in sort_words:
        words_count.setdefault(word, 1)
        words_count[word] += 1

    sort_words = sorted(words_count, key=words_count.get, reverse=True)[0:10]
    print(f'Наиболее часто встречающиеся слова в новостях:      File format - XML')

    for word in sort_words:
        print(f'Слово "{word}" встречается {words_count[word]} раз.')


find_words_xml()

find_words_json()
