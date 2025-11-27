from abc import ABC, abstractmethod
from typing import List
from app.models.expense import Expense

# 1. 策略介面 (Abstract Strategy)
class AnalysisStrategy(ABC):
    @abstractmethod
    def analyze(self, data: List[Expense]) -> float:
        pass

# 2. 具體策略 (Concrete Strategies)
class TotalAmountStrategy(AnalysisStrategy):
    def analyze(self, data: List[Expense]) -> float:
        if not data: return 0.0
        return sum(item.amount for item in data)

class AverageAmountStrategy(AnalysisStrategy):
    def analyze(self, data: List[Expense]) -> float:
        if not data: return 0.0
        total = sum(item.amount for item in data)
        return round(total / len(data), 2)

# 3. Context
class ExpenseAnalyzer:
    def __init__(self, strategy: AnalysisStrategy):
        self.strategy = strategy

    def execute(self, data: List[Expense]) -> float:
        return self.strategy.analyze(data)

# 工廠方法：根據字串產生對應的策略物件 (簡單工廠)
def get_strategy(strategy_type: str) -> AnalysisStrategy:
    strategies = {
        "total": TotalAmountStrategy(),
        "average": AverageAmountStrategy()
    }
    return strategies.get(strategy_type, TotalAmountStrategy())