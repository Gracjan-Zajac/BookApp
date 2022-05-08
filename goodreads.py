from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import random

GOODREADS_FRONTPAGE = 'https://www.goodreads.com/'


class GoodReads:

    def __init__(self):
        # Creates headless browser:
        opts = Options()
        opts.headless = True
        assert opts.headless
        self.browser = Firefox(options=opts)
        self.browser.get(GOODREADS_FRONTPAGE)
        self.browser.implicitly_wait(5)

    def get_info(self, book):
        """
         Gets information about book from goodreads.com
        """
        search_field = self.browser.find_element(By.ID, 'sitesearch_field')
        search_field.clear()
        search_field.send_keys(book)
        search_field.send_keys(Keys.RETURN)

        result = self.browser.find_element(By.CLASS_NAME, 'bookTitle')
        result.click()

        if self.browser.find_element(By.XPATH, "//*[contains(text(), '...more')]"):
            more = self.browser.find_element(By.XPATH, "//*[contains(text(), '...more')]")
            more.click()

        description = self.browser.find_element(By.ID, 'description').text
        description = os.linesep.join([s for s in description.splitlines() if s])
        description = description.replace('(less)', "")

        return description

    def get_quote(self):
        """
        Takes a random quote from goodreads.com and returns it.
        """
        quotes = self.browser.find_element(By.ID, 'quotes')
        quotes_elements = quotes.find_elements(By.CLASS_NAME, 'quoteText')
        quotes_list = []

        for quote in quotes_elements:
            quote = quote.get_attribute('innerHTML').lstrip()
            end_quote = quote.find('<')
            raw_quote = quote[:end_quote].strip()
            author_start = quote.find('<span class="authorOrTitle">') + len('<span class="authorOrTitle">')
            author_end = quote.find('</span>')
            author = quote[author_start:author_end].strip()
            quote_and_author = f'{raw_quote}\n- {author}'
            quotes_list.append(quote_and_author)

        print(quotes_list[3])



test = GoodReads()
test.get_quote()