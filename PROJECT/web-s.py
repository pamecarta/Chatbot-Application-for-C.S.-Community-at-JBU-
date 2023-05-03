from urllib.request import urlopen
import re
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://catalog.jbu.edu/preview_program.php?catoid=22&poid=2495&hl=computer+science&returnto=search"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")

coreS = html.find("Core")
Start = coreS + len("Core")
EndIn = html.find("Classes")
CatalogCore = html[Start:EndIn]


cleantext = BeautifulSoup(html, "lxml").text
print(cleantext)