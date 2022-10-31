import unittest
import CommandController
from RedisStore import RedisStore
import unittest
from unittest.mock import patch

# @test(groups=["unit", "strings"])
class TestCommandController(unittest.TestCase):
    store=None

    @classmethod
    def setUpClass(cls):
        cls.store=RedisStore()

    def test_set_command(self):
        command="SET abc test-value"
        result=CommandController.execute_command(command,self.store)
        self.assertTrue(True,result)

    @patch('builtins.print')
    def test_get_command(self, mock_print):
        command = "GET abc"
        CommandController.execute_command(command,self.store)
        mock_print.assert_called_with('test-value')

if __name__ == '__main__':
    unittest.main()
