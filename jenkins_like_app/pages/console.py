from nicegui import ui
from state import logs_state


def create_console_page(build_id: str) -> None:
    ui.label(f'Console Output - Build {build_id}').classes('text-2xl font-semibold mb-4')
    with ui.card().classes('p-0 overflow-hidden'):
        with ui.row().classes('items-center justify-between px-4 py-3 bg-card-header'):
            ui.label('Live Log').classes('text-lg font-medium')
            with ui.row().classes('gap-2'):
                ui.button('Clear', icon='clear', on_click=lambda: logs_state.clear(build_id)).props('dense')
        log_area = ui.log(max_lines=1000).classes('console-area')

        def refresh():
            log_area.clear()
            for line in logs_state.get(build_id):
                log_area.push(line)

        refresh()
        ui.timer(0.5, refresh)

