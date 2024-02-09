""" connector.py"""

from connectors.core.connector import Connector
from connectors.core.connector import get_logger, ConnectorError
from . import operations

logger = get_logger('text-utility')

def get_available_operations(operations, operation):
    '''returns the function object defined by operation str'''
    for func in filter(callable, operations.__dict__.values()):
        if operation in func.__qualname__:
            return func

class TextUtility(Connector):
    def execute(self, config, operation, params, **kwargs):
        try:
            params.update({'operation': operation})
            action = get_available_operations(operations, operation)
            return action(config, params)
        except Exception as Err:
            raise ConnectorError(Err)

    def check_health(self, config):
        try:
            from sentence_transformers import SentenceTransformer
        except Exception as Err:
            logger.error('Required import failed: [{0}]'.format(Err))
            raise ConnectorError(Err)
