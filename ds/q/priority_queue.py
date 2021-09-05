from dataclasses import dataclass
from ds.q import Queue
from ds.linked_list.singly import Node, change_node_cls


@dataclass
class PNode(Node):
    priority: int


change_node_cls(PNode)


class PriorityQueue(Queue):
    pass


if __name__ == '__main__':
    pass
