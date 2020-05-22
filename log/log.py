import logging
import logging.config
import pathlib
import yaml


def setup_logging(path='logging.yaml', default_level=logging.INFO):
    """Reads a log configuration file."""
    p = pathlib.Path(path)

    if p.exists():
        print('Loading logger config from file.')
        configuration = yaml.safe_load(p.read_bytes())
        configuration['root']['level'] = default_level.upper() if isinstance(default_level, str) else default_level
        logging.config.dictConfig(configuration)
    else:
        print('Loading default logger config.')
        logging.basicConfig(level=default_level)