import pandas as pd
from pandas import DataFrame
from bs4 import BeautifulSoup, Tag
from src.dto import DataDto


class Scraper:
    _soup: BeautifulSoup = None

    def __init__(self, text):
        self.html_text = text
        self._soup = BeautifulSoup(self.html_text, "lxml")

    def get_list_table_row(self) -> list[Tag]:
        return self._soup.find_all("div", {"class": "tableRow panelRow ui-draggable ui-draggable-handle"})

    @staticmethod
    def _get_topic_cluster_name(div: Tag) -> str:
        return div.find("div", {"class": "keywords nowrap"}).text

    @staticmethod
    def _get_topic_cluster_id(div: Tag) -> str:
        return div.find("div", {"class": "topicId"}).text

    @staticmethod
    def _get_scholarly_output(div: Tag) -> str:
        return div.find("button", {"class": "link primary-link showPublications"}).text

    @staticmethod
    def _get_publication_share(div: Tag) -> str:
        return div.find_all("div", {"class": "tableCell number"})[1].text

    @staticmethod
    def _get_fwci(div: Tag) -> str:
        return div.find_all("div", {"class": "tableCell number"})[2].text

    @staticmethod
    def _get_prominence_percentile(div: Tag) -> str:
        return div.find("div", {"class": "tableCell prominence"}).find("button", {"class": "link primary-link percentileVal"}).text

    @staticmethod
    def to_data_frame(data_list: list[DataDto]) -> DataFrame:
        list_topic_cluster_name = []
        list_topic_cluster_id = []
        list_scholarly_output = []
        list_publication_share = []
        list_fwci = []
        list_prominence_percentile = []
        for data in data_list:
            list_topic_cluster_name.append(data.cluster_name)
            list_topic_cluster_id.append(data.cluster_id)
            list_scholarly_output.append(data.scholarly_output)
            list_publication_share.append(data.publication_share)
            list_fwci.append(data.fwci)
            list_prominence_percentile.append(data.prominence_percentile)
        return pd.DataFrame({
            "Cluster Name": list_topic_cluster_name,
            "Cluster Id": list_topic_cluster_id,
            "Scholarly Output": list_scholarly_output,
            "Publication Share": list_publication_share,
            "FWCI": list_fwci,
            "Prominence Percentile": list_prominence_percentile
        })

    def start(self) -> DataFrame:
        return_list = []
        for i in self.get_list_table_row():
            return_list.append(DataDto(
                self._get_topic_cluster_name(i),
                self._get_topic_cluster_id(i),
                self._get_scholarly_output(i),
                self._get_publication_share(i),
                self._get_fwci(i),
                self._get_prominence_percentile(i)
            ))
        return self.to_data_frame(return_list)
