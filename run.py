import requests
from bs4 import BeautifulSoup
import os

config = {
  'url': 'https://github.com/Alvin9999/new-pac/wiki/ss%E5%85%8D%E8%B4%B9%E8%B4%A6%E5%8F%B7',
  'url2': 'https://github.com/Alvin9999/new-pac/wiki/v2ray%E5%85%8D%E8%B4%B9%E8%B4%A6%E5%8F%B7',
  'headers': {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 FS"
  },
  'timeout': 30
}

cry_times=0
def get_SSR():
  global cry_times
  cry_times+=1
  
  res = requests.get(config['url'], headers=config['headers'])
  res.encoding = 'utf-8'
  print('get SSR http status: ', res.status_code)
  if res.status_code != 200 and cry_times < 3:
    print('reinit SSR:', cry_times)
    return get_SSR()
  
  html=BeautifulSoup(res.text, 'html.parser')
  SSRs=html.find(string='SSR链接：').parent.parent

  str=''
  for item in SSRs.next_siblings:
    if 'ssr://' in item.text or 'ss://' in item.text:
      str+=item.text+'\n'
    else:
      continue
  return str


vmess_time=0
def get_vmess():
  global vmess_time
  vmess_time+=1
  vmess=''
  res=requests.get(config['url2'], headers=config['headers'])
  res.encoding='utf-8'
  print('get vmess http status: ', res.status_code)
  if res.status_code != 200 and vmess_time < 3:
    print('reinit vmess: ', vmess_time)
    return get_vmess()

  html=BeautifulSoup(res.text, 'html.parser')
  start=html.find(string='现在客户端很多都支持URL直接导入vmess链接，复制粘贴即可。').parent
  for item in start.next_siblings:
    if '果想搭建自己的v2ray节点' in item.text:
      break
    vmess+=item.text+'\n'
  return vmess

def wirte_file(str):
  if os.path.exists('./result.txt'):
    os.remove('./result.txt')
    print('delete result.txt ok!')

  with open('./result.txt', 'w', encoding='utf-8') as f:
    f.write(str)

  print('write file ok')

if __name__ == '__main__':
  ssr = get_SSR()
  vmess = get_vmess()
  wirte_file(ssr + vmess)
