class Counter:
    def __init__(self, current=1, min_value=0, max_value=10):
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

    def set_current(self, start):
        self.current = start

    def set_max(self, max_value):
        self.max_value = max_value

    def set_min(self, min_value):
        self.min_value = min_value

    def step_up(self):
        if self.current >= self.max_value:
            raise ValueError("Достигнут максимум")
        self.current += 1

    def step_down(self):
        if self.current <= self.min_value:
            raise ValueError("Достигнут минимум")
        self.current -= 1

    def get_current(self):
        return self.current

counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10, 'Test1'
try:
    counter.step_up()
except ValueError as e:
    print(e) 
assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7, 'Test3'
try:
    counter.step_down() 
except ValueError as e:
    print(e) 
assert counter.get_current() == 7, 'Test4'