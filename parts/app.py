import logging
from cheroot.wsgi import Server as WSGIServer, PathInfoDispatcher
from cheroot.ssl.builtin import BuiltinSSLAdapter
from services import run_app as run_parts_management_app

PARTS_MANAGEMENT = run_parts_management_app()
DISPATCHER = PathInfoDispatcher([('/parts', PARTS_MANAGEMENT)])


PORT = 8040
SERVER = WSGIServer(('0.0.0.0', PORT), DISPATCHER)

if __name__ == '__main__':
    logging.basicConfig(format='', level=logging.INFO)
    logging.info('Running server on port %s', PORT)
    SERVER.safe_start()
