from dataclasses import dataclass
from typing import Tuple
import queue
import numpy as np
from environment import Env
from unit import Unit

@dataclass
class Task:

    @dataclass
    class Target:
        unitId: Unit
        product: np.ndarray

        def __init__(self, unitId: int, product: np.ndarray) -> None:
            # FIXME: unitid type
            self.unitId = unitId
            self.product = product

    endtime: int
    targets: list[Target]

@dataclass
class TaskQueue:
    env: Env
    tasks: queue.PriorityQueue[Tuple[int, Task]] = queue.PriorityQueue()

    def addTask(self, task: Task):
        self.tasks.put((task.endtime, task))

    def settleATask(self):
        cEndtime, cTask = self.tasks.get()
        for t in cTask.targets:
            newTask: Task = t.unit.produceTrigger()
            newTask.endtime += self.env.time # 校准时钟
            if newTask:
                self.addTask(newTask)
        self.env.setTime(cEndtime)