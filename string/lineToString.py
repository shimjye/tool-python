#-*- coding: utf-8 -*-
from convert_case import *

prestr = """
"""
endstr = """
"""

paramString = """
test doc
"""

# main
if __name__ == "__main__":
    param = paramString.split('\n')
    # type, colName, format, comment
    # query = '\t\t\treturnVO.set{0}(resultSet.getString("{1}"));'
    query = '\t\tsql.append(", {0}\\n");'

    print(prestr)
    for item in param:
        if not item:
            continue
        item_split = item.strip().split(' ')
        var1 = to_camel_case(item_split[0])
        var2 = ' '.join(item_split[1:])
        print(query.format(item_split[0]))
    print(endstr)
