from pugsql.statement import Raw, Statement
import pytest
from unittest import TestCase
from unittest.mock import Mock



def test_raw():
    assert Raw().transform('x') == 'x'


class StatementTest(TestCase):
    def test_no_engine(self):
        s = Statement('foo', 'select 1', '', Raw())
        self.assertRaises(RuntimeError, lambda: s())

    def test_no_name(self):
        with pytest.raises(ValueError, message='Statement must have a name.'):
            Statement(None, 'foo', '', Raw())

    def test_name_empty(self):
        with pytest.raises(ValueError, message='Statement must have a name.'):
            Statement('', 'foo', '', Raw())

    def test_sql_none(self):
        with pytest.raises(
                ValueError,
                message='Statement must have a SQL string.'):
            Statement('foo', None, '', Raw())

    def test_sql_empty(self):
        with pytest.raises(
                ValueError,
                message='SQL string cannot be empty.'):
            Statement('foo', '', '', Raw())

    def test_sql_whitespace(self):
        with pytest.raises(
                ValueError,
                message='SQL string cannot be empty.'):
            Statement('foo', '   ', '', Raw())

    def test_result_none(self):
        with pytest.raises(
                ValueError,
                message='Statement must have a result type.'):
            Statement('foo', 'select 1', '', None)
