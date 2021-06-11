import sublime
import sublime_plugin


class GrepCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.show_input_panel("Grep:", "", self.on_done, None, None)

	def on_done(self, text):
		self.window.active_view().run_command("keep_lines", { "containing": text })

class KeepLinesCommand(sublime_plugin.TextCommand):
	def run(self, edit, containing):
		rr = self.view.find_all(containing)
		keep = [self.view.rowcol(self.view.full_line(r).begin())[0] for r in self.view.find_all(containing, sublime.LITERAL)]
		total = list(range(self.view.rowcol(self.view.size())[0] + 1))
		delete = [x for x in total if x not in keep]

		for y in reversed(delete):
			self.view.erase(edit, self.view.full_line(self.view.text_point(y, 0)))