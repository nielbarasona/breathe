from textual.app import App, ComposeResult
from textual.widgets import DataTable
from .sheet import Sheet


class BreatheApp(App):
    def __init__(self, sheet: Sheet) -> None:
        self.sheet = sheet
        super().__init__()

    def compose(self) -> ComposeResult:
        yield DataTable()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns(*self.sheet.parts[0].format)
        table.add_rows(self.sheet.output())
