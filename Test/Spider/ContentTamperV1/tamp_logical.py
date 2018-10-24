# encoding: utf-8

"""
网页篡改
只针对主页进行分析
"""

import difflib
import uuid
from datetime import datetime
import re
import time
from collections import namedtuple


def get_id():
    return str(uuid.uuid4())


def compare_html(original_source, modified_source, flag_md5, original_md5, modified_md5, target_id, start_url):

    cmpResult = namedtuple(
        'cmpResult', 'modify date lenbef lenaft md5Before md5After contentBefore contentAfter startLineNo')
    try:
        original_format = original_source.splitlines()
        modified_format = modified_source.splitlines()
    except Exception as e:
        print(e)
        try:
            original_format = original_source.encode('utf-8').decode('utf-8').splitlines()
            modified_format = modified_source.encode('ut f-8').decode('utf-8').splitlines()
        except Exception as e2:
            print(e2)
            original_format = original_source.encode('gbk').decode('gbk').splitlines()
            modified_format = modified_source.encode('gbk').decode('gbk').splitlines()

    if not flag_md5:
        diff_result = ''
        for _ in difflib.unified_diff(original_format, modified_format, n=0):
            diff_result += _ + '\n'

        # @@ -3 +3 @@
        start_lines = re.findall('@@ -(\d+)', diff_result, re.M)
        after_line_no = re.findall(' \+(\d+)', diff_result, re.M)
        hunks = re.split('@@.*?@@\n', diff_result, flags=re.M)[1::]
        original_content = ''
        modified_content = ''
        for i in range(len(start_lines)):
            startLineNo = start_lines[i]
            afterLineNo = after_line_no[i]
            hunk_line = hunks[i].splitlines(True)
            original_line = ''
            modified_line = ''
            for line in hunk_line:

                if line == '\n':
                    continue

                line = line.strip(' ')

                # 判断点击数
                cpm_rst = judge_unnecessary_tamper(line)
                if cpm_rst:
                    continue

                # -是修改前的，+是修改后的
                if line[0] == '+':
                    original_line += line
                    original_line = format_source(original_line)
                    original_line += '\n'

                elif line[0] == '-':
                    modified_line += line + '\n'
                    modified_line = format_source(modified_line)
                    modified_line += '\n'
            # 输出到数据库，与前端约定用\n换行
            if original_line or modified_line != '':
                original_content += u'变更前行号:' + startLineNo + '  ' + original_line
                modified_content += u'变更后行号:' + afterLineNo + '  ' + modified_line
        original_content = original_content.strip(' ').replace('  ', '')
        modified_content = modified_content.strip(' ').replace('  ', '')

        cpm_line_no = ','.join(start_lines)
        result = cmpResult(True, datetime.now(), len(original_source), len(modified_source), original_md5,
                           modified_md5, original_content.encode('utf-8'), modified_content.encode('utf-8'),
                           cpm_line_no)

        insert_time = time.time()
        event_id = get_id()
        save_to_mysql(target_id, start_url, result, insert_time, event_id)

        return result

    else:
        pass


# 主函数
def content_tamper_main(target_id: str):
    """
    主函数
    篡改默认三十分钟监测一次，其他模块默认一天一次，所以篡改另建一个爬虫存储表，专门爬取首页内容并检测
    :param target_id:
    """
    try:
        start_url = find_original_home_page(target_id)
        print(start_url)

        # 根据传入的target_id从数据库获取网页源码
        original_html_source = find_original_html_source(target_id)
        # print(before_target_source)

        modified_source = find_modified_html_source(target_id)
        # print(after_target_source)

        modified_md5 = find_modified_md5_by_url(start_url)

        # 根据第二次爬取的网页地址查找对应md5
        original_md5 = find_original_md5_by_url(start_url)

        flag_md5 = False
        data_update(original_md5, modified_md5)

        compare_html(original_html_source, modified_source, flag_md5, original_md5, modified_md5, target_id, start_url)

    except Exception as e:
        print(e)
