#-*- coding: utf-8 -*-
from convert_case import *

'''
param = [
"  `nickname` varchar(500) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '닉네임'",
"  `last_login_dt` datetime DEFAULT NULL COMMENT '마지막 로그인 일시'",
"  `birth_date` date DEFAULT NULL COMMENT '생년월일 yyyy-mm-dd'",
"  `gender` int(10) NOT NULL DEFAULT '0' COMMENT '성별 0미지정, 1남, 2여'",
]
paramString = """
  `nickname` varchar(500) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '닉네임',
  `last_login_dt` datetime DEFAULT NULL COMMENT '마지막 로그인 일시',
  `birth_date` date DEFAULT NULL COMMENT '생년월일 yyyy-mm-dd',
  `gender` int(10) NOT NULL DEFAULT '0' COMMENT '성별 0미지정, 1남, 2여',
'''

prestr = """//	$docdo-ss={"id":"com.sootnoon.goose.GooseBeanModel"}
//	{
//		"projectName": "goose",
//		"packageName": "com.sootnoon.goose.api.latest.",
//		"className": "",
//		"types": ["""
endstr = """//		]
//	}
//	$docdo-se
//	$docdo-sg
"""

paramString = """
"""

def getMysqlType(str):
    if(str.find('int') != -1):
        return 'Integer'
    elif(str.find('double') != -1):
        return 'Double'
    elif(str.find('varchar') != -1):
        return 'String'
    elif(str.find('date') != -1):
        return 'Date'

def getMysqlFormat(str):
    if(str.find('datetime') != -1):
        return 'yyyy-MM-dd HH:mm:ss'
    elif(str.find('timestamp') != -1):
        return 'yyyy-MM-dd HH:mm:ss'
    elif(str.find('date') != -1):
        return 'yyyy-MM-dd'
    return ''


# main
if __name__ == "__main__":
    param = paramString.split('\n')
    # row, type, colName, format, comment
    query = '//\t\t\t{{"type": "{0}", "name": "{1}", "format": "{2}", "desc": "{3}"}},'

    print(prestr)
    for item in param:
        if not item:
            continue
        item_split = item.strip().replace('`', '').replace("'", "").split(' ')
        type_name = getMysqlType(item_split[1])
        variable_name = to_camel_case(item_split[0])
        format_value = getMysqlFormat(item_split[1])
        comment = ' '.join(item_split[1:])
        print(query.format(type_name, variable_name, format_value, comment))
    print(endstr)
