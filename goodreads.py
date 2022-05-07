from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

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
