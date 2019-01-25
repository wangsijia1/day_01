import allure
class Test_02:
    @allure.step(title="我是test_01测试步骤")
    def test_01(self):
        print("test_01")
        assert True
    @allure.step(title="我是test_02测试步骤")
    def test_02(self):
        print("test_02")
        assert  False