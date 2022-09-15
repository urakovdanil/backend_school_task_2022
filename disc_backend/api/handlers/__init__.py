from .imports import ImportsView
from.delete import DeleteItemView
from .nodes import NodesView
from .updates import UpdatesView


HANDLERS = (
    UpdatesView,
    ImportsView,
    DeleteItemView,
    NodesView
)
