import requests as rq
import sys
import time
import msgtips
import win32api
import win32con


if __name__ == '__main__':
    gui = msgtips.TestTaskbarIcon()
    texts = '#修改host日期\n#宇鱼工作室出品\n'
    time_now = time.strftime("#%c\n", time.localtime())
    texts += time_now
    url = 'https://raw.hellogithub.com/hosts'
    ua = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Appl'
                      'eWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38'
    }
    try:
        host = rq.get(url, headers=ua, timeout=1).text
        host_path = 'C:\\Windows\\System32\\drivers\\etc\\hosts'
        with open(host_path, 'w+', encoding='utf-8') as f:
            f.write(texts+host)
        gui.showMsg(title="提示", msg="更新hosts成功")
        win32api.MessageBox(0, "更新hosts成功", "提示", win32con.MB_ICONASTERISK)
        time.sleep(3)
        gui.CloseGui()
    except rq.exceptions.ConnectTimeout as ConnectTimeout:
        print("Error = {}".format(ConnectTimeout))
        win32api.MessageBox(0, str(ConnectTimeout), "连接超时", win32con.MB_ICONWARNING)
        sys.exit('添加失败')
    except rq.exceptions.ConnectionError as ConnectionError:
        print("Error = {}".format(ConnectionError))
        win32api.MessageBox(0, str(ConnectionError), "连接出错", win32con.MB_ICONWARNING)
        sys.exit('添加失败')
    except Exception as e:
        print("Error = {}".format(e))
        win32api.MessageBox(0, str(e), "未知错误", win32con.MB_ICONWARNING)
        sys.exit('添加失败')
    sys.exit('添加成功，请查看hosts文件')
