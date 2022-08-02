class TestClassInFolder:
    def __init__(self, input_1: float, input_2: float) -> None:
        self.input_1 = input_1
        self.input_2 = input_2

    def test_method(self):
        result = self.input_1 * self.input_2
        result_str = str(result)
        return "input_1 multiplied by input_2 in a folder! = " + result_str
