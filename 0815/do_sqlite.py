#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始化数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('CREATE TABLE user(id VARCHAR(20) PRIMARY KEY, name VARCHAR(20), score INT)')
cursor.execute(r"INSERT INTO user VALUES('A-001', 'Adam', 95)")
cursor.execute(r"INSERT INTO user VALUES('A-002', 'Bart', 62)")
cursor.execute(r"INSERT INTO user VALUES('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()

def get_score_in(low, high):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('SELECT name FROM user WHERE score BETWEEN ? AND ?', (low, high))
    result = cursor.fetchall()
    names = list(map(lambda x: x[0], result))
    cursor.close()
    conn.close()
    return names
print(get_score_in(80, 95))
print(get_score_in(60, 80))
print(get_score_in(60, 100))
#assert get_score_in(80, 95) == ['Adm'], get_score_in(80, 95)
#assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
#assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)
print('Pass')
