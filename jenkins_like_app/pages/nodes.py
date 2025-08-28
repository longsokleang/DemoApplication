from nicegui import ui
from state import nodes_state


def create_nodes_page() -> None:
    ui.label('Nodes').classes('text-2xl font-semibold mb-4')

    columns = [
        {'name': 'name', 'label': 'Name', 'field': 'name', 'align': 'left'},
        {'name': 'labels', 'label': 'Labels', 'field': 'labels'},
        {'name': 'executors', 'label': 'Executors', 'field': 'executors'},
        {'name': 'status', 'label': 'Status', 'field': 'status'},
    ]

    table = ui.table(columns=columns, rows=[], row_key='name').classes('no-border')

    def refresh():
        rows = []
        for n in nodes_state.nodes:
            rows.append({
                'name': n.name,
                'labels': ', '.join(n.labels),
                'executors': f"{n.busy_executors}/{n.total_executors}",
                'status': ui.chip('Online' if n.online else 'Offline', color='positive' if n.online else 'negative').props('dense'),
            })
        table.rows = rows
        table.update()

    refresh()
    ui.timer(2.0, refresh)

