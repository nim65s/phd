#!/usr/bin/env python

"""
Pandoc filter to add some space between subfloats in latex
"""

from json import dumps
from pandocfilters import toJSONFilter, Para, RawInline


def space_subfloats(key, value, format, meta):
    if key == 'Div' and format == 'latex':
        if value[1][0] == {'t': 'RawBlock', 'c': ['tex', '\\begin{figure}\n\\centering']}:
            ret = []
            for val in value[1]:
                if '\\subfloat' in dumps(val):
                    started = False
                    subret = [RawInline('tex', '\\hspace*{\\fill}\n')]
                    for elt in val['c']:
                        if 'c' in elt and elt['c'] == ['tex', '\\subfloat']:
                            if started:
                                subret.append(RawInline('tex', '\\hfill%\n'))
                            else:
                                started = True
                        subret.append(elt)
                    subret.append(RawInline('tex', '\n\\hspace*{\\fill}\n'))
                    ret.append(Para(subret))
                else:
                    ret.append(val)
            return ret


if __name__ == "__main__":
    toJSONFilter(space_subfloats)
