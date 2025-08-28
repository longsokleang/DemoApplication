from nicegui import ui
from state import builds_state


def _status_icon(status: str) -> str:
    return {
        'running': 'schedule',
        'success': 'check_circle',
        'failed': 'error',
        'queued': 'hourglass_empty',
    }.get(status, 'help')


def create_builds_page() -> None:
    ui.label('Builds').classes('text-2xl font-semibold mb-4')

    columns = [
        {'name': 'id', 'label': 'ID', 'field': 'id'},
        {'name': 'pipeline', 'label': 'Pipeline', 'field': 'pipeline'},
        {'name': 'status', 'label': 'Status', 'field': 'status'},
        {'name': 'duration', 'label': 'Duration', 'field': 'duration'},
        {'name': 'actions', 'label': '', 'field': 'actions'},
    ]

    table = ui.table(columns=columns, rows=[], row_key='id').classes('no-border')

    def refresh():
        rows = []
        for b in builds_state.builds:
            rows.append({
                'id': b.id,
                'pipeline': b.pipeline_name,
                'status': ui.row().classes('items-center gap-2').bind_children_from([ui.icon(_status_icon(b.status)), ui.label(b.status.capitalize())], 'children'),
                'duration': b.duration,
                'actions': ui.button('Console', icon='terminal', on_click=lambda bid=b.id: ui.open(f'/console/{bid}')).props('flat dense'),
            })
        table.rows = rows
        table.update()

    refresh()
    ui.timer(1.5, refresh)

