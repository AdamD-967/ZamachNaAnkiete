from main import Target
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

text = "Makbet opowiada o człowieku, który popełnił błąd, który zniszczył mu życie"


opts = Options()
opts.add_argument("--headless")

driver = Chrome(ChromeDriverManager().install(), options=opts)
target = Target(driver)
target.add({'opend':text})
target.run(2, "296109")

try:
    driver.close()
except:
    pass

""" 
działa, jest git, 
tylko nie można podawać bezpośrednio multiline-inputów, 
tylko trzeba tak jak tu sprowadzić do jednej linii 
"""