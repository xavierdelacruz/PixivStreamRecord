import urllib3
from bs4 import BeautifulSoup
import json
import sys,os,signal
import time

def getStreamUrl(id):
    http = urllib3.PoolManager()
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    # user1 tkh_c
    # user2 sakusyo-art
    # user3 katze_horenso
    url = 'https://sketch.pixiv.net/@%s/lives/' %id
    r = http.request('GET', url)
    soup = BeautifulSoup(r.data.decode('utf-8'), "lxml")
    x = soup.find(id='state').string
    x = x[x.find('=') + 1:]
    x = x.split('\n')[0].rstrip(';').replace('undefined', 'null')
    y = json.loads(x)['dehydrated']
    # find liveId
    params = y['context']['dispatcher']['stores']['RouteStore']['navigation']['params']
    if 'live_id' in params:
        live_id = params['live_id']
        m3u8Url = y['context']['dispatcher']['stores']['LiveStore']['lives'][live_id]['owner']['hls_movie']
        return m3u8Url,live_id
    else:
        return False,False

def getHighResUrl(id):
    baseUrl,live_id = getStreamUrl(id)
    # This is a huge mess lolololol
    if baseUrl:
        http = urllib3.PoolManager()
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        resCode = http.request('GET', baseUrl)
        if resCode.status == 200:
            return baseUrl, live_id
        else:
            return False,False
    else:
        return False,False

if __name__ == "__main__":
    userid = sys.argv[1]
    sleep_seconds = int(sys.argv[2])
    dateTime = time.strftime('%y%m%d%H%M',time.localtime(time.time()))
    highResUrl, live_id = getHighResUrl(userid)

    filenum = 0
    while(1):
        highResUrl = None
        live_id = None
        while not live_id:
            highResUrl, live_id = getHighResUrl(userid)
            if live_id:
                break
            print(f'Live has not started, sleeping for {sleep_seconds} seconds')
            time.sleep(sleep_seconds)
        filenum += 1
        print('URL = %s , live_id = %s'%(highResUrl,live_id))
        fileName = 'PixivStream-%s-%s-%s-%s' %(userid,dateTime,live_id,filenum)
        print('logFileName = %s.log , streamFileName = %s.mkv'%(fileName,fileName))
        processInfo = os.popen('ps -ef |grep %s |grep -v grep'%live_id).readlines()
        processNum = len(processInfo)
        print('processNum = %s'%processNum)
        if processNum==0:
            target_dir = 'output/'
            if not os.path.exists('output/'):
                os.mkdir(target_dir)
            os.system(f'nohup /usr/bin/ffmpeg -i {highResUrl} -c copy {target_dir}{fileName}.mkv >{target_dir}{fileName}.log 2>&1 &')
            print('Stream start Recording')
            while(1):
                time.sleep(60)
                http = urllib3.PoolManager()
                urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
                resCode = http.request('GET', highResUrl)
                if resCode.status == 200:
                    print('resCode = %s , Stream is still alive from %s'%(resCode.status,userid))
                    continue
                else:
                    processPids = os.popen("ps -ef |grep %s |grep -v grep|awk '{print $2}'" %live_id).readlines()
                    for pid in processPids:
                        print('pid = %s , Stream record is dead' %pid)
                        os.kill(int(pid),signal.SIGKILL)
                    break
        else:
            print('Stream is Recording')