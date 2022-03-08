import HtmlTestRunner
import unittest
from tests import apiTestcase

html_report_dir = './results/html_report' 
def run_test_suite_generate_html_report():
    # Create a TestSuite object.
    # initialize the test suite
    loader = unittest.TestLoader()
    test_suite = unittest.TestSuite()
    # Add test function in the suite.
    test_suite.addTests(loader.loadTestsFromModule(apiTestcase))
    # Create HtmlTestRunner object and run the test suite.
    test_runner = HtmlTestRunner.HTMLTestRunner(output=html_report_dir)
    test_runner.run(test_suite)
    
run_test_suite_generate_html_report()
