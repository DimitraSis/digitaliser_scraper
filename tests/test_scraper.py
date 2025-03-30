import unittest
from unittest.mock import patch, MagicMock
from scraper import fetch_service_status
import json

class TestScraper(unittest.TestCase):

    @patch("scraper.requests.get")  # Correct target
    def test_fetch_service_status(self, mock_get):
        # Setup the mock response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = """
            <div class="item">
                <strong data-servicevariable="Description">Service A</strong>
                <span class="info">Status: Operational</span>
            </div>
        """
        mock_get.return_value = mock_response

        # Call the function to be tested
        service_data = fetch_service_status()

        # Assert that the function returns the expected data
        self.assertEqual(len(service_data), 1)
        self.assertEqual(service_data[0]['service_name'], 'Service A')
        self.assertEqual(service_data[0]['status'], 'Operational')




if __name__ == "__main__":
    unittest.main()
