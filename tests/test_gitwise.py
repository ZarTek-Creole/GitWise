import unittest
from gitwise import check_repository_status, integrate_with_openai

class TestGitWise(unittest.TestCase):

    def test_check_repository_status(self):
        # Test the check_repository_status function
        result = check_repository_status()
        self.assertIn('status', result)
        self.assertIn('recommendations', result)
        self.assertEqual(result['status'], 'analysis complete')
        self.assertIsInstance(result['recommendations'], list)

    def test_integrate_with_openai(self):
        # Test the integrate_with_openai function
        data = {"status": "analysis complete", "recommendations": ["Consider squashing commits", "Feature branch might be beneficial"]}
        result = integrate_with_openai(data)
        self.assertIn('analysis', result)
        self.assertIsInstance(result['analysis'], str)

if __name__ == '__main__':
    unittest.main()