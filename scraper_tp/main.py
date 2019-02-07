import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

pregex = re.compile(r'^([0-9]+)\.\s(\S.*)$')


def get_chrome():
    chrome_driver_path = 'webdriver/chromedriver'
    return webdriver.Chrome(executable_path=chrome_driver_path)


def get_firefox():
    gecko_driver_path = 'webdriver/geckodriver'
    return webdriver.Firefox(executable_path=gecko_driver_path)


def extract(id, browser):
    url = f'https://www.thripitakaya.org/tipitakaya/Index/{id}'
    browser.get(url)
    content: webelement.WebElement = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'dvSuttaConent')))
    WebDriverWait(content, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "resRw")))
    levels = content.find_elements_by_xpath('./div/div[contains(@class, "resRw")]')
    if len(levels) == 5:
        book = levels[0].text.strip()
        nikaya = levels[1].text.strip()
        wagga = levels[2].text.strip()
    sutta = levels[-1].text.strip()
    with open(f'books/{sutta}.txt', 'w') as file:
        if len(levels) == 5:
            file.write(f"{book}\n")
            file.write(f"{nikaya}\n")
            file.write(f"{wagga}\n")
        file.write(f"{sutta}\n")
        paras = WebDriverWait(content, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, "./div/div/div/div[contains(@class, 'resRw')]")))
        for p in paras:
            ptext = p.text
            match = pregex.match(ptext)
            if match:
                file.write(f"\n#{match.groups()[0]}\n")
                p = match.groups()[1]
            else:
                p = ptext
            lines = p.split('.')
            for l in lines[:-1]:
                file.write(f"{l.strip()}.\n")
            ll = lines[-1].strip()
            if ll:
                file.write(f"{ll}\n")
            file.write("\n")


def start():
    browser = get_chrome()
    for i in range(45, 58):
        extract(i, browser)
    browser.close()


if __name__ == '__main__':
    start()
