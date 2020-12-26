#!/usr/bin/python

# To start tracking a new site:
#  - create a parser class in another file, based off (say) bbc.BBCParser
#  - add it to parsers (below)
# Test with test_parser.py

# List of parsers to import and use based on parser.domains

parsers = """
gooseparser.GooseParser
""".split()

parser_dict = {}

# Import the parsers and fill in parser_dict: domain -> parser
for parsername in parsers:
    module, classname = parsername.rsplit('.', 1)
    parser = getattr(__import__(module, globals(), fromlist=[classname]), classname)
    parser_dict['all'] = parser

def get_parser(url):
    return parser_dict['all']

# Each feeder places URLs into the database to be checked periodically.

parsers = [parser for parser in parser_dict.values()]

__all__ = ['parsers', 'get_parser']
