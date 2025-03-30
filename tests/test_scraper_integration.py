import unittest
import requests
from scraper import fetch_service_status

class TestScraperIntegration(unittest.TestCase):
    
    def test_fetch_service_status_real(self):
        """Real test: Make an actual request to the website."""
        try:
            service_data = fetch_service_status()

            # Ensure we got some data
            self.assertGreater(len(service_data), 0, "No services were fetched.")

            # Check that required fields exist in the response
            for service in service_data:
                self.assertIn("service_name", service)
                self.assertIn("status", service)
                self.assertIn("timestamp", service)

        except requests.RequestException as e:
            self.fail(f"Network request failed: {e}")

if __name__ == "__main__":
    unittest.main()
