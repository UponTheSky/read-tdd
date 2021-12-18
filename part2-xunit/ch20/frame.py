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
        self.set_up()
        method = getattr(self, self.name)
        method()
        self.tear_down()
        
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