class ScoringEngine:
    def __init__(self):
        self.benchmarks = {
            "healthcare": {"recommended": 3.5, "weight": 1.2},
            "education": {"recommended": 0.6, "weight": 1.1},
            "water": {"recommended": 100, "weight": 1.3},
            "sanitation": {"recommended": 100, "weight": 1.1},
            "transport": {"recommended": 5.0, "weight": 1.0},
            "green_space": {"recommended": 9.0, "weight": 0.8},
            "housing": {"recommended": 300, "weight": 1.2},
            "electricity": {"recommended": 100, "weight": 1.3},
        }
 
    def score_plan(self, user_input):
        budget = user_input.get("budget", 1000000)
        population = user_input.get("population", 50000)
        current_state = user_input.get("current_state", {})
        priorities = user_input.get("priorities", {})
 
        sector_gaps = {}
        for sector in self.benchmarks.keys():
            current_value = current_state.get(sector, 0)
            benchmark = self.benchmarks[sector]["recommended"]
            
            if population > 0:
                current_normalized = (current_value / population) * 1000
            else:
                current_normalized = 0
            
            if benchmark > 0:
                gap = max(0, (benchmark - current_normalized) / benchmark)
            else:
                gap = 0
            
            gap = min(gap, 1.0)
            
            base_weight = self.benchmarks[sector]["weight"]
            priority_mult = priorities.get(sector, 1.0)
            weighted_gap = gap * base_weight * priority_mult
            
            sector_gaps[sector] = {
                "current": current_value,
                "gap_score": gap,
                "weighted_gap": weighted_gap,
            }
 
        total_weighted = sum(g["weighted_gap"] for g in sector_gaps.values())
        if total_weighted == 0:
            total_weighted = 1.0
 
        allocation_percentages = {}
        final_allocation = {}
        
        for sector in self.benchmarks.keys():
            if sector in sector_gaps:
                pct = (sector_gaps[sector]["weighted_gap"] / total_weighted) * 100
            else:
                pct = 0
            
            allocation_percentages[sector] = round(pct, 1)
            final_allocation[sector] = int((pct / 100) * budget)
 
        return {
            "sector_gaps": sector_gaps,
            "allocation_percentages": allocation_percentages,
            "final_allocation": final_allocation,
            "population": population,
            "budget": budget,
        }
 