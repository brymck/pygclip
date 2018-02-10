"""
    pygclip.io
    ~~~~~~~~~~~

    Input/output functionality.

    :copyright: © 2018 by Bryan Lee McKelvey.
    :license: MIT, see LICENSE for more details.
"""

import logging
from subprocess import Popen, PIPE
from typing import List, Union


def run_shell_command(args: List[str], stdin: Union[bytes, str, None]=None) -> str:
    logger = logging.getLogger(__name__)
    logger.debug('Running command: {}'.format(args))
    if stdin is None:
        process = Popen(args, stdout=PIPE)
        return process.communicate()[0].decode('utf-8')
    else:
        process = Popen(args, stdin=PIPE, stdout=PIPE)
        return process.communicate(stdin.encode('utf-8'))[0].decode('utf-8')


def _generate_hex(text: str) -> str:
    return run_shell_command(['hexdump', '-ve', '1/1 "%.2x"'], text)


def write_html_to_clipboard(html: str) -> None:
    hex_text = _generate_hex(html)
    run_shell_command(['osascript', '-e', u'set the clipboard to \xabdata HTML{}\xbb'.format(hex_text)])


