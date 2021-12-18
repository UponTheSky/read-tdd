class TestCase:
    def __init__(self, name):
        self.name = name

    def set_up(self):
        pass

    def run(self):
        self.set_up()
        method = getattr(self, self.name)
        method()
        
class WasRun(TestCase):
    def __init__(self, name):
        super().__init__(name)
        self.was_run = None

    def test_method(self):
        self.was_run = 1
        
    def set_up(self):
        self.was_run = None
        self.was_set_up = 1

    def was_set_up(self):
        self.was_set_up = 1