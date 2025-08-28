from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Dict
import random
import time


@dataclass
class Pipeline:
    id: str
    name: str
    branch: str
    status: str
    duration: str


@dataclass
class Node:
    name: str
    labels: List[str]
    total_executors: int
    busy_executors: int
    online: bool


@dataclass
class Build:
    id: str
    pipeline_name: str
    status: str
    duration: str


class PipelinesState:
    def __init__(self) -> None:
        self.pipelines: List[Pipeline] = [
            Pipeline(id='101', name='Backend API', branch='main', status='running', duration='2m 10s'),
            Pipeline(id='102', name='Web App', branch='develop', status='queued', duration='—'),
            Pipeline(id='103', name='Mobile', branch='release', status='success', duration='5m 55s'),
        ]

    def random_update(self) -> None:
        if not self.pipelines:
            return
        pipeline = random.choice(self.pipelines)
        pipeline.status = random.choice(['running', 'success', 'failed', 'queued'])
        if pipeline.status == 'running':
            pipeline.duration = f"{random.randint(0, 9)}m {random.randint(0, 59)}s"


class NodesState:
    def __init__(self) -> None:
        self.nodes: List[Node] = [
            Node(name='master', labels=['linux', 'docker'], total_executors=2, busy_executors=1, online=True),
            Node(name='agent-1', labels=['linux', 'k8s'], total_executors=4, busy_executors=3, online=True),
            Node(name='agent-2', labels=['windows'], total_executors=1, busy_executors=0, online=False),
        ]

    def random_update(self) -> None:
        if not self.nodes:
            return
        node = random.choice(self.nodes)
        node.online = random.choice([True, True, True, False])
        node.busy_executors = min(node.total_executors, max(0, node.busy_executors + random.choice([-1, 0, 1])))


class BuildsState:
    def __init__(self) -> None:
        self.builds: List[Build] = [
            Build(id='201', pipeline_name='Backend API', status='running', duration='1m 12s'),
            Build(id='202', pipeline_name='Web App', status='queued', duration='—'),
            Build(id='203', pipeline_name='Mobile', status='success', duration='5m 55s'),
        ]

    def random_update(self) -> None:
        if not self.builds:
            return
        build = random.choice(self.builds)
        build.status = random.choice(['running', 'success', 'failed', 'queued'])
        if build.status == 'running':
            build.duration = f"{random.randint(0, 9)}m {random.randint(0, 59)}s"


class LogsState:
    def __init__(self) -> None:
        self.logs_by_build: Dict[str, List[str]] = {}

    def append(self, build_id: str, line: str) -> None:
        self.logs_by_build.setdefault(build_id, []).append(line)
        if len(self.logs_by_build[build_id]) > 1000:
            self.logs_by_build[build_id] = self.logs_by_build[build_id][-1000:]

    def get(self, build_id: str) -> List[str]:
        return self.logs_by_build.get(build_id, [])

    def clear(self, build_id: str) -> None:
        self.logs_by_build[build_id] = []


pipelines_state = PipelinesState()
nodes_state = NodesState()
builds_state = BuildsState()
logs_state = LogsState()

