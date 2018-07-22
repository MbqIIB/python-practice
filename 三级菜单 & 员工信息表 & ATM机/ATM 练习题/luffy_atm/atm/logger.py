#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/7/22 下午1:00
# @Author  : littlelinghome
# @Site    : 
# @File    : logger.py
# @Software: PyCharm

import logging,os
from conf import settings


def logger(log_type):
    logger = logging.getLogger(log_type)
    logger.setLevel(settings.LOG_LEVEL)
    log_file = os.path.join(settings.LOG_PATH,settings.LOG_TYPES[log_type])
    fh = logging.FileHandler(log_file)
    fh.setLevel(settings.LOG_LEVEL)
    formatter = settings.LOG_FORMAT

    fh.setFormatter(formatter)

    logger.addHandler(fh)

    return logger