import subprocess
import pygclip.io


def test_write_to_clipboard():
    """Test if `write_to_clipboard` pastes a string to the clipboard"""
    pygclip.io.write_to_clipboard('hello world')
    process = subprocess.Popen('pbpaste', stdout=subprocess.PIPE)
    contents = process.communicate()[0].decode('utf-8')
    assert contents == 'hello world'
