import logging

from log import log
import submodule

# this is a standard method for creating a logging object
LOG = logging.getLogger(__name__)

if __name__ == '__main__':
    # we set up the logging configuration
    # additionally, the logging.yaml has a console handler, so all logs will be emitted to
    # stdout as well as the filehanlders specified
    log.setup_logging('../log/config/logging.yaml', log_dir='./logs')

    # a logging message from the main thread (take note of the first item, should be main.py)
    LOG.info('This is a test log for the main thread')

    # a logging message from the imported thread (the first item should be submodule.py)
    submodule.write_info_log('This is an imported INFO log message.')

    # we can also disable imported logs by name
    submodule_logger = logging.getLogger('submodule')

    # before setting the submodule_logger level, we can that because our global logger
    # is set at INFO, the following won't emit
    submodule.write_debug_log("This won't write anywhere.")

    # but if we set the level of that logger to debug, it will now emit
    submodule_logger.setLevel(logging.DEBUG)
    submodule.write_debug_log('Now this will write out')

    # we can silence all but the most critical warnings like this
    submodule_logger.setLevel(logging.CRITICAL)
    submodule.write_critical_log('Oh no!  Major malfunction.')

    # We can print all logger objects available through all imported modules
    # I've import requests so we can see more loggers
    import requests
    print(log.get_all_loggers())

    # you might notice a my_module logger in there as well -- this is from the log
    # module we import -- if we don't specify a logger name, this defaults to my_module
