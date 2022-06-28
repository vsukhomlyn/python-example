import io
from unittest.mock import patch
from app.app import main


@patch('sys.stdout', new_callable=io.StringIO)
def test_main(stdout):
    with patch('builtins.input', side_effect=[1, 2]):
        main()
    assert stdout.getvalue() == 'Sum of a + b = 3\n'


@patch('sys.stdout', new_callable=io.StringIO)
def test_main_exception(stdout):
    with patch('builtins.input', side_effect=[1, 'a']):
        main()
    assert stdout.getvalue() == "Unexpected error : invalid literal for int() with base 10: 'a'" \
                                " invalid literal for int() with base 10: 'a'\n"
