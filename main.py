from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from typing import Dict

class Target():
    def __init__(self, driver):
        self.layers = dict() # słownik par {rodzaj_ankiety:odpowiedź}
        self.driver = driver # używany driver
        self.ank = r"https://www.mentimeter.com/"

    def add(self, layer: Dict[str, str]) -> None:
        self.layers.update(layer) # dodawanie kolejnych warstw
    
    def cloud(self, ans: str) -> None:
        xinp = r"/html/body/div[1]/div/div[2]/div[1]/form/fieldset/div/div/input"
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xinp)))
            ent1 = self.driver.find_element_by_xpath(xinp)
            ent1.send_keys(ans)
            ent1.submit()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, r"/html/body/div[1]/div/div[2]/div[1]/div[2]/h1")))
        except:
            self.driver.close()

    def opend(self, ans: str) -> None:
        xinp = r"/html/body/div[1]/div/div[2]/div[1]/form/fieldset/div/textarea"
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xinp)))
            ent = self.driver.find_element_by_xpath(xinp)
            ent.send_keys(ans)
            ent.submit()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, r"/html/body/div[1]/div/div[2]/div[1]/div[2]/h1")))
        except:
            self.driver.close()

    def run(self, iterations: int, pin: str) -> None:
        keys = list(self.layers.keys())
        items = list(self.layers.values())

        try:
            for i in range(iterations):
                self.driver.get(self.ank)
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, r"/html/body/div[1]/div[1]/header/div/div/form/input")))
                ent = self.driver.find_element_by_xpath(r"/html/body/div[1]/div[1]/header/div/div/form/input")
                ent.send_keys(pin)
                ent.submit()
                for l in range(len(keys)):
                    eval(f"self.{keys[l]}('{items[l]}')")

                self.driver.delete_all_cookies()
        except:
            pass
        try:
            self.driver.close()
        except:
            pass
        

def main():
    pass # chwilowy brak ustaleń

if __name__ == "__main__":
    main()
