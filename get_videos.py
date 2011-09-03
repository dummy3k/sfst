import logging
import logging.config
import re, urllib
from pprint import pprint
from anchor_parser import AnchorParser

if __name__ == '__main__':
    logging.config.fileConfig("logging.conf")

log = logging.getLogger(__name__)

for page_no in range(1, 999):
    url = 'http://day9.tv/archives/page/%s/' % page_no
    print "# " + url

    log.debug("download: %s" % url)
    html = urllib.urlopen(url).read()
    #~ with open('index.html') as f:
        #~ html = f.read()

    #~ log.debug("len(html): %s" % len(html))

    if not 'Older Episodes' in html:
        log.info("no more pages")
        break

    url_title = {}
    for url, title in re.findall('href="(http://blip.tv[^ "]+).*>(.*)</a>', html):
        if not url in url_title:
            url_title[url] = [title]
        else:
            url_title[url].append(title)

    p = AnchorParser()
    p.feed(html)
    p.close()

    links = p.anchors
    links = filter(lambda x: x[0].find('http://blip.tv/') >= 0, links)
    links = filter(lambda x: not x[0].endswith('#disqus_thread'), links)
    #~ pprint(links)
    for item in links:
        print(item)
