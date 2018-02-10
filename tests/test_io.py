import subprocess
import pygclip.io


def test_clipboard():
    pygclip.io.write_to_clipboard('hello world')
    process = subprocess.Popen('pbpaste', stdout=subprocess.PIPE)
    contents = process.communicate()[0].decode('utf-8')
    assert contents == 'hello world'
