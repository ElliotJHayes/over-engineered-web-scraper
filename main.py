import urllib.request
from bs4 import BeautifulSoup
import time

toVisit = {"http://python.org/"}
links = {}
visited = {""}

while len(toVisit) > 0:
    url = toVisit.pop()
    print(url)
    response = None
    try:
        response = urllib.request.urlopen(url)
    except:
        visited.add(url)
        continue

    soup = BeautifulSoup(response, "html.parser")
    if soup is not None:
        ext_links = []
        for link in soup("a"):
            if link is not None and link.get("href") is not None and "http" in link.get("href") and link not in visited:
                ext_links.append(link.get("href"))
        toVisit.update(ext_links)
    visited.add(url)

print("done")
print(visited)
