import unittest
import requests

class FlaskTest(unittest.TestCase):
    API_URL = "https://api-samuelsandoval-me.herokuapp.com/"
    
    def test_index(self):
        r = requests.get(self.API_URL)
        self.assertEqual(r.status_code, 200)

    def test_about(self):
        CURR_URL = "{}/about".format(self.API_URL)
        r = requests.get(CURR_URL)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.json()), 1)

    def test_education(self):
        CURR_URL = "{}/education".format(self.API_URL)
        r = requests.get(CURR_URL)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.json()), 1)

    def test_experience(self):
        CURR_URL = "{}/experience".format(self.API_URL)
        r = requests.get(CURR_URL)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.json()), 3)

    def test_gospel(self):
        CURR_URL = "{}/gospel".format(self.API_URL)
        r = requests.get(CURR_URL)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.json()), 2)
    
    def test_projects(self):
        CURR_URL = "{}/projects".format(self.API_URL)
        r = requests.get(CURR_URL)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.json()), 5)

    def test_error(self):
        CURR_URL = "{}/page".format(self.API_URL)
        r = requests.get(CURR_URL)
        self.assertEqual(r.status_code, 404)
    
if __name__ == '__main__':
    unittest.main()