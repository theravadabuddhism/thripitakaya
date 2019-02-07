import os


def compile(path: str, info):
    header = rf'''
\documentclass[12]{{article}}
\usepackage[a4paper,left=2.5cm, right=2.5cm, top=2.5cm, bottom=2.5cm]{{geometry}}
\usepackage{{fontspec,xltxtra,xunicode}}

\setlength{{\headheight}}{{15.2pt}}

\font\serif="FreeSerif:script=sinh"
\font\serifbb="FreeSerif:script=sinh" at 10pt
\font\serifsection="FreeSerif:script=sinh" at 12pt
\font\deffont="FreeSerif:script=sinh" at 10pt

\sloppy

\date{{}}
\title{{\serif {info[2]}}}
\begin{{document}}

\deffont

\maketitle

{generate_unit(path, info)}

\end{{document}}

    '''
    with open('output/main.tex', 'w') as outfile:
        outfile.write(header)
        os.chdir("output")
    os.system("xelatex main.tex")


def generate_unit(path: str, info: dict):
    res = ""
    with open(path, 'r') as file:
        title = next(file).strip()
        assert title == info[2]
        for line in file:
            line = line.rstrip()
            if line.startswith('###'):
                res += rf"\section*{{\serifsection {line[3:]}}}"
            elif line.startswith('##'):
                res += rf"\subsection*{{\serifsection {line[2:]}}}"
            elif line.startswith('#'):
                res += f"{line[1:]}. "
            else:
                res += line
            res += "\n"
    return res
