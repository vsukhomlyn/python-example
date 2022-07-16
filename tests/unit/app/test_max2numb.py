import io
from unittest.mock import patch
from app.max2numb import max2numb


@patch('sys.stdout', new_callable=io.StringIO)
def test_main(stdout):
    with patch('builtins.input', side_effect=[1, 2]):
        max2numb()
    assert stdout.getvalue() == 'Max is b: 2\n'


@patch('sys.stdout', new_callable=io.StringIO)
def test_main_exception(stdout):
    with patch('builtins.input', side_effect=[1, 'a']):
        max2numb()
    assert stdout.getvalue() == "Unexpected error : invalid literal for int() with base 10: 'a'" \
                                " invalid literal for int() with base 10: 'a'\n"

