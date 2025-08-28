from nicegui import ui


def header_bar() -> None:
    with ui.header().classes('bg-primary text-white shadow-md'):
        with ui.row().classes('w-full items-center justify-between px-4 py-2'):
            with ui.row().classes('items-center gap-3'):
                ui.icon('engineering').classes('text-2xl')
                ui.label('Jenkins-like').classes('text-xl font-semibold')
            with ui.row().classes('items-center gap-4'):
                ui.input('Search').props('dense standout').classes('w-64')
                ui.button(icon='account_circle').props('flat round dense')


def sidebar_nav() -> None:
    with ui.left_drawer().classes('bg-sidebar text-white'):
        ui.label('Navigation').classes('px-4 py-3 text-sm opacity-80')
        with ui.list().classes('px-0'):
            with ui.item(on_click=lambda: ui.open('/')):
                ui.icon('dashboard').classes('mr-3')
                ui.item_section('Dashboard')
            with ui.item(on_click=lambda: ui.open('/nodes')):
                ui.icon('dns').classes('mr-3')
                ui.item_section('Nodes')
            with ui.item(on_click=lambda: ui.open('/builds')):
                ui.icon('view_list').classes('mr-3')
                ui.item_section('Builds')


def jenkins_layout(content_builder) -> None:
    header_bar()
    sidebar_nav()
    with ui.page_sticky(position='bottom-right', x_offset=20, y_offset=20):
        ui.button(icon='help', on_click=lambda: ui.notify('Help is not implemented'))
    with ui.container().classes('p-4'):
        content_builder()

