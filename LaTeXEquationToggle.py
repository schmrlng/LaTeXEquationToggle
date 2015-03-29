import sublime, sublime_plugin

class latexequationtoggleCommand(sublime_plugin.TextCommand):
    def nextline(self, line):
        return self.view.line(line.end()+1)

    def prevline(self, line):
        return self.view.line(line.begin()-1)

    def run(self, edit):
        delims = [('\\[', '\\]'),
                  ('\\begin{equation}', '\\end{equation}'),
                  ('\\begin{equation*}', '\\end{equation*}'),
                  ('\\begin{align}', '\\end{align}'),
                  ('\\begin{align*}', '\\end{align*}'),
                  ('$', '$')]
        if len(self.view.sel()) == 1:
            sel = self.view.sel()[0]
            startline = self.view.line(sel)
            for i in range(10):
                startline = self.prevline(startline)
                idx, delim = next(((idx, d) for (idx, d) in enumerate(delims)
                                   if self.view.substr(startline).lstrip().startswith(d[0])), (None, None))
                if delim:
                    break
            else:
                return
            endline = self.view.line(sel)
            for i in range(10):
                endline = self.nextline(endline)
                if self.view.substr(endline).lstrip().startswith(delim[1]):
                    break
            else:
                return
            newidx = (idx + 1) % len(delims)
            startregion = self.view.find(delim[0], startline.begin(), sublime.LITERAL)
            endregion = self.view.find(delim[1], endline.begin(), sublime.LITERAL)
            self.view.replace(edit, endregion, delims[newidx][1])
            self.view.replace(edit, startregion, delims[newidx][0])
