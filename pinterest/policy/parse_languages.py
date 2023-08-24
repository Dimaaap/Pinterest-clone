import requests
from bs4 import BeautifulSoup


class LanguageParser:
    """
    Клас, який збирає дані із сайту за URL-адресою PARSE_URL,
    парсить їх і оформлює список із 50 найпопулярніших мов світу,
    відсортованих у алфавітному порядку
    """
    PARSE_URL = "http://www2.harpercollege.edu/mhealy/g101ilec/intro/clt/cltclt/top100.html"
    MAX_COUNT_LANGUAGES_IN_LIST = 50
    __languages_list = []

    def __init__(self):
        """
        При ініціалізації класу одразу відправити GET-запит на задану URL-адресу
        """
        self.request = requests.get(self.PARSE_URL)

    def get_html(self):
        """
        Якщо сайт повертає статус-код 200, прокидаємо дані у вигляді HTML-документу далі,
        інакше - викидаємо помилку
        :return:
        """
        if self.request.status_code != 200:
            raise ValueError("Parsing Error")
        return self.request.content

    def parse_html(self):
        """
        Отримуємо HTML-документ, парсимо його і складаємо не очищені назви мов у список
        :return:
        """
        html_content = self.get_html()
        soup = BeautifulSoup(html_content, "lxml")
        lang_table = soup.find("table")
        all_tr = lang_table.find_all("tr")
        for row in all_tr:
            language = row.find("a")
            if language:
                self.__languages_list.append(language.text)
        return self.__languages_list

    def clean_list_data(self):
        """
        Очищаємо список із мовами, прибираємо друге слово у назві мови, яке йде після коми
        На приклад: CHINESE, MANDARIN => CHINESE
        Далі прибираємо дублікати
        І обмежуємо фінальний набір лише 50-ма мовами, відсортованими в алфавітному порядку
        Повертає список мов у форматі, який потрібен для створення випадаючого списку
        у input форми для вибору мови сайту.
        [("chinese", "CHINESE"), ...]
        """
        languages_list = self.parse_html()
        languages_list = list(set([i.split(",")[0] for i in languages_list[:self.MAX_COUNT_LANGUAGES_IN_LIST]]))
        input_dropdown_list = [(i.lower(), i.capitalize()) for i in languages_list]
        return sorted(input_dropdown_list)


def get_country_list():
    a = LanguageParser()
    return a.clean_list_data()