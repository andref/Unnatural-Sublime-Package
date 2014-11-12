# encoding: utf-8

import sublime
import re

__version__ = '0.2.0'


def is_natural_file(view):
    """Is this view editing a Natural file?"""
    syntax = view.settings().get(u'syntax')
    return syntax.endswith('Natural.tmLanguage')


def text_preceding_points(view, points):
    """Return the text of the lines containing the specified points up to
    those points."""
    lines = [view.line(point) for point in points]
    lines_to_point = [sublime.Region(line.begin(), point) for line, point in zip(lines, points)]
    return [view.substr(region) for region in lines_to_point]


def find_text_by_selector(view, selector):
    """Find the text that is "covered" by the given selector."""
    regions = view.find_by_selector(selector)
    return [view.substr(region) for region in regions]


__level__ = re.compile(r'^\s*(\d+).*$')

def update_var_levels(view, edit, line, amount=+1):
    """Update the variable levels in the given line. If amount is +1,

    1 #my-var (a10)

    becomes

    2 #my-var (a10)

    Variable levels never go below zero.
    """
    match = __level__.match(view.substr(line))
    if not match:
        return
    start = match.start(1)
    end = match.end(1)
    level_string = match.group(1)
    new_level = int(level_string, base=10) + amount
    if new_level < 1:
        new_level = 1
    new_level_string = str(new_level)
    level_region = sublime.Region(line.begin() + start, line.begin() + end)
    view.replace(edit, level_region, new_level_string)
