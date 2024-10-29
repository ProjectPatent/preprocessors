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

    def __init__(self, date=None):
        self.corp_data_list = []
        self.univ_data_list = []
        

        if date is not None and is_yymmdd_format(date):
            self.date = date
        else:
            self.date = get_today_yymmdd()
        
    def read_data(self):
        """
        기업, 대학 | 특허/실용신안, 디자인, 상표 xml파일을 읽어서 데이터를 리턴
        """
        data_path = "./data"
        
        patent_utility = "_patent_utility_"
        design = "_design_"
        trademark = "_trademark_"

        patent_utility_path = data_path + f"/{self.date}" + patent_utility
        design_path = data_path + f"/{self.date}" + design
        trademark_path = data_path + f"/{self.date}" + trademark
        
        self.read_data_patent_utility_data(patent_utility_path, 'corp')
        # self.corp_data_list.append(self.read_data_design_data(design_path, 'corp'))
        # self.corp_data_list.append(self.read_data_trademark_data(trademark_path, 'corp'))
        
        # self.univ_data_list.append(self.read_data_patent_utility_data(patent_utility_path, 'univ'))
        # self.univ_data_list.append(self.read_data_design_data(design_path, 'univ'))
        # self.univ_data_list.append(self.read_data_trademark_data(trademark_path, 'univ'))
        
        # print(self.corp_data_list)

        tree = etree.parse("./data/test.xml")
        root = tree.getroot()

        return root

    def read_data_patent_utility_data(self, data_path, data_class):
        path = data_path + f"{data_class}.xml"
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



# root = DataParser().read_data()
# for book in root.findall("book"):
#     title = book.find("title").text
#     author = book.find("author").text
#     year = book.find("year").text
#     price = book.find("price").text

#     print(f"Title: {title}")
#     print(f"Author: {author}")
#     print(f"Year: {year}")
#     print(f"Price: ${price}")


# print(DataParser().date)
DataParser().read_data()