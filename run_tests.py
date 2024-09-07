# run_tests.py

import unittest

if __name__ == '__main__':
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_suite)