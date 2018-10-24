import sys
from urllib.parse import urlparse
from CMS.test1.script import bak_check
from CMS.test1.lib.core import webcms,PortScan
# reload(sys)
# sys.setdefaultencoding('utf-8')

if __name__ == "__main__":
    ww = PortScan.PortScan()
    ww.work()

    

