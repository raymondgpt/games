import random

# 初始化历史结果列表
history_results = []


def roll_dice():
    # 随机生成三个骰子的点数（1到6）
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)
#结果集 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
    # 计算三个骰子的总和
    total = dice1 + dice2 + dice3

    # 判断结果是“大”还是“小”
    # 如果总和在4到10之间，判定为“小”，在11到17之间判定为“大”,3和18是围筛

    if 4 <= total <= 10:
        result = "小"
    elif 11 <= total <= 17:
        result = "大"
    elif total == 3 or total == 18:
        result = "围骰"
    else:貌似可以了 奇怪 为啥我在这里不行呢 那为啥我在unterprter那里不行 这里可以呢
        result = "其他"

    # 把每次的结果存储到历史结果列表中
    history_results.append({
        "骰子点数": [dice1, dice2, dice3],
        "总和": total,
        "结果": result
    })

    # # 打印当前结果
    # print(f"骰子点数: {dice1}, {dice2}, {dice3} | 总和: {total} | 结果: {result}")


# 示例运行10次，查看结果
for _ in range(5):
    roll_dice()

# 打印历史结果
print("\n历史记录:")
for i, record in enumerate(history_results, 1):
    print(f"第 {i} 局: 骰子点数: {record['骰子点数']} | 总和: {record['总和']} | 结果: {record['结果']}")
