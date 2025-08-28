import random
import threading
import time
from state import pipelines_state, nodes_state, builds_state, logs_state


def _background_loop():
    while True:
        # Simulate updates
        pipelines_state.random_update()
        nodes_state.random_update()
        builds_state.random_update()

        # Simulate logs
        for build in builds_state.builds:
            if build.status == 'running':
                logs_state.append(build.id, f"[{time.strftime('%H:%M:%S')}] {random.choice(['Compiling', 'Testing', 'Linting', 'Packaging'])}...")

        time.sleep(1)


def start_background_updater() -> None:
    thread = threading.Thread(target=_background_loop, daemon=True)
    thread.start()

