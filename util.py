# encoding: utf-8

import sublime


VERSION = '0.1.0'


def is_natural_file(view):
    """Is this view editing a Natural file?"""
    syntax = view.settings().get('syntax')
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
