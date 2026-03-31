from .part import Part


class Sheet:
    def __init__(self, parts: list[Part] | None = None) -> None:
        self.parts = []
        if parts is not None:
            self.parts.extend(parts)

    def __repr__(self) -> str:
        return_string = []
        for part in self.parts:
            return_string.append(f"{part}")
        return "\n".join(return_string)
        # return f" {self.name} Date: {format_date(self.date)} Interval: {self.interval} Next Event: {format_date(self.next_event)}"

    def output(self) -> list:
        output_list = []
        for part in self.parts:
            output_list.append(part.output())
        return output_list
