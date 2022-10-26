from utils import division
from utils import funk_one
from utils import sqrt
from utils import funk_two
from utils import check_simple
from utils import find_max_index
from utils import number_conversion
import pytest

# тест нескольких функций с помощью библиотеки pytest v7.2.0


@pytest.mark.parametrize('a,b, expected_result', [(10, 2, 5),
                                                  (14, 2, 7),
                                                  (20, 5, 4),
                                                  (12, 3, 4),
                                                  (8, 2, 4)])
def test_answer(a, b, expected_result):
    assert division(a, b) == expected_result


@pytest.mark.parametrize('x, res', [(3, 21),
                                    (5, 50),
                                    (7, 91),
                                    (8, 116)])
def test_funk_one(x, res):
    assert funk_one(x) == res


@pytest.mark.parametrize('a, result', [(4, 2),
                                       (25, 5),
                                       (49, 7),
                                       (121, 11)])
def test_sqrt(a, result):
    assert sqrt(a) == result


@pytest.mark.parametrize('y, rult', [(7, 2.6457513110645907),
                                     (11, 3.3166247903554),
                                     (0, 0),
                                     (3, 1.7320508075688772)])
def test_sqrt(y, rult):
    assert sqrt(y) == rult


@pytest.mark.parametrize('expected_exception, division_n, divider', [(ZeroDivisionError, 10, 0),
                                                                     (TypeError, 10, "3")])
def test_error(expected_exception, division_n, divider):
    with pytest.raises(expected_exception):
        division(division_n, divider)


list_example = [(3, True), (5, True), (7, True), (8, False)]


@pytest.mark.parametrize('num, out', list_example)
def test_check_simple(num, out):
    assert check_simple(num) == out


@pytest.mark.parametrize('input_list, maxa', [([2, 3, 4, 5, 6], 6), ([7, 9, 3, 1, 0, 5], 9)])
def test_find_max_index(input_list, maxa):
    assert find_max_index(input_list) == maxa


list_example_two = [(3, '11'), (5, '101'), (7, '111')]


@pytest.mark.parametrize('number, binary', list_example_two)
def test_number_conversion(number, binary):
    assert number_conversion(number) == binary
