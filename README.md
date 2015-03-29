# LaTeX Equation Environment Cycling for Sublime Text

Ever write a paper without a plan for what you're typing? Or even a plan for what you're writing about? If the first case applies to you, this Sublime Text plugin may be helpful (in the second case, do drop me a line if you find a good solution).

Place your cursor inside an equation-style environment and press <kbd>⌘</kbd>+<kbd>Shift</kbd>+<kbd>C</kbd> (<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>C</kbd> on Windows or Linux) to cycle between:

```latex
\[      \begin{equation}      \begin{equation*}      \begin{align}      \begin{align*}      $      \[
    =>                    =>                     =>                 =>                  =>     =>      => ...
\]      \end{equation}        \end{equation*}        \end{align}        \end{align*}        $      \]

```

Some details: for safety, this command only works if
* There is only one current selection (cursor) active
* Each equation delimiter is at the beginning of the line it appears on (excepting whitespace, e.g. indentation)
* The equation delimiters are within +/-10 lines of the current selection location

## Installation

Clone this repository into
* OS X: ```~/Library/Application Support/Sublime Text 3/Packages/LatexEquationToggle```
* Windows: ```%APPDATA%\Sublime Text 3\Packages\LatexEquationToggle```
* Linux: ```~/.config/sublime-text-3/Packages/LatexEquationToggle```
If anyone other than me ever uses this package (or even reads this sentence), I'll consider putting it on https://packagecontrol.io/. A bit of a chicken-and-egg thing perhaps.