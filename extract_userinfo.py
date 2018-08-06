# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 19:49:54 2018

@author: TingC
"""
import re


def extract_man(soup):
    data = dict()
    data['name'] = soup.find('div',{'class':'name'}).text.split()[0]

    a,b = soup.find('div',{'class':'manPic'}).dl.find_all('dt')[-1].text.split('：')
    data[a] = b
    
    divs = soup.find_all('div',{'class':'inter'})
    label = soup.find('div',{'class':'inter label'})
    if label:
        divs.pop(divs.index(label))
        #data['sex'] = 
        data['tags'] = '/'.join([i.text for i in label.find_all('span')])
    
    #data['id'] = 
    splits = [i for i in re.findall('>(.*?)<', str(divs[-1])) if i != '/']
    # splits = [i.strip() for i in soup.find('div',{'class':'inter'}).text.split('/')]
    data['age'], data['height'], data['education'], data['area'] = splits[:4]
    
    # 是否有照片
    div = soup.find('div',{'class':'manPic'}).find('div',{'class':'noPic'})
    if div:
        data['picture'] = '无'
    else:
        data['picture'] = '有'
        
    # 恋爱状态
    div = soup.find('div',{'class':'womanPic'})
    if not div:
        div = soup.find('div',{'class':'manPic'})
    if div.em:
        data['status'] = div.em.text
    else:
        data['status'] = ''
    
    # 爬取表格
    for infor in ['data', 'perData']:
        div = soup.find('div',{'class': infor})
        dt = div.find_all('dt')
        dd = [d for d in div.find_all('dd') if not d.get('style')]
        for i in range(len(dt)):
            key = re.sub('\s+','',dt[i].text[:-1])
            value = re.sub('\s+','',dd[i].text.strip())
            if key in data and value != data[key]:
                if key == '有无子女':
                    data['择偶要求_有无子女'] = value
                elif key == '相貌自评':
                    continue
                else:
                    raise Exception('这个键有问题 %s %s %s' % (key, value, data[key]))
            else:
                data[key] = value
    data['intro'] = re.sub('\s+','',soup.find('div',{'class':'intr'}).text.strip())
    if '择偶要求_有无子女' not in data:
        data['择偶要求_有无子女'] = data['有无子女']
    if '登录后可见' in data.values():
        raise Exception('登陆问题')
    return data


def extract_woman(soup):
    data = dict()
    data['name'] = soup.find('div',{'class':'name'}).text.split()[0]
       
    a,b = soup.find('div',{'class':'data'}).find_all('dt')[-1].text.split('：')
    data[a] = b
    
    divs = soup.find_all('div',{'class':'inter'})
    label = soup.find('div',{'class':'inter label'})
    if label:
        divs.pop(divs.index(label))
        #data['sex'] = 
        data['tags'] = '/'.join([i.text for i in label.find_all('span')])
    
    #data['id'] = 
    splits = [i for i in re.findall('>(.*?)<', str(divs[-1])) if i != '/']
    # splits = [i.strip() for i in soup.find('div',{'class':'inter'}).text.split('/')]
    data['age'], data['height'], data['education'], data['area'] = splits[:4]
    
    # 是否有照片
    div = soup.find('div',{'class':'womanPic'}).find('div',{'class':'noPic'})
    if div:
        data['picture'] = '无'
    else:
        data['picture'] = '有'
        
    # 恋爱状态
    div = soup.find('div',{'class':'womanPic'})
    if not div:
        div = soup.find('div',{'class':'manPic'})
    if div.em:
        data['status'] = div.em.text
    else:
        data['status'] = ''
    
    # 爬取表格
    infor = 'perData'
    div = soup.find('div',{'class': infor})
    dt = div.find_all('dt')
    dd = [d for d in div.find_all('dd') if not d.get('style')]
    for i in range(len(dt)):
        key = re.sub('\s+','',dt[i].text[:-1])
        value = re.sub('\s+','',dd[i].text.strip())
        if key in data and value != data[key]:
            if key == '有无子女':
                data['择偶要求_有无子女'] = value
            elif key == '相貌自评':
                continue
            else:
                raise Exception('这个键有问题 %s %s %s' % (key, value, data[key]))
        else:
            data[key] = value
    data['intro'] = re.sub('\s+','',soup.find('div',{'class':'intr'}).text.strip())
    
    if '择偶要求_有无子女' not in data:
        data['择偶要求_有无子女'] = data['有无子女']
    if '登录后可见' in data.values():
        raise Exception('登陆问题')
    return data