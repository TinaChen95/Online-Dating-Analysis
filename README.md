# Online-Dating-Analysis
IS HE/SHE YOUR SOULMAT? - An analysis of Online Dating in China based on www.baihe.com

他/她是最适合你的吗？ — 基于百合网的中国在线婚恋情况分析


## 商业背景
* 根据《中国统计年鉴》，15岁以上的单身人口已达到2.51亿人
* 同时，离婚率的不断上升也使得单身人群占比增加
* 婚恋市场潜力巨大！
![Image text](https://github.com/TinaChen95/Online-Dating-Analysis/img/图片1.png)
### 在线婚恋市场的机遇
艾瑞咨询公司的一份报告证实，婚姻和爱情市场的规模稳步增长，2018将超过100亿元
![Image text](https://github.com/TinaChen95/Online-Dating-Analysis/img/图片2.png)
### 在线婚恋市场的挑战
截止2016年底，中国超过10万用户的成熟在线交友网站的数量，已经超过20个
![Image text](https://github.com/TinaChen95/Online-Dating-Analysis/img/图片3.png)

## 数据来源与获取
百合网 （http://www.baihe.com/ ）是中国第一家通过网上实名进行交友和婚恋的服务商，已有超过9000万注册用户，在全国100个城市开设了实体店
根据百合网年报显示，百合网2015年营业收入达到1.85亿元。

基于Python的数据爬虫
* Requests获取页面 + BeautifulSoup解析页面
* 使用Cookies模拟登陆

### 数据分析模块
* 在线婚恋现状分析  
 基于百合网数据，对婚恋现状进行基础统计分析。如针对相恋时间、用户年龄的分析
 
* 约会模式分析  
 基于百合网数据，对情侣的组合分析。例如对星座组合、性格组合等的分析

### 机器学习应用
* 基于Kmeans模型的辅助用户建模与初步匹配
* 基于Logistic回归的结婚指数预测
