import sys

sys.path.append(".")
from pelicanconf import *  # noqa: F401,F403

SITEURL = "https://fortyclock.github.io/ord-web-page"
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
DELETE_OUTPUT_DIRECTORY = True
