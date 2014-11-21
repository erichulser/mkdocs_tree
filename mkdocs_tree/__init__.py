from mkdocs import events

from . import build
from . import config as tree_config

def includeme(config):
    """
    Intitializes the `tree` extension for mkdocs.

    ### Parameters
        config | <dict>
    """
    tree_config.docs_dir = config.get('docs_dir', 'docs')
    events.register_callback(events.BuildPage, build.create_tree)