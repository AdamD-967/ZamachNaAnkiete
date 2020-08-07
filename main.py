from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from typing import Dict

class Target:
    def __init__(self, mode: str, pin: str):
        self.options = Options()
        if mode == "headless":
            self.options.add_argument("--headless")
        self.layers = dict() # słownik par {rodzaj_ankiety:odpowiedź}
        self.driver = Chrome(ChromeDriverManager().install(), options=self.options)
        self.pin = pin
        self.ank = r"https://www.mentimeter.com/"

    def add(self, layer: Dict[str, str]) -> None:
        self.layers.update(layer) # dodawanie kolejnych warstw
    
    def cloud(self, ans: str) -> None:
        xinp = r"/html/body/div[1]/div/div[2]/div[1]/form/fieldset/div/div/input"
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xinp)))
            ent1 = self.driver.find_elements_by_xpath(xinp)
            for ent in ent1:
                ent.send_keys(ans)
                ent.submit()
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

    def run(self, iterations: int) -> None:
        try:
            for i in range(iterations):
                self.driver.get(self.ank)
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, r"/html/body/div[1]/div[1]/header/div/div/form/input")))
                ent = self.driver.find_element_by_xpath(r"/html/body/div[1]/div[1]/header/div/div/form/input")
                ent.send_keys(self.pin)
                ent.submit()
                k0 = list(self.layers.keys())[0]
                eval(f"self.{k0}('{self.layers[k0]}')")

                self.driver.delete_all_cookies()
        except:
            pass
        self.layers.pop(k0)


def main() -> None:
    actions = ["set", "run", "add", "break"]
    while True:
        action = input(">>> ")
        try:
            assert action in actions
            if action == "set":
                pin = input("pin: ")
                mode = input("mode: ")
                target = Target(mode, pin)
            elif action == "add":
                layer = input("type: ")
                mess = input("message: ")
                target.add({layer:mess})
            elif action == "run":
                it = int(input("iterations: "))
                target.run(it)
            else:
                break
            print(target.layers)
        except:
            print("error")
        
    try:
        target.driver.close()
    except:
        pass


if __name__ == "__main__":
    main()
