#-*- coding: utf-8 -*-
from convert_case import *

'''
Simple create-sql to docdo-source-string.
Work with python 3.x.
'''

prestr = """//	$docdo-ss={"id":"com.sootnoon.docdo.DocdoBeanModel"}
//	{
//		"projectName": "docdo",
//		"packageName": "com.sootnoon.docdo.api.latest.",
//		"className": "DocdoBean",
//		"types": ["""
endstr = """//		]
//	}
//	$docdo-se
//	$docdo-sg
"""

paramString = """
  `nickname` varchar(500) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'nickname',
  `last_login_dt` datetime DEFAULT NULL COMMENT 'last_login_dt',
  `birth_date` date DEFAULT NULL COMMENT 'birth_date yyyy-mm-dd',
  `gender` int(10) NOT NULL DEFAULT '0' COMMENT 'gender 0:defalut, 1:man, 2:woman',
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
    # type, colName, format, comment
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
