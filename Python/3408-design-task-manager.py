# time complexity:
# add: O(log n) (SortedSet insertion)
# edit: O(log n) for remove + O(log n) for add = O(log n)
# rmv: O(log n) (SortedSet removal)
# execTop: O(1) to access last element, O(log n) for remove
# Initialization: O(n log n) for n initial tasks
# space complexity: O(n)
from typing import List
from sortedcontainers import SortedSet


class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.tasks = SortedSet()
        self.taskToUsers = {}
        self.taskToPriority = {}
        for user_id, task_id, priority in tasks:
            self.add(user_id, task_id, priority)
            
    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.tasks.add((priority, taskId, userId))
        self.taskToUsers[taskId] = userId
        self.taskToPriority[taskId] = priority
        
    def edit(self, taskId: int, newPriority: int) -> None:
        user = self.taskToUsers[taskId]
        self.rmv(taskId)
        self.add(user, taskId, newPriority)  
             
    def rmv(self, taskId: int) -> None:
        user = self.taskToUsers[taskId]        
        priority = self.taskToPriority[taskId]
        self.tasks.remove((priority, taskId, user))
        del self.taskToUsers[taskId]
        del self.taskToPriority[taskId]
        
    def execTop(self) -> int:
        if not self.tasks:
            return -1
        _, taskId, userId = self.tasks[-1]
        self.rmv(taskId)
        return userId




obj = TaskManager([[1, 101, 10], [2, 102, 20], [3, 103, 15]])
print(obj.add(4, 104, 5))
print(obj.edit(102, 8))
print(obj.execTop())
print(obj.rmv(101))
print(obj.add(5, 105, 15))
print(obj.execTop())
