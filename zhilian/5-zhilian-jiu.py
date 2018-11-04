'''
Request URL: https://sou.zhaopin.com/jobs/searchresult.ashx?
jl=%E4%B8%8A%E6%B5%B7&kw=python%E5%BC%80%E5%8F%91&sm=0&p=1&isadv=0
Request Method: GET
Request URL: http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%e4%b8%8a%e6%b5%b7&kw=python%e5%bc%80%e5%8f%91&sm=0&isadv=0&sg=d53ea3547af348a9baf1016edda15cdf&p=2
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36
Request URL: http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%e4%b8%8a%e6%b5%b7&kw=python%e5%bc%80%e5%8f%91&sm=0&isadv=0&sg=d53ea3547af348a9baf1016edda15cdf&p=3
jl: 上海
kw: python开发
sm: 0
p: 1
isadv: 0

'''
import urllib.request
import urllib.parse
from fzzl01 import Zhilianjiu

# 爬虫三剑客
get_url = 'https://sou.zhaopin.com/jobs/searchresult.ashx?'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
    'Cookie': 'ZP-ENV-FLAG=gray; dywea=95841923.543481321681999170.1537002568.1537002568.1537002568.1; dywec=95841923; dywez=95841923.1537002568.1.1.dywecsr=baidu|dyweccn=(organic)|dywecmd=organic; LastCity=%E4%B8%8A%E6%B5%B7; LastCity%5Fid=538; adfbid=0; adfbid2=0; sts_deviceid=165dc7dfea1a28-03f46c19d605d2-2711639-2359296-165dc7dfea31046; sts_sg=1; sts_sid=165dc7dfea52c4-0598517bc859fc-2711639-2359296-165dc7dfea6606; zp_src_url=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DObkRpNMLgu4GwG3XsFUoKQIYob95pBZb1fCDpH-t-EQv91WCvGgzMZ_-PDxG8z1y%26wd%3D%26eqid%3D804246e80001d5e7000000025b9ccc3d; __utma=269921210.1479507425.1537002570.1537002570.1537002570.1; __utmc=269921210; __utmz=269921210.1537002570.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ZP-ENV-FLAG=gray; GUID=c94d2624d1184f2ba5214e4e4f558942; ZL_REPORT_GLOBAL={%22sou%22:{%22actionid%22:%22344ee144-2c1b-4b3d-b892-decb3cbad08e-sou%22%2C%22funczone%22:%22smart_matching%22}}; Hm_lvt_d838d7d6abb840b6c1a339ec5aee915d=1537002573; Hm_lpvt_d838d7d6abb840b6c1a339ec5aee915d=1537002573; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1537002573; ZP_OLD_FLAG=true; _jzqa=1.556436521441183700.1537002577.1537002577.1537002577.1; _jzqc=1; _jzqx=1.1537002577.1537002577.1.jzqsr=sou%2Ezhaopin%2Ecom|jzqct=/.-; _jzqckmp=1; _qzjc=1; JSSearchModel=0; BLACKSTRIP=yes; sts_evtseq=4; LastJobTag=%e4%ba%94%e9%99%a9%e4%b8%80%e9%87%91%7c%e5%b8%a6%e8%96%aa%e5%b9%b4%e5%81%87%7c%e8%8a%82%e6%97%a5%e7%a6%8f%e5%88%a9%7c%e7%bb%a9%e6%95%88%e5%a5%96%e9%87%91%7c%e5%ae%9a%e6%9c%9f%e4%bd%93%e6%a3%80%7c%e5%91%a8%e6%9c%ab%e5%8f%8c%e4%bc%91%7c%e5%91%98%e5%b7%a5%e6%97%85%e6%b8%b8%7c%e9%a4%90%e8%a1%a5%7c%e5%b9%b4%e5%ba%95%e5%8f%8c%e8%96%aa%7c%e5%bc%b9%e6%80%a7%e5%b7%a5%e4%bd%9c%7c%e4%ba%a4%e9%80%9a%e8%a1%a5%e5%8a%a9%7c%e8%a1%a5%e5%85%85%e5%8c%bb%e7%96%97%e4%bf%9d%e9%99%a9%7c%e9%80%9a%e8%ae%af%e8%a1%a5%e8%b4%b4%7c%e5%8a%a0%e7%8f%ad%e8%a1%a5%e5%8a%a9%7c%e6%af%8f%e5%b9%b4%e5%a4%9a%e6%ac%a1%e8%b0%83%e8%96%aa%7c%e5%85%8d%e8%b4%b9%e7%8f%ad%e8%bd%a6%7c%e5%85%a8%e5%8b%a4%e5%a5%96%7c%e5%88%9b%e4%b8%9a%e5%85%ac%e5%8f%b8%7c%e5%b9%b4%e7%bb%88%e5%88%86%e7%ba%a2%7c%e8%82%a1%e7%a5%a8%e6%9c%9f%e6%9d%83%7c%e5%8c%85%e5%90%83%7c%e9%ab%98%e6%b8%a9%e8%a1%a5%e8%b4%b4%7c14%e8%96%aa%7c%e5%8c%85%e4%bd%8f%7c%e5%81%a5%e8%ba%ab%e4%bf%b1%e4%b9%90%e9%83%a8%7c%e4%b8%8d%e5%8a%a0%e7%8f%ad%7c%e6%88%bf%e8%a1%a5%7c%e4%bd%8f%e6%88%bf%e8%a1%a5%e8%b4%b4%7c%e6%97%a0%e8%af%95%e7%94%a8%e6%9c%9f%7c%e9%87%87%e6%9a%96%e8%a1%a5%e8%b4%b4%7c%e5%85%8d%e6%81%af%e6%88%bf%e8%b4%b7; urlfrom=121126445; urlfrom2=121126445; adfcid=none; adfcid2=none; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1537003267; LastSearchHistory=%7b%22Id%22%3a%2238be9624-c848-41c6-b179-20fb02af2134%22%2c%22Name%22%3a%22python%e5%bc%80%e5%8f%91+%2b+%e4%b8%8a%e6%b5%b7%22%2c%22SearchUrl%22%3a%22http%3a%2f%2fsou.zhaopin.com%2fjobs%2fsearchresult.ashx%3fjl%3d%25e4%25b8%258a%25e6%25b5%25b7%26kw%3dpython%25e5%25bc%2580%25e5%258f%2591%26sm%3d0%26isadv%3d0%26sg%3dd53ea3547af348a9baf1016edda15cdf%26p%3d3%22%2c%22SaveTime%22%3a%22%5c%2fDate(1537003622131%2b0800)%5c%2f%22%7d; _qzja=1.63410539.1537002577229.1537002577229.1537002577229.1537003561341.1537003623869.0.0.0.9.1; _qzjb=1.1537002577229.9.0.0.0; _qzjto=9.1.0; _jzqb=1.9.10.1537002577.1; dyweb=95841923.27.9.1537003913274; __utmb=269921210.25.9.1537003913276'

}
data = {
    "jl": "上海",
    "kw": "python爬虫",
    "sm": "0",
    "p": "1",
    "isadv": "0",
}
# jl=%E4%B8%8A%E6%B5%B7&kw=python%E5%BC%80%E5%8F%91&sm=0&p=1&isadv=0
data = urllib.parse.urlencode(data)
url = get_url + data
# 定制请求
request = urllib.request.Request(url=url, headers=headers)
# 响应请求
response = urllib.request.urlopen(request)
# 响应内容
content = response.read().decode('utf-8')
# print(content)
# 解析数据content,定位节点
# 导入bs4 库
from bs4 import BeautifulSoup

# 创建bs4 对象
soup = BeautifulSoup(content, 'lxml')
# 先找xpath 路径
'//div[@id="newlist_list_content_table"]/table/tbody/tr/td/div/a'
# 把xpath 路径改为bs4形式
table_list = soup.select("#newlist_list_content_table > table")
# print(table_list)
# 遍历table_list 返回table 标签对象
lzh_1 = []
for table in table_list[1:]:
    # print(table)
    # 再次节点定位/table/tbody/tr/td/div/a'
    # //td[@class="zwmc"]/div/a/get.text
    zwmc = table.select(".zwmc > div > a")[0].get_text()
    zwyx = table.select(".zwyx")[0].get_text()
    gzdd = table.select(".gzdd")[0].get_text()
    gsmc= table.select(".gsmc")[0].get_text()

    # print(a_list)
# print(zwmc)
# print(zwyx)
# print(gzdd)
# print(gsmc)
#     封装类,实例化对象,并添加到列表
    zljiu = Zhilianjiu(zwmc,zwyx,gzdd,gsmc)
    lzh_1.append(zljiu.__dict__)
# print(lzh_1)

# 保存

with open('zl_jiu.json','w',encoding='utf-8') as fp:
    fp.write(str(lzh_1))
