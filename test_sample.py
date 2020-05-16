import covid
import pytest

def test_raisesException_whenNoArguments():
    with pytest.raises(Exception):
        covid.main()
