from main import Target
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

opts = Options()
opts.add_argument("--headless")

driver = Chrome(ChromeDriverManager().install(), options=opts)
target = Target(driver)
target.add({'cloud':'tojestsprawadlaojcamateusza'})
target.run(25, "187877")

try:
    driver.close()
except:
    pass

"""działa bez zarzutów, jest całkiem szybkie"""
