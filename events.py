# encoding: utf-8

import sublime, sublime_plugin
try:
    from . import util
except ValueError:
    import util


class PerformEventListener(sublime_plugin.EventListener):
    """Suggest subroutine completions for the perform statement."""

    def on_query_completions(self, view, prefix, points):
        if not util.is_natural_file(view):
            return None
        texts = util.text_preceding_points(view, points)
        if all([text.strip().endswith('perform') for text in texts]):
            subroutines = util.find_text_by_selector(view,
                'entity.name.function.natural')
            if not subroutines:
                return None
            subroutines.sort()
            completions = [(sub, sub) for sub in subroutines]
            return (completions, sublime.INHIBIT_WORD_COMPLETIONS)


class AddRulerToColumn72Listener(sublime_plugin.EventListener):
    """Add a ruler to column 72 when a Natural file is opened. If the user has
    other rulers, they're not messed with."""

    def on_load(self, view):
        if not util.is_natural_file(view):
            return
        rulers = view.settings().get('rulers')
        if 72 not in rulers:
            rulers.append(72)
            rulers.sort() # why? to be neat.
            view.settings().set('rulers', rulers)


class FixWordSeparatorsListener(sublime_plugin.EventListener):
    """Fix the `word_separators` setting for a Natural view so that the hyphen
    and hash sign can be considered parts of words."""

    def on_load(self, view):
        if not util.is_natural_file(view):
            return
        separators = view.settings().get('word_separators')
        separators = separators.replace('-', '').replace('#', '')
        view.settings().set('word_separators', separators)
