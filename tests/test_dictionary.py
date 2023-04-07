from typer.testing import CliRunner

from dictionary import cli

runner = CliRunner()

def test_integer_word():
    result = runner.invoke(cli.app, ["word","123"])
    assert "Please enter a valid word, integers are not allowed." in result.stdout

def test_incorrect_word():
    result = runner.invoke(cli.app, ["word", "askjdgf"])
    assert "Please provide a valid word." in result.stdout

def test_special_char_in_word():
    result = runner.invoke(cli.app, ["word", "as^&jdgf"])
    assert "Please provide a valid word." in result.stdout