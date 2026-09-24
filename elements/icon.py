from elements.base_element import BaseElement


class Icon(BaseElement):
    @property
    def type_of(self) -> str:  # Переопределяем свойство type_of
        return "icon"
