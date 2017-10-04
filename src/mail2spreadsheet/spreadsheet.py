# https://docs.google.com/spreadsheets/d/1Sa7f9t-mS9-O-P6C5XUlg_Ii7Ei1JrMmX0erf63xMBo/edit#gid=0
import logging
import gspread

from collections import OrderedDict

template = OrderedDict([
    ("hex"       , ""),
    ("squawk"    , ""),
    ("flight"    , ""),
    ("lat"       , ""),
    ("lon"       , ""),
    ("nucp"      , ""),
    ("seen_pos"  , ""),
    ("altitude"  , ""),
    ("vert_rate" , ""),
    ("track"     , ""),
    ("speed"     , ""),
    ("category"  , ""),
    ("mlat"      , ""),
    ("tisb"      , ""),
    ("messages"  , ""),
    ("seen"      , ""),
    ("rssi"      , ""),
])


def update_row(conf, columns):
    gc = gspread.authorize(conf.credentials)
    logging.info('Loading spreadsheet: "%s"' % conf.spreadsheet)
    sh = gc.open(conf.spreadsheet)
    worksheet = sh.get_worksheet(0)
    values = [columns[k] for k in template.keys()]
    logging.info('Inserting values: %s' % values)
    worksheet.append_row(values)
