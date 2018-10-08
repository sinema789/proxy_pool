from .utils import get_page
from pyquery import PyQuery as Pq
from lxml import etree
import re


class ProxyMetaclass(type):

    def __new__(mcs, name, bases, attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k, v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(mcs, name, bases, attrs)


class Crawler(object, metaclass=ProxyMetaclass):

    def get_proxies(self, callback):
        proxies = []
        for proxy in eval("self.{}()".format(callback)):
            print('成功获取到代理', proxy)
            proxies.append(proxy)
        return proxies

    def crawl_data5u(self):
        """
        获取无忧代理
        :return: 代理
        """
        for i in ['gngn', 'gnpt']:
            start_url = 'http://www.data5u.com/free/{}/index.shtml'.format(i)
            html = get_page(start_url)
            ip_address = re.compile(
                ' <ul class="l2">\s*<span><li>(.*?)</li></span>\s*'
                '<span style="width: 100px;"><li class=".*">(.*?)</li></span>')
            # \s * 匹配空格，起到换行作用
            re_ip_address = ip_address.findall(html)
            for address, port in re_ip_address:
                result = address + ':' + port
                yield result.replace(' ', '')

    def crawl_daili66(self, page_count=4):
        """
        获取代理66
        :param page_count: 页码
        :return: 代理
        """
        start_url = 'http://www.66ip.cn/{}.html'
        urls = [start_url.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            print('Crawling', url)
            html = get_page(url)
            if html:
                doc = Pq(html)
                trs = doc('.containerbox table tr:gt(0)').items()
                for tr in trs:
                    ip = tr.find('td:nth-child(1)').text()
                    port = tr.find('td:nth-child(2)').text()
                    yield ':'.join([ip, port])

    def crawl_xici(self, page_count=4):
        """
        获取西刺代理
        :param page_count: 页码
        :return: 代理
        """
        start_url = 'http://www.xicidaili.com/nn/{}.html'
        urls = [start_url.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            print('Crawling', url)
            html = get_page(url)
            eroot = etree.HTML(html)

            ip_addresses = eroot.xpath('//table[@id="ip_list"]/tr[position()>1]/td[2]/text()')
            ports = eroot.xpath('//table[@id="ip_list"]/tr[position()>1]/td[3]/text()')
            for i in zip(ip_addresses, ports):
                ip_address = i[0] + ':' + i[1]
                yield ip_address
