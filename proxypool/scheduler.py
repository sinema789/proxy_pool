import time
from multiprocessing import Process
from .setting import *
from .api import app
from .getter import Getter
from .tester import Tester


class Scheduler(object):

    def scheduler_tester(self, cycle=TESTER_CYCLE):
        """
        定时测试代理
        :param cycle: 测试周期
        :return:
        """
        tester = Tester()
        while True:
            print('测试器开始运行')
            tester.run()
            time.sleep(cycle)

    def scheduler_getter(self, cycle=GETTER_CYCLE):
        """
        定时获取代理
        :param cycle: 获取代理
        :return:
        """
        getter = Getter()
        while True:
            print('开始抓取代理')
            getter.run()
            time.sleep(cycle)

    def schedule_api(self):
        """
        开启API
        :return:
        """
        app.run(API_HOST, API_PORT)

    def run(self):
        """
        运行代理池
        :return:
        """
        print('代理池开始运行')
        if TESTER_ENABLED:
            tester_process = Process(target=self.scheduler_tester)
            tester_process.start()

        if GETTER_ENABLED:
            getter_process = Process(target=self.scheduler_getter)
            getter_process.start()

        if API_ENABLED:
            api_process = Process(target=self.schedule_api)
            api_process.start()