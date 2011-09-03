import logging
import htmllib
import formatter
import string

log = logging.getLogger(__name__)

class AnchorParser(htmllib.HTMLParser):
    def __init__(self, verbose=0):
        self.url_title = {}
        self.anchors = []
        f = formatter.NullFormatter()
        htmllib.HTMLParser.__init__(self, f, verbose)

    def anchor_bgn(self, href, name, type):
        self.save_bgn()
        self.href = href
        #~ log.debug(href)

    def anchor_end(self):
        text = string.strip(self.save_end())
        if self.href and text:
            log.debug("href: %s, text: %s" % (self.href, text))
            self.anchors.append((self.href, text))
        else:
            log.warn("bad html")
