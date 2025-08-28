from nicegui import ui
from state import pipelines_state


def _status_chip(status: str):
    color = {
        'running': 'warning',
        'success': 'positive',
        'failed': 'negative',
        'queued': 'info',
    }.get(status, 'grey')
    return ui.chip(status.capitalize(), color=color).props('dense')


def create_dashboard_page() -> None:
    ui.label('Dashboard').classes('text-2xl font-semibold mb-4')
    with ui.card().classes('p-0 overflow-hidden'):
        with ui.row().classes('items-center justify-between px-4 py-3 bg-card-header'):
            ui.label('Pipelines').classes('text-lg font-medium')
            ui.button('New Pipeline', icon='add', on_click=lambda: ui.notify('Not implemented')).props('unelevated')

        columns = [
            {'name': 'name', 'label': 'Name', 'field': 'name', 'align': 'left'},
            {'name': 'branch', 'label': 'Branch', 'field': 'branch'},
            {'name': 'status', 'label': 'Status', 'field': 'status'},
            {'name': 'duration', 'label': 'Duration', 'field': 'duration'},
            {'name': 'actions', 'label': '', 'field': 'actions'},
        ]

        table = ui.table(columns=columns, rows=[], row_key='id').classes('no-border')

        def refresh_table():
            rows = []
            for p in pipelines_state.pipelines:
                rows.append({
                    'id': p.id,
                    'name': p.name,
                    'branch': p.branch,
                    'status': _status_chip(p.status),
                    'duration': p.duration,
                    'actions': ui.button('Open', icon='open_in_new', on_click=lambda pid=p.id: ui.open(f'/console/{pid}')).props('flat dense'),
                })
            table.rows = rows
            table.update()

        refresh_table()
        ui.timer(1.0, refresh_table)

