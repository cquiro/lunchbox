from enum import Enum

class ChoiceEnum(Enum):
    @classmethod
    def choices(choice_list):
        return tuple((choice_item.name, choice_item.value) for choice_item in choice_list)
