# price_data.py
from .utils.BudgetCalculator import budget_calculator

# 定義價格資料，這裡可以根據需求載入不同的資料
price_tw = {
    "機+酒": 
        10000,
}

price_hk = {
    "車資": 
        0
}

# 設定參數
num_people = 1  # 人數
exchange_rate = 0.21  # 匯率
fixed_costs = { 
    "購物" : 0,
    "購物" : 0    
    }  # 預估費用

# create_info
create_info = budget_calculator(
    domestic_costs= price_tw, 
    foreign_costs= price_hk, 
    fixed_costs= fixed_costs, 
    num_people=num_people, 
    exchange_rate=exchange_rate
    )

budget_table = create_info.generate_budget_table()
total_text = create_info.generate_total_text()