from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
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

    def get_quote(self):
        """
        Returns a random quote from goodreads.com.
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

        random_quote = random.choice(quotes_list)

        return random_quote
