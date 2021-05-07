"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employees_dict = dict()
        for employe in employees:
            employees_dict[employe.id] = employe
        r = 0

        def foo(id: int, r: int) -> int:
            employe = employees_dict[id]
            r = employe.importance
            if not employe.subordinates:
                return r
            for e_id in employe.subordinates:
                r += foo(e_id, r)
            return r
        r = foo(id, r)
        return r
