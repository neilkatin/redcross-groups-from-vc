
# update.py -- add a list of emails to a specified microsoft graph group

import logging
from logging.config import dictConfig

import os
import dotenv
import msal

def main():
    log.info("running...")

    load_dotenv(verbose=True)

    app = login()
    log.info("done...")

def login():

    app = msal.ConfidentialClientApplication(
            "a68be7b3-5e75-40fb-a25b-925ece2803df",
            authority="https://login.microsoftonline.com/specsnet.onmicrosoft.com")

    accounts = app.get_accounts()
    if accounts:

        for a in accounts:
            log.info(r"found account { a['username']) }")
    else:
        log.error("no accounts found")

    return app


def init_logging(app_name):
    logging_config = {
        'version': 1,
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'default',
                'level': 'DEBUG',
                'stream': 'ext://sys.stderr'
            },
            #'wsgi': {
            #    'class': 'logging.StreamHandler',
            #    'formatter': 'default',
            #    'level': 'DEBUG',
            #    'stream': 'ext://flask.logging.wsgi_errors_stream'
            #},
        },
        'formatters': {
            'default': {
                'format': '%(asctime)s %(levelname)-5s %(name)-10s %(funcName)-.15s:%(lineno)d %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S',
            },
        },
        'root': {
            'level': 'DEBUG',
            #'handlers': [ 'console', 'wsgi' ],
            'handlers': [ 'console' ],
            #'handlers': [ 'wsgi' ],
        },
        'loggers': {
            'urllib3': {
                'level': 'INFO',
            },
            'selenium': {
                'level': 'INFO',
            },
        },
    }

    logging.config.dictConfig(logging_config)
    log = logging.getLogger(app_name)
    return log


if __name__ == "__main__":
    log = init_logging(__name__)
    main()

