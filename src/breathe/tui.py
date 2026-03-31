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
        table.add_columns("Name", "Date")
        for part in self.sheet.parts:
            table.add_row(f"{part.name}", f"{part.date}")
