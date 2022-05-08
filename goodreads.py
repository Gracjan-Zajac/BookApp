from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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

        more = self.browser.find_element(By.XPATH, "//*[contains(text(), '...more')]")
        more.click()

        description = self.browser.find_element(By.ID, 'description')

        return description.text.replace('(less)', "")
