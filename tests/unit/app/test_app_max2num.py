import io
from unittest.mock import patch
from app.app_max2num import main


@patch('sys.stdout', new_callable=io.StringIO)
def test_main(stdout):
    with patch('builtins.input', side_effect=[1, 2]):
        main()
    assert stdout.getvalue() == 'Max of a and b is 2\n'


@patch('sys.stdout', new_callable=io.StringIO)
def test_main_exception(stdout):
    with patch('builtins.input', side_effect=[1, 'a']):
        main()
    assert stdout.getvalue() == "Unexpected error : invalid literal for int() with base 10: 'a'\n"
