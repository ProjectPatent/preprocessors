"""
데이터 전처리하는 모듈
"""

from lxml import etree

from utils.time_utils import get_today_yymmdd, is_yymmdd_format
from projectKer.config.config import api_params

class DataParser():
    """
    XML 파일을 읽고 데이터를 전처리하는 클래스입니다.
    """

    def __init__(self, path, date=None):
        self.path = path
        self.corp_data_list = []
        self.univ_data_list = []
        if date is not None and is_yymmdd_format(date):
            self.date = date
        else:
            self.date = get_today_yymmdd()
        
    def xml_to_list(self):
        """
        기업, 대학 | 특허/실용신안, 디자인, 상표 xml파일을 읽어서 데이터를 리턴
        """
        
        # 기업
        self.read_xml(data_target='patent_utility',  data_class='corp')
        # self.read_xml(data_target='design_path', data_class='corp')
        # self.read_xml(data_target='trademark_path', data_class='corp')
        # # 대학
        # self.read_xml(data_target='patent_utility',  data_class='univ')
        # self.read_xml(data_target='design_path', data_class='univ')
        # self.read_xml(data_target='trademark_path', data_class='univ')


    def read_xml(self, data_target, data_class):
        path = f"{self.path}/{self.date}_{data_target}_{data_class}.xml"
        tree = etree.parse(path)
        root = tree.getroot()
        for item in root.iter('item'):
            temp = {}
            for key, value in api_params["patent_utility"].items():
                temp[f"{key}"] = item.find(f".//{value}").text
            self.corp_data_list.append(temp)

    # def read_data_design_data(self, data_path, data_class):
    #     path = data_path + f"{data_class}.xml"
    #     pass

    # def read_data_trademark_data(self, data_path, data_class):
    #     path = data_path + f"{data_class}.xml"
    #     pass



# print(DataParser().date)
data_path = "./data"
data_parser = DataParser(data_path)
data_parser.xml_to_list()
print(data_parser.corp_data_list)
