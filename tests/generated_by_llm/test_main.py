import pytest
from unittest.mock import Mock, patch
from src.app import App

class TestApp:
    def setup_method(self):
        self.app = App()

    @patch('src.app.get_data')
    def test_get_data_success(self, mock_get_data):
        # Arrange
        mock_get_data.return_value = {"data": "success"}
        
        # Act
        result = self.app.get_data()
        
        # Assert
        assert result == {"data": "success"}
        mock_get_data.assert_called_once_with()

    @patch('src.app.get_data')
    def test_get_data_failure(self, mock_get_data):
        # Arrange
        mock_get_data.return_value = {"error": "failure"}
        
        # Act
        with pytest.raises(ValueError) as excinfo:
            self.app.get_data()
        
        # Assert
        assert str(excinfo.value) == "Failed to retrieve data: failure"
        mock_get_data.assert_called_once_with()

    @patch('src.app.get_data')
    def test_app_initialization(self, mock_get_data):
        # Arrange
        app = App()
        
        # Act
        result = app
        
        # Assert
        assert isinstance(result, App)
        assert not mock_get_data.called

if __name__ == "__main__":
    pytest.main(['-v', 'tests/test_main.py'])