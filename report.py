import unittest
import HTMLTestRunner


def createsuite():
    testunit = unittest.TestSuite()
    test_dir = "./test_case"
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py", top_level_dir=None)

    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTest(test_case)
    return testunit


if __name__ == '__main__':
    report_file = "result.html"
    fp = open(report_file, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="报告", description="执行结果")
    runner.run(createsuite())
    fp.close()
