from main import Target
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

text = """Moim zdaniem to nie ma tak, że dobrze albo że nie dobrze.
 Gdybym miał powiedzieć, co cenię w życiu najbardziej, powiedziałbym, że ludzi. 
 Ekhm… Ludzi, którzy podali mi pomocną dłoń, kiedy sobie nie radziłem, kiedy byłem sam. 
 I co ciekawe, to właśnie przypadkowe spotkania wpływają na nasze życie. 
 Chodzi o to, że kiedy wyznaje się pewne wartości, nawet pozornie uniwersalne, bywa, że nie znajduje się zrozumienia, 
 które by tak rzec, które pomaga się nam rozwijać. Ja miałem szczęście, by tak rzec, ponieważ je znalazłem. I dziękuję życiu. 
 Dziękuję mu, życie to śpiew, życie to taniec, życie to miłość. Wielu ludzi pyta mnie o to samo, ale jak ty to robisz?, 
 skąd czerpiesz tę radość? A ja odpowiadam, że to proste, to umiłowanie życia, to właśnie ono sprawia, że dzisiaj na przykład 
 buduję maszyny, a jutro… kto wie, dlaczego by nie, oddam się pracy społecznej i będę ot, choćby sadzić… znaczy… marchew."""

driver = Chrome(ChromeDriverManager().install())
target = Target(driver)
target.add({'opend':"".join(text.split('\n'))})
target.run(2, "211872")

try:
    driver.close()
except:
    pass

""" 
działa, jest git, 
tylko nie można podawać bezpośrednio multiline-inputów, 
tylko trzeba tak jak tu sprowadzić do jednej linii 
"""