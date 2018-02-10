"""
    pygclip.io
    ~~~~~~~~~~~

    Input/output functionality.

    :copyright: © 2018 by Bryan Lee McKelvey.
    :license: MIT, see LICENSE for more details.
"""

import subprocess


def write_to_clipboard(output: str) -> None:
    process = subprocess.Popen('pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(output.encode('utf-8'))

