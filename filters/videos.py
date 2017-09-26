#!/usr/bin/env python3

"""
Pandoc filter to convert markdown's "%[caption](my_video.mp4)"
to html5 & latex video tags

Same syntax as https://github.com/rekado/parkdown#extensions
"""

from subprocess import run, PIPE

from pandocfilters import RawBlock, toJSONFilter

WIDTH = 12.8
PDFPC = False

FORMATS = {
    'latex': ['beamer'],
    'html': ['revealjs', 'html', 'html5'],
}
TEMPLATES = {
    'latex': r"""\begin{figure}[htbp]
        \centering
        \noindent\makebox[\textwidth]{%s}
        \caption{%s}
        \end{figure}""",
    'html': r"""<figure>
        <video controls>
        <source src='%s' type='video/mp4'>
        Your player does not support the video tag
        </video>
        <figcaption>%s</figcaption>
        </figure>""",
    'pdfpc': r"\href{run:%s?loop&autostart}{\includegraphics[width=%fcm,height=%fcm]{%s.jpg}}",
    'movie': r"\movie[width=%fcm,height=%fcm,autostart]{\includegraphics[width=%fcm]{%s.jpg}}{%s}",
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
        width = WIDTH
        opt = value[1]['c'][0]
        if len(opt) > 2:
            for key, val in opt[2]:
                if key == 'width' and val.endswith('%'):
                    width *= int(val[:-1]) / 100

        # get video height
        ffmpeg = run(['ffmpeg', '-i', src], stderr=PIPE).stderr.decode().split('\n')
        for line in ffmpeg:
            if 'Stream' in line:
                for word in line.split():
                    if 'x' in word and not word.startswith('0x'):
                        resolution = word
                        break
                else:
                    raise ValueError('resolution not found in %s' % line)
                break
        else:
            raise ValueError('stream not found in %s' % ffmpeg)
        x, y = resolution.split('x')
        height = int(y) * width / int(x)
        for fmt_name, fmt_values in FORMATS.items():
            if format in fmt_values:
                if PDFPC:
                    movie = TEMPLATES['pdfpc'] % (src, width, height, src)
                else:
                    movie = TEMPLATES['movie'] % (width, height, width, src, src)
                return [RawBlock(fmt_name, TEMPLATES[fmt_name] % (movie, title))]


if __name__ == "__main__":
    toJSONFilter(media)
