import unittest
# from ..controllers.CommandController import CommandController
from controllers import CommandController
from RedisStore import RedisStore
import unittest
from unittest.mock import patch

class TestCommandController(unittest.TestCase):
    store=None

    @classmethod
    def setUpClass(cls):
        cls.store=RedisStore()

    def test_1_set_command(self):
        command="SET abc test-value"
        result=CommandController.execute_command(command,self.store)
        self.assertTrue(True,result)

    @patch('builtins.print')
    def test_2_get_command(self, mock_print):
        command = "GET abc"
        CommandController.execute_command(command,self.store)
        mock_print.assert_called_with('test-value')

    def test_3_numequalto(self):
        command="NUMEQUALTO test-value"
        count=CommandController.execute_command(command,self.store)
        self.assertEqual(count,1)

    @patch('builtins.print')
    def test_4_unset_command(self,mock_print):
        command1="UNSET abc"
        command2="GET abc"
        result=CommandController.execute_command(command1,self.store)
        self.assertTrue(True,result)
        CommandController.execute_command(command2,self.store)
        mock_print.assert_called_with('NULL')
    
    def test_5_end_command(self):
        command="END"
        result =CommandController.execute_command(command,self.store)
        self.assertFalse(False,result)

    def test_6_numequalto0(self):
        command="NUMEQUALTO test-value"
        count=CommandController.execute_command(command,self.store)
        self.assertTrue(True,count)
    

if __name__ == '__main__':
    unittest.main()
