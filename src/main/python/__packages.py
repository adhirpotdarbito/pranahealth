'''
   
    Copyright (C) 2018-2019 AtmanCare India Private Limited
    
    This source code is owned and maintained by AtmanCare India Private Limited
    and not allowed to be used or to be distributed without prior written
    permission of AtmanCare India Private Limited.
   
'''

import sys

package_list = []
pkg_list_diact = {}

def prepare_pkgs_list(db,lid):
    cursor = db.cursor()
    try:
        query_str = "select packages from lifestyle_pkg_map where lifestyle=%d" %lid
        cursor.execute(query_str)
    except Exception as err:
        print (Exception, err)
        cursor.close()
        return -1

    l_pkg_map = cursor.fetchone()
    while l_pkg_map is not None:
        packages = l_pkg_map[0]
        cursor_in = db.cursor()
        try:
            query_str = "select name, description from preventive_pkg where id=%d" %packages
            cursor_in.execute(query_str)
        except Exception as err:
            print (Exception, err)
            cursor_in.close()
            cursor.close()
            return -1
        pkg_details = cursor_in.fetchone()
        pkg_name = pkg_details[0]
        pkg_desc = pkg_details[1]

        if pkg_name not in package_list:
            package_list.append(pkg_name)
            pkg_list_diact[pkg_name] = pkg_desc

        cursor_in.close()
        l_pkg_map = cursor.fetchone()

    cursor.close()
    return 0

def get_count_pkgs():
    return len(package_list)

def get_pkg_name_by_pos(pos):
    return package_list[pos]

def get_pkg_desc(pkg):
    return pkg_list_diact[pkg]
