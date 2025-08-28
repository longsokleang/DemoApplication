from pathlib import Path
from nicegui import ui, app

# Local imports
from components.layout import jenkins_layout
from pages.dashboard import create_dashboard_page
from pages.nodes import create_nodes_page
from pages.builds import create_builds_page
from pages.console import create_console_page
from data import start_background_updater


ASSETS_DIR = Path(__file__).parent / 'assets'
app.add_static_files('/static', str(ASSETS_DIR))


def include_theme() -> None:
    """Inject the Jenkins-inspired theme stylesheet into the document head."""
    ui.add_head_html('<link rel="stylesheet" href="/static/theme.css">')


def page_with_layout(page_builder):
    """Render a page inside the common Jenkins-like layout."""
    include_theme()
    jenkins_layout(page_builder)


@ui.page('/')
def index_page() -> None:
    page_with_layout(create_dashboard_page)


@ui.page('/nodes')
def nodes_page() -> None:
    page_with_layout(create_nodes_page)


@ui.page('/builds')
def builds_page() -> None:
    page_with_layout(create_builds_page)


@ui.page('/console/{build_id}')
def console_page(build_id: str) -> None:
    include_theme()
    jenkins_layout(lambda: create_console_page(build_id))


if __name__ == '__main__':
    # Start background data simulation and run the app
    start_background_updater()
    ui.run(title='Jenkins-like CI Dashboard', reload=False)

