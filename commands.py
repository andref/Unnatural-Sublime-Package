# encoding: utf-8

import sublime, sublime_plugin
import re
try:
    from . import util
except ValueError:
    import util


class IndentVariableCommand(sublime_plugin.TextCommand):
    """Indent the region and increase any variable levels."""

    def run(self, edit):
        self.view.run_command('indent')
        for region in self.view.sel():
            for line in self.view.lines(region):
                util.update_var_levels(self.view, edit, line, amount=+1)

    def description(self):
        return 'Indent Variable'


class UnindentVariableCommand(sublime_plugin.TextCommand):
    """Unindent the region and decrease any variable levels."""

    def run(self, edit):
        self.view.run_command('unindent')
        for region in self.view.sel():
            for line in self.view.lines(region):
                util.update_var_levels(self.view, edit, line, amount=-1)

    def description(self):
        return 'Unindent Variable'


class CommentEmptyLines(sublime_plugin.TextCommand):
    """Fill all empty lines with an asterisk, so that the file won't get
    squashed when opened in the SPOD editor."""

    def run(self, edit):
        last_point = 0
        while True:
            empty_line = self.view.find('^\s*\R', last_point)
            if not empty_line:
                break
            self.view.replace(edit, empty_line, '*\n')
            last_point = empty_line.end()

    def is_enabled(self):
        return util.is_natural_file(self.view)

    def is_visible(self):
        return util.is_natural_file(self.view)

    def description(self):
        return "Comment Empty Lines"


class UncommentEmptyLines(sublime_plugin.TextCommand):
    """Uncomment all empty lines to make it resemble a sane source file."""

    def run(self, edit):
        while True:
            empty_line = self.view.find('^\*\s*\R', 0)
            if not empty_line:
                break
            self.view.replace(edit, empty_line, '\n')

    def is_enabled(self):
        return util.is_natural_file(self.view)

    def is_visible(self):
        return util.is_natural_file(self.view)

    def description(self):
        return "Uncomment Empty Lines"
