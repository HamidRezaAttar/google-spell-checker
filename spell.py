import re
import urllib.request
import urllib.parse

from urllib.request import urlopen
from html.parser import HTMLParser


class Spell:
    def __init__(self):
        user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36"
        self.headers = {
            "User-Agent": user_agent,
        }

    def get_page(self, url):
        req = urllib.request.Request(url, None, self.headers)
        page = urlopen(req)
        html = str(page.read())
        page.close()
        return html

    def correct(self, text):
        html = self.get_page(
            f"http://www.google.com/search?hl=en&q={urllib.parse.quote(text)}&meta=&gws_rd=ssl"
        )
        html_parser = HTMLParser()
        match = re.search(
            r"(?:Showing results for|Did you mean|Including results for)[^\0]*?<a.*?>(.*?)</a>",
            html,
        )
        if match is None:
            fix = text
        else:
            fix = match[1]
            fix = re.sub(r"<.*?>", "", fix)
            fix = html_parser.unescape(fix)
        return fix

    def decode(self, text):
        return (
            bytes(text, encoding="utf-8")
            .decode("unicode-escape")
            .encode("latin1")
            .decode("utf-8")
        )
