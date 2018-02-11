from io import StringIO
from subprocess import Popen, PIPE
import sys
import pytest

from pygclip.cli import main


def test_main_with_file(resource):
    """Test that the entry point will complete for a simple file."""
    sys.argv = ['pygclip', '-s', 'monokai', '-l', 'python', resource('simple.py')]
    main()


def test_main_with_stdin(clipboard, resource):
    """Test that the entry point will complete reading from standard input."""
    sys.argv = ['pygclip', '-s', 'monokai', '-l', 'python', resource('simple.py')]
    main()
    file_result = clipboard()

    old_stdin = sys.stdin
    with open(resource('simple.py'), 'r') as f:
        sys.stdin = StringIO(f.read())
    sys.argv = ['pygclip', '-s', 'monokai', '-l', 'python']
    main()
    stdin_result = clipboard()
    sys.stdin = old_stdin

    assert file_result == stdin_result


def test_main_with_clipboard(clipboard, resource):
    """Test that the entry point will complete reading from the clipboard."""
    sys.argv = ['pygclip', '-s', 'monokai', '-l', 'python', resource('simple.py')]
    main()
    file_result = clipboard()

    sys.argv = ['pygclip', '-s', 'monokai', '-l', 'python', '-c']
    with open(resource('simple.py'), 'r') as f:
        text = f.read()
    Popen(['pbcopy'], stdin=PIPE).communicate(text.encode('utf-8'))
    main()
    clipboard_result = clipboard()

    assert file_result == clipboard_result


def test_main_fails_with_blank_clipboard():
    """Test that the entry point will fail when reading from a blank clipboard."""
    Popen(['osascript', '-e', 'set the clipboard to ""']).communicate()
    sys.argv = ['pygclip', '-s', 'monokai', '-l', 'python', '-c']
    with pytest.raises(ValueError):
        main()
