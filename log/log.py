import logging
import logging.config
import pathlib
import yaml


def setup_logging(path='logging.yaml', log_dir=None, mk_log_dir=True, default_level=logging.INFO):
    """
    Reads a log configuration file, and if that logging configuration can't be found,
    the default configuration will be read in.
    :param path: a path to the logging configuration file - defaults as adjacent to the script
    calling the log module
    :param log_dir: a directory to emit logs to - defaults to None so adjacent to the caller location
    :param mk_log_dir: a boolean on whether or not to create the logging directories if found
    :param default_level: sets the default level of logging.
    :return: None
    """
    p = pathlib.Path(path)

    if p.exists():
        print('Loading logger config from file.')
        configuration = yaml.safe_load(p.read_bytes())
        configuration['root']['level'] = default_level.upper() if isinstance(default_level, str) else default_level

        if log_dir:
            set_output_dir(log_dir, configuration, mkdir=mk_log_dir)

        logging.config.dictConfig(configuration)

    else:
        print('Loading default logger config.')
        logging.basicConfig(level=default_level)


def set_output_dir(log_dir, configuration, mkdir=True):
    """
    By default, the logging configuration does not specify an output directory,
    so if a log_dir is passed into setup logging, this will modify the configuration
    dictionary to emit logs to a specified directory.  Otherwise, they will emit
    in the same directory as sys.argv[0] or sys.executable, depending on whether
    the binary is frozen or not.
    :param log_dir: a directory to emit log files to
    :param configuration: a configuration dictionary read from a logging.yaml file
    :param mkdir: a boolean on whether to create the log directories
    :return: None
    """

    for handler in configuration['handlers'].items():
        if 'file_handler' in handler[0]:
            log_out = pathlib.Path(log_dir) / handler[1]['filename']

            if mkdir:
                log_out.parent.mkdir(parents=True, exist_ok=True)

            handler[1]['filename'] = str(log_out)


def get_all_loggers():
    """Returns all loggers available in a list"""
    return [logging.getLogger(name) for name in logging.root.manager.loggerDict]
