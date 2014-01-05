# -*- coding: utf-8 -*-
"""
Contains a simple crawling API to use pylinkchecker programmatically.

We will do everything to keep functions in this module backward compatible
across versions.
"""
from __future__ import unicode_literals, absolute_import

from pylinkchecker.crawler import configure_logger, execute_from_config
from pylinkchecker.models import Config


def crawl(url):
    """Crawls a URL and returns a pylinkchecker.crawler.Site instance."""
    config = Config()
    config.parse_api_config([url])
    logger = configure_logger(config)
    crawler = execute_from_config(config, logger)

    return crawler.site


def crawl_with_options(urls, options_dict=None, logger=None):
    # TODO
    pass