import requests
from bs4 import BeautifulSoup
import os

config = {
  'url': 'https://github.com/Alvin9999/new-pac/wiki/ss%E5%85%8D%E8%B4%B9%E8%B4%A6%E5%8F%B7',
  'headers': {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 FS"
  },
  'timeout': 30
}

cry_times = 0

def init():
  global cry_times
  cry_times+=1
  
  res = requests.get(config['url'], headers=config['headers'])
  res.encoding='utf-8'
  print('http status: ', res.status_code)
  if res.status_code != 200 and cry_times < 3:
    print('reinit', cry_times)
    return init()
  
  html = BeautifulSoup(res.text, 'html.parser')
  SSRs = html.find_all('p', text='SSR链接：')[0].find_next_siblings('p', limit=5)
  wirte_file(SSRs)


def wirte_file(SSRs):
  if os.path.exists('./result.txt'):
    os.remove('./result.txt')
    print('delete result.txt ok!')

  str = ''
  for item in SSRs:
    str = str+item.text + '\n'

  with open('./result.txt', 'w', encoding='utf-8') as f:
    f.write(str)

  print('write file ok')

if __name__ == '__main__':
  init()
