import logging
from os import path
from oauth2client.service_account import ServiceAccountCredentials
from configparser import SafeConfigParser



class Conf(object):

    scope = ['https://spreadsheets.google.com/feeds']

    def __init__(self, cmd, credentials_file=None, spreadsheet=None):
        self.credentials = None
        self.credentials_file = None
        self.spreadsheet = None

        self._cmd = cmd
        self._parser = None
        self._logger = logging.getLogger(__name__)

        if credentials_file:
            self.credentials_file = credentials_file
        self.try_parse_credentials()
        if spreadsheet:
            self.spreadsheet = spreadsheet
        else:
            self.try_parse_spreadsheet()

    def try_parse_credentials(self):
        if not self.credentials_file:
            self.credentials_from_cmd()
        if not self.credentials_file:
            self.credentials_from_ini()
        self._logger.info(
            'Loading credentials from: "%s"' % self.credentials_file,
        )
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(
            self.credentials_file, self.scope,
        )

    def try_parse_spreadsheet(self):
        if not self.spreadsheet:
            self.spreadsheet_from_cmd()
        if not self.spreadsheet:
            self.spreadsheet_from_ini()

    def credentials_from_cmd(self):
        self.credentials_file = self._cmd.credentials_file

    def spreadsheet_from_cmd(self):
        self.spreadsheet = self._cmd.spreadsheet

    def get_parser(self):
        if not self._parser:
            self._parser = SafeConfigParser()
            config_ini = path.join(path.dirname(__file__), 'etc/config.ini')
            self._logger.info('Loading configuration from: "%s"' % config_ini)
            self._parser.read(config_ini)
        return self._parser

    def credentials_from_ini(self):
        etc = path.join(path.dirname(__file__), 'etc')
        self.credentials_file = path.join(
            etc,
            self.get_parser()['spreadsheet']['credentials_file'],
        )

    def spreadsheet_from_ini(self):
        self.spreadsheet = self.get_parser()['spreadsheet']['spreadsheet']
