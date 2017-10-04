from mail2spreadsheet.conf import Conf
from mail2spreadsheet.spreadsheet import update_row
from argparse import ArgumentParser
import json
import logging


def parse_log_level(level):
    return {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warn': logging.WARN,
        'error': logging.ERROR,
        'fatal': logging.FATAL,
    }[level]


def main():
    parser = ArgumentParser(
        description='''
        Watch GMail emails and forward some of them to a spreadsheet
        ''',
    )
    parser.add_argument(
        '--credentials-file',
        help='''
        The JSON file this application creates after it logs into Google API.
        ''',
    )
    parser.add_argument(
        '--spreadsheet',
        help='''
        The URL of the GoogleSpreadsheet document you want to modify.
        ''',
    )
    parser.add_argument(
        '--secret',
        help='''
        The JSON file you obtained by registering this application as
        described here:
        https://developers.google.com/sheets/api/quickstart/python.
        ''',
    )
    parser.add_argument(
        '--log-level',
        help='''How much info to print''',
        choices=('debug', 'info', 'warn', 'error', 'fatal'),
        default='error',
    )
    parser.add_argument(
        'row',
        help='''
        The JSON containing the row you want to append to the spreadsheet.
        ''',
    )
    cmd = parser.parse_args()
    logging.basicConfig(
        level=parse_log_level(cmd.log_level),
        format='%(levelname)s %(asctime)s %(message)s'
    )
    conf = Conf(cmd)
    columns = json.loads(cmd.row)
    update_row(conf, columns)
