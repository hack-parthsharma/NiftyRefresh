import os
import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

CHROMEDRIVER_PATH = os.environ["CHROMEDRIVER_PATH"]

OPENSEA_COLLECTION_URL = "YOUR_URL/{token_id}"
OPENSEA_COLLECTION_RANGE = (1, 10_000)

chrome = Chrome(CHROMEDRIVER_PATH)


def refresh_metadata(index):
    chrome.get(OPENSEA_COLLECTION_URL.format(token_id=index))
    chrome.implicitly_wait(1)
    actions = ActionChains(chrome)
    actions.send_keys(Keys.TAB * 17)
    time.sleep(1)
    actions.send_keys(Keys.ENTER)
    time.sleep(3)
    actions.perform()
    print(f"Updated: {index}")


if __name__ == "__main__":
    for i in range(*OPENSEA_COLLECTION_RANGE):
        refresh_metadata(i)
