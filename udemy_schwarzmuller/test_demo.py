import unittest
from unittest.mock import patch, MagicMock
import shutil
import demo  # Assuming your script is named demo.py

class TestDatabaseOperations(unittest.TestCase):

    @patch('shutil.copy')
    def test_backup_db_success(self, mock_copy):
        # Simulate successful copy
        demo.backup_db()
        mock_copy.assert_called_once_with(demo.active_db_file, demo.backup_db_file)

    @patch('shutil.copy', side_effect=FileNotFoundError)
    def test_backup_db_file_not_found(self, mock_copy):
        with self.assertLogs('root', level='ERROR') as cm:
            demo.backup_db()
            self.assertIn('Error: app.db not found.', cm.output[0])

    @patch('shutil.copy')
    def test_restore_db_success(self, mock_copy):
        # Simulate successful copy
        demo.restore_db()
        mock_copy.assert_called_once_with(demo.backup_db_file, demo.active_db_file)

    @patch('shutil.copy', side_effect=FileNotFoundError)
    def test_restore_db_file_not_found(self, mock_copy):
        with self.assertLogs('root', level='ERROR') as cm:
            demo.restore_db()
            self.assertIn('Error: backup.db not found.', cm.output[0])

if __name__ == '__main__':
    unittest.main()