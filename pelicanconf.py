AUTHOR = "Автор блога"
SITENAME = "Мой блог"
SITEURL = ""

PATH = "content"
TIMEZONE = "Europe/Moscow"
DEFAULT_LANG = "ru"

ARTICLE_PATHS = ["articles"]
ARTICLE_SAVE_AS = "{slug}/index.html"
ARTICLE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"
PAGE_URL = "{slug}/"

THEME = "themes/blog"
STATIC_PATHS = ["images"]

DEFAULT_DATE_FORMAT = "%d.%m.%Y"
SUMMARY_MAX_LENGTH = 40
RELATIVE_URLS = True

# Static Comments is auto-loaded by Pelican 4.5+ when installed from pip.
# This flag activates the plugin.
PELICAN_COMMENT_SYSTEM = True
PELICAN_COMMENT_SYSTEM_DIR = "comments"
PELICAN_COMMENT_SYSTEM_IDENTICON_SIZE = 48
PELICAN_COMMENT_SYSTEM_AUTHORS = (AUTHOR,)
PELICAN_COMMENT_SYSTEM_FEED = "feeds/comments-%s.atom.xml"

# Email where comment submissions arrive. The form builds a mailto link,
# so there is no backend, database, paid service, or external script.
PELICAN_COMMENT_SYSTEM_EMAIL_USER = "your.email"
PELICAN_COMMENT_SYSTEM_EMAIL_DOMAIN = "gmail.com"

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
    },
    "output_format": "html5",
}
