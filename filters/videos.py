#!/usr/bin/env python3

"""
Pandoc filter to convert markdown's "%[caption](my_video.mp4)"
to html5 & latex video tags

Same syntax as https://github.com/rekado/parkdown#extensions
"""

from subprocess import run, PIPE

from pandocfilters import RawBlock, toJSONFilter

WIDTH = 12.8
FORMATS = {
        'latex': ['beamer'],
        'html': ['revealjs', 'html', 'html5'],
        }
TEMPLATES = {
        'latex': r"""\begin{figure}[htbp]
        \centering
        \noindent\makebox[\textwidth]{\movie[width=%fcm,height=%fcm,autostart]{\includegraphics[width=%fcm]{%s.jpg}}{%s}}
        \caption{%s}
        \end{figure}""",
        'html': r"""<figure>
        <video controls>
        <source src='%s' type='video/mp4'>
        Your player does not support the video tag
        </video>
        <figcaption>%s</figcaption>
        </figure>""",
        }
PERCENT = {
        't': 'Str',
        'c': '%',
        }


def media(key, value, format, meta):
    if key == 'Para' and value[0] == PERCENT and value[1]['t'] == 'Link':
        # get filename and caption
        title, src = value[1]['c'][1], value[1]['c'][2][0]
        title = ' '.join(d['c'] for d in title if d['t'] == u'Str')

        # get video height
        for line in run(['ffmpeg', '-i', src], stderr=PIPE).stderr.decode().split('\n'):
            if 'Stream' in line:
                for word in line.split():
                    if 'x' in word and not word.startswith('0x'):
                        resolution = word
                        break
                break
        width, height = resolution.split('x')
        height = int(height) * WIDTH / int(width)
        for fmt_name, fmt_values in FORMATS.items():
            if format in fmt_values:
                return [RawBlock(fmt_name, TEMPLATES[fmt_name] % (WIDTH, height, WIDTH, src, src, title))]


if __name__ == "__main__":
    toJSONFilter(media)
