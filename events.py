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
