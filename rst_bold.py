"""
Description::
  Shortcut to mark some selected text as bold text in reStructedText.

Example::
  selected_text -> **selected_text**

Key Mapping::
  { "keys": ["super+alt+b"], "command": "rst_bold"}

"""

import sublime_plugin


class RstBoldCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    print "here"
    for region in self.view.sel():
      self.view.replace(edit, region, "**%s**" % self.view.substr(region))


"""
API Reference:
http://www.sublimetext.com/docs/2/api_reference.html

Examples:
https://github.com/ehamiter/Sublime-Text-2-Plugins
"""
