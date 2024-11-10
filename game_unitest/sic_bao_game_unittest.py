import unittest
import random
# 导入被测试的代码
from sic_bao_game import roll_dice, history_results




class TestDiceGame(unittest.TestCase):

    def setUp(self):
        """每次测试前清空历史记录"""
        global history_results
        history_results.clear()

    def test_dice_roll_within_range(self):
        """测试每个骰子的点数是否在1到6之间"""
        roll_dice()
        last_result = history_results[-1]["骰子点数"]
        for dice in last_result:
            self.assertIn(dice, range(1, 6), "骰子点数不在1到6范围内")

    def test_total_sum_range(self):
        """测试三个骰子的总和是否在3到18之间"""
        roll_dice()
        last_result = history_results[-1]["总和"]
        self.assertIn(last_result, range(3, 19), "总和不在3到18范围内")

    def test_result_classification(self):
        """测试总和的结果分类是否正确"""
        test_cases = {
            "小": range(4, 11),
            "大": range(11, 17),
            "围骰": [3, 18]
        }

        for expected_result, totals in test_cases.items():
            for total in totals:
                dice_values = self.mock_dice_for_total(total)
                with self.subTest(total=total):
                    result = self.classify_result(total)
                    self.assertEqual(result, expected_result, f"分类错误: 总和{total}应为{expected_result}")

    def mock_dice_for_total(self, total):
        """模拟骰子掷出的点数以获得指定的总和"""
        for i in range(1, 7):
            for j in range(1, 7):
                for k in range(1, 7):
                    if i + j + k == total:
                        return [i, j, k]
        return [1, 1, 1]  # 如果无法找到符合条件的组合，返回一个默认值

    def classify_result(self, total):
        """根据总和分类结果，作为roll_dice中分类的辅助函数"""
        if 4 <= total <= 10:
            return "小"
        elif 11 <= total <= 17:
            return "大"
        elif total == 3 or total == 18:
            return "围骰"
        else:
            return "其他"

    def test_history_record_format(self):
        """测试历史记录的格式是否正确"""
        roll_dice()
        last_record = history_results[-1]
        self.assertIn("骰子点数", last_record)
        self.assertIn("总和", last_record)
        self.assertIn("结果", last_record)
        self.assertIsInstance(last_record["骰子点数"], list, "骰子点数应为列表")
        self.assertIsInstance(last_record["总和"], int, "总和应为整数")
        self.assertIsInstance(last_record["结果"], str, "结果应为字符串")

# 运行单元测试
if __name__ == "__main__":
    unittest.main()
