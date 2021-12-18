from abc import abstractmethod

class TestCase:
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def set_up(self):
        pass

    @abstractmethod
    def tear_down(self):
        pass

    def run(self):
        result = TestResult()
        result.test_started()
        self.set_up()
        try:
            method = getattr(self, self.name)
            method()
        except:
            result.test_failed()
        self.tear_down()
        return result
        
class WasRun(TestCase):
    def __init__(self, name):
        super().__init__(name)
        self.was_run = None

    def test_method(self):
        self.was_run = 1
        self.log += " test_method"
        
    def set_up(self):
        self.was_run = None
        self.log = "set_up"

    def tear_down(self):
        self.log += " tear_down"

    def test_broken_method(self):
        raise Exception()

class TestResult:
    def __init__(self):
        self.run_count = 0
        self.error_count = 0
    
    def test_started(self):
        self.run_count += 1

    def test_failed(self):
        self.error_count += 1

    def summary(self):
        return f"{self.run_count} run, {self.error_count} failed"
