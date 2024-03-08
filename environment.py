from dataclasses import dataclass
import numpy as np
from mapGraph import MapGraph

from person import Person
from unit import Unit

@dataclass
class Env:
    naturalResources: np.ndarray
    naturalResourcesInventory: np.ndarray
    personList: list[Person]
    unitList: list[Unit]
    map: MapGraph
    priceVector: np.ndarray
    timePeriod: int
    time: int = 0

    def setTime(self, time: int):
        self.time = time
