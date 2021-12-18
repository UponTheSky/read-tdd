from frame import TestCase, WasRun, TestResult, TestSuite

class TestCaseTest(TestCase):
    def __init__(self, name):
        super().__init__(name)
        self.result = TestResult()

    def test_template_method(self):
        test = WasRun("test_method")
        test.run(self.result)
        assert(test.log == "set_up test_method tear_down")

    def test_result(self):
        test = WasRun("test_method")
        test.run(self.result)
        assert("1 run, 0 failed" == self.result.summary())

    def test_failed_result(self):
        test = WasRun("test_broken_method")
        test.run(self.result)
        assert("1 run, 1 failed" == self.result.summary())

    def test_failed_result_formatting(self):
        self.result.test_started()
        self.result.test_failed()
        assert("1 run, 1 failed" == self.result.summary())

    def test_suite(self):
        suite = TestSuite()
        suite.add(WasRun("test_method"))
        suite.add(WasRun("test_broken_method"))
        suite.run(self.result)
        assert("2 run, 1 failed" == self.result.summary())

suite = TestSuite()
tests = [
    "test_template_method", 
    "test_result", 
    "test_failed_result_formatting", 
    "test_failed_result",
    "test_suite"
]

for test in tests:
    suite.add(TestCaseTest(test))

# result = TestResult()
# suite.run(result)
# print(result.summary())
