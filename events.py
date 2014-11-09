# encoding: utf-8

import Natural.util as util
import sublime, sublime_plugin


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
            completions = [[sub, sub] for sub in subroutines]
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
            rulers.sort()
            view.settings().set('rulers', rulers)
