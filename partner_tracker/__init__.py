def setup_logging(filename):
    import sys
    import json
    import logging.config

    try:
        with open(filename) as file:
            logging.config.dictConfig(json.load(file))

    except FileNotFoundError:
        print('WARNING: file %s not found, using default logging settings' % filename, file=sys.stderr)
