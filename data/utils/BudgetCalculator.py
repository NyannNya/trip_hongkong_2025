# BudgetCalculator.py

class budget_calculator:
    def __init__(self, domestic_costs, foreign_costs, fixed_costs, num_people=1, exchange_rate=1):
        self.domestic_costs = domestic_costs
        self.foreign_costs = foreign_costs
        self.fixed_costs = fixed_costs
        self.num_people = num_people
        self.exchange_rate = exchange_rate

    @staticmethod
    def format_amount(amount, divisor=1, multiplier=1):
        """格式化金額，並以千分位顯示"""
        return "{:,}".format(int(amount / divisor * multiplier))

    def generate_budget_table(self):
        """
        根據各地區費用字典自動生成預算表，並考慮人數和匯率的參數。
        """
        budget_table = {"項目": [], "金額": []}
        
        # 處理國內項目，考慮人數
        for item, amount in self.domestic_costs.items():
            budget_table["項目"].append(item)
            budget_table["金額"].append(self.format_amount(amount, divisor=self.num_people))
        
        # 處理國外項目，考慮匯率
        for item, amount in self.foreign_costs.items():
            budget_table["項目"].append(item)
            budget_table["金額"].append(self.format_amount(amount, multiplier=self.exchange_rate))
        
        # 處理固定費用
        for item, amount in self.fixed_costs.items():
            budget_table["項目"].append(item)
            budget_table["金額"].append(self.format_amount(amount))
        
        return budget_table

    def generate_total_text(self):
        """生成總計文字，考慮人數和匯率"""
        total_domestic = sum(self.domestic_costs.values())
        total_foreign = sum(self.foreign_costs.values())
        total_fixed = sum(self.fixed_costs.values())
        total = total_domestic / self.num_people + round(total_foreign * self.exchange_rate, 0)
        formatted_price = f"{total:,.0f}"
        return f"{formatted_price} + {self.format_amount(total_fixed)} ≒ {total + total_fixed:.0f} / 1人"
