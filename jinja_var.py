import sublime_plugin


class JinjaVarCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    for region in self.view.sel():
      self.view.replace(edit, region, "{{ %s }}" % self.view.substr(region))


"""
API Reference:
http://www.sublimetext.com/docs/2/api_reference.html

Examples:
https://github.com/ehamiter/Sublime-Text-2-Plugins
"""
