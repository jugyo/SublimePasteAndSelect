import sublime, sublime_plugin

class PasteAndSelectCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        text = sublime.get_clipboard()
        for s in self.view.sel():
            self.view.replace(edit, s, text)