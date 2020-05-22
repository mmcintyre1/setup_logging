import logging

LOG = logging.getLogger(__name__)


def write_info_log(msg):
    LOG.info(msg)


def write_debug_log(msg):
    LOG.debug(msg)


def write_critical_log(msg):
    LOG.critical(msg)

