from main import Target
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager

driver = Chrome(ChromeDriverManager().install())
target = Target(driver)
target.add({'cloud':'ananasowa inkwizycja'})
target.run(6, "771413")

try:
    driver.close()
except:
    pass

"""działa bez zarzutów, jest całkiem szybkie"""
