# coding: utf-8

"""
    GMO Aozora Net Bank Open API

    <p>オープンAPI仕様書（PDF版）は下記リンクをご参照ください</p> <div>   <div style='display:inline-block;'><a style='text-decoration:none; font-weight:bold; color:#00b8d4;' href='https://gmo-aozora.com/business/service/api-specification.html' target='_blank'>オープンAPI仕様書</a></div><div style='display:inline-block; margin-left:2px; left:2px; width:10px; height:10px; border-top:2px solid #00b8d4; border-right:2px solid #00b8d4; transparent;-webkit-transform:rotate(45deg); transform: rotate(45deg);'></div> </div> <h4 style='margin-top:30px; border-left: solid 4px #1B2F48; padding: 0.1em 0.5em; color:#1B2F48;'>共通仕様</h4> <div style='width:100%; margin:10px;'>   <p style='font-weight:bold; color:#616161;'>＜HTTPリクエストヘッダ＞</p>   <div style='display:table; margin-left:10px; background-color:#29659b;'>     <div style='display:table-cell; min-width:130px; padding:9px; border:1px solid #fff; color:#fff;'>項目</div>     <div style='display:table-cell; width:85%; padding:9px; border:1px solid #fff; color:#fff;'>仕様</div>   </div>   <div style='display:table; margin-left:10px;'>     <div style='display:table-cell; min-width:130px; padding:9px; border:1px solid #fff; color:#fff; background-color:#29659b;'>プロトコル</div>     <div style='display:table-cell; width:85%; padding:9px; border:1px solid #fff; background-color:#f8f8f8;'>HTTP1.1/HTTPS</div>   </div>   <div style='display:table; margin-left:10px;'>     <div style='display:table-cell; min-width:130px; padding:9px; border:1px solid #fff; color:#fff; background-color:#29659b;'>charset</div>     <div style='display:table-cell; width:85%; padding:9px; border:1px solid #fff; background-color:#f8f8f8;'>UTF-8</div>   </div>   <div style='display:table; margin-left:10px;'>     <div style='display:table-cell; min-width:130px; padding:9px; border:1px solid #fff; color:#fff; background-color:#29659b;'>content-type</div>     <div style='display:table-cell; width:85%; padding:9px; border:1px solid #fff; background-color:#f8f8f8;'>application/json</div>   </div>   <div style='display:table; margin-left:10px;'>     <div style='display:table-cell; min-width:130px; padding:9px; border:1px solid #fff; color:#fff; background-color:#29659b;'>domain_name</div>     <div style='display:table-cell; width:85%; padding:9px; border:1px solid #fff; background-color:#f8f8f8;'>       本番環境：api.gmo-aozora.com</br>       開発環境：stg-api.gmo-aozora.com     </div>   </div>   <div style='display:table; margin-left:10px;'>     <div style='display:table-cell; min-width:130px; padding:9px; border:1px solid #fff; color:#fff; background-color:#29659b;'>メインURL</div>     <div style='display:table-cell; width:85%; padding:9px; border:1px solid #fff; background-color:#f8f8f8;'>       https://{domain_name}/ganb/api/personal/{version}</br>       <span style='border-bottom:solid 1px;'>Version:1.x.x</span> の場合</br>       　https://api.gmo-aozora.com/ganb/api/personal/<span style='border-bottom:solid 1px;'>v1</span>     </div>   </div> </div> <div style='margin:20px 10px;'>   <p style='font-weight:bold; color:#616161;'>＜リクエスト共通仕様＞</p>   <p style='padding-left:20px; font-weight:bold; color:#616161;'>NULLデータの扱い</p>   <p style='padding-left:40px;'>パラメータの値が空の場合、またはパラメータ自体が設定されていない場合、どちらもNULLとして扱います</p> </div> <div style='margin:20px 10px;'>   <p style='font-weight:bold; color:#616161;'>＜レスポンス共通仕様＞</p>   <p style='padding-left:20px; font-weight:bold; color:#616161;'>NULLデータの扱い</p>   <ul>     <li>レスポンスデータ</li>       <ul>         <li style='list-style-type:none;'>レスポンスデータの値が空の場合または、レスポンスデータ自体が設定されない場合は「項目自体を設定しません」と記載</li>       </ul>     <li>配列</li>       <ul>         <li style='list-style-type:none;'>配列の要素の値が空の場合は「空のリスト」と記載</li>         <li style='list-style-type:none;'>配列自体が設定されない場合は「項目自体を設定しません」と記載</li>       </ul>   </ul> </div> <div style='margin:20px 10px;'>   <p style='font-weight:bold; color:#616161;'>＜更新系APIに関する注意事項＞</p>   <ul>     <li style='list-style-type:none;'>更新系処理がタイムアウトとなった場合、処理自体は実行されている可能性がありますので、</li>     <li style='list-style-type:none;'>再実行を行う必要がある場合は必ず照会系の処理で実行状況を確認してから再実行を行ってください</li>   </ul> </div>   # noqa: E501

    OpenAPI spec version: 1.1.12
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ganb_personal_client.models.bulk_transfer_info import BulkTransferInfo  # noqa: F401,E501


class BulkTransferResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'account_id': 'str',
        'remitter_name': 'str',
        'transfer_designated_date': 'str',
        'transfer_data_name': 'str',
        'total_count': 'str',
        'total_amount': 'str',
        'bulk_transfer_infos': 'list[BulkTransferInfo]'
    }

    attribute_map = {
        'account_id': 'accountId',
        'remitter_name': 'remitterName',
        'transfer_designated_date': 'transferDesignatedDate',
        'transfer_data_name': 'transferDataName',
        'total_count': 'totalCount',
        'total_amount': 'totalAmount',
        'bulk_transfer_infos': 'bulkTransferInfos'
    }

    def __init__(self, account_id=None, remitter_name=None, transfer_designated_date=None, transfer_data_name=None, total_count=None, total_amount=None, bulk_transfer_infos=None):  # noqa: E501
        """BulkTransferResponse - a model defined in Swagger"""  # noqa: E501

        self._account_id = None
        self._remitter_name = None
        self._transfer_designated_date = None
        self._transfer_data_name = None
        self._total_count = None
        self._total_amount = None
        self._bulk_transfer_infos = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if remitter_name is not None:
            self.remitter_name = remitter_name
        if transfer_designated_date is not None:
            self.transfer_designated_date = transfer_designated_date
        if transfer_data_name is not None:
            self.transfer_data_name = transfer_data_name
        if total_count is not None:
            self.total_count = total_count
        if total_amount is not None:
            self.total_amount = total_amount
        if bulk_transfer_infos is not None:
            self.bulk_transfer_infos = bulk_transfer_infos

    @property
    def account_id(self):
        """Gets the account_id of this BulkTransferResponse.  # noqa: E501

        口座ID 半角英数字 口座を識別するID   # noqa: E501

        :return: The account_id of this BulkTransferResponse.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this BulkTransferResponse.

        口座ID 半角英数字 口座を識別するID   # noqa: E501

        :param account_id: The account_id of this BulkTransferResponse.  # noqa: E501
        :type: str
        """
        if account_id is not None and len(account_id) > 29:
            raise ValueError("Invalid value for `account_id`, length must be less than or equal to `29`")  # noqa: E501
        if account_id is not None and len(account_id) < 12:
            raise ValueError("Invalid value for `account_id`, length must be greater than or equal to `12`")  # noqa: E501

        self._account_id = account_id

    @property
    def remitter_name(self):
        """Gets the remitter_name of this BulkTransferResponse.  # noqa: E501

        振込依頼人名 半角文字   # noqa: E501

        :return: The remitter_name of this BulkTransferResponse.  # noqa: E501
        :rtype: str
        """
        return self._remitter_name

    @remitter_name.setter
    def remitter_name(self, remitter_name):
        """Sets the remitter_name of this BulkTransferResponse.

        振込依頼人名 半角文字   # noqa: E501

        :param remitter_name: The remitter_name of this BulkTransferResponse.  # noqa: E501
        :type: str
        """
        if remitter_name is not None and len(remitter_name) > 48:
            raise ValueError("Invalid value for `remitter_name`, length must be less than or equal to `48`")  # noqa: E501
        if remitter_name is not None and len(remitter_name) < 1:
            raise ValueError("Invalid value for `remitter_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._remitter_name = remitter_name

    @property
    def transfer_designated_date(self):
        """Gets the transfer_designated_date of this BulkTransferResponse.  # noqa: E501

        振込指定日 半角文字 YYYY-MM-DD形式   # noqa: E501

        :return: The transfer_designated_date of this BulkTransferResponse.  # noqa: E501
        :rtype: str
        """
        return self._transfer_designated_date

    @transfer_designated_date.setter
    def transfer_designated_date(self, transfer_designated_date):
        """Sets the transfer_designated_date of this BulkTransferResponse.

        振込指定日 半角文字 YYYY-MM-DD形式   # noqa: E501

        :param transfer_designated_date: The transfer_designated_date of this BulkTransferResponse.  # noqa: E501
        :type: str
        """
        if transfer_designated_date is not None and len(transfer_designated_date) > 10:
            raise ValueError("Invalid value for `transfer_designated_date`, length must be less than or equal to `10`")  # noqa: E501
        if transfer_designated_date is not None and len(transfer_designated_date) < 10:
            raise ValueError("Invalid value for `transfer_designated_date`, length must be greater than or equal to `10`")  # noqa: E501

        self._transfer_designated_date = transfer_designated_date

    @property
    def transfer_data_name(self):
        """Gets the transfer_data_name of this BulkTransferResponse.  # noqa: E501

        振込データ名 全半角文字 作成した総合振込のデータを区別するためのメモ   # noqa: E501

        :return: The transfer_data_name of this BulkTransferResponse.  # noqa: E501
        :rtype: str
        """
        return self._transfer_data_name

    @transfer_data_name.setter
    def transfer_data_name(self, transfer_data_name):
        """Sets the transfer_data_name of this BulkTransferResponse.

        振込データ名 全半角文字 作成した総合振込のデータを区別するためのメモ   # noqa: E501

        :param transfer_data_name: The transfer_data_name of this BulkTransferResponse.  # noqa: E501
        :type: str
        """
        if transfer_data_name is not None and len(transfer_data_name) > 10:
            raise ValueError("Invalid value for `transfer_data_name`, length must be less than or equal to `10`")  # noqa: E501
        if transfer_data_name is not None and len(transfer_data_name) < 1:
            raise ValueError("Invalid value for `transfer_data_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._transfer_data_name = transfer_data_name

    @property
    def total_count(self):
        """Gets the total_count of this BulkTransferResponse.  # noqa: E501

        合計件数 半角数字   # noqa: E501

        :return: The total_count of this BulkTransferResponse.  # noqa: E501
        :rtype: str
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this BulkTransferResponse.

        合計件数 半角数字   # noqa: E501

        :param total_count: The total_count of this BulkTransferResponse.  # noqa: E501
        :type: str
        """
        if total_count is not None and len(total_count) > 6:
            raise ValueError("Invalid value for `total_count`, length must be less than or equal to `6`")  # noqa: E501
        if total_count is not None and len(total_count) < 1:
            raise ValueError("Invalid value for `total_count`, length must be greater than or equal to `1`")  # noqa: E501

        self._total_count = total_count

    @property
    def total_amount(self):
        """Gets the total_amount of this BulkTransferResponse.  # noqa: E501

        合計金額 半角数字   # noqa: E501

        :return: The total_amount of this BulkTransferResponse.  # noqa: E501
        :rtype: str
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """Sets the total_amount of this BulkTransferResponse.

        合計金額 半角数字   # noqa: E501

        :param total_amount: The total_amount of this BulkTransferResponse.  # noqa: E501
        :type: str
        """
        if total_amount is not None and len(total_amount) > 20:
            raise ValueError("Invalid value for `total_amount`, length must be less than or equal to `20`")  # noqa: E501
        if total_amount is not None and len(total_amount) < 1:
            raise ValueError("Invalid value for `total_amount`, length must be greater than or equal to `1`")  # noqa: E501

        self._total_amount = total_amount

    @property
    def bulk_transfer_infos(self):
        """Gets the bulk_transfer_infos of this BulkTransferResponse.  # noqa: E501

        総合振込明細情報 総合振込明細のリスト 明細情報取得フラグが「True：取得する」、かつ明細情報取得結果フラグが「True：取得可」のときのみ設定します それ以外は項目自体を設定しません   # noqa: E501

        :return: The bulk_transfer_infos of this BulkTransferResponse.  # noqa: E501
        :rtype: list[BulkTransferInfo]
        """
        return self._bulk_transfer_infos

    @bulk_transfer_infos.setter
    def bulk_transfer_infos(self, bulk_transfer_infos):
        """Sets the bulk_transfer_infos of this BulkTransferResponse.

        総合振込明細情報 総合振込明細のリスト 明細情報取得フラグが「True：取得する」、かつ明細情報取得結果フラグが「True：取得可」のときのみ設定します それ以外は項目自体を設定しません   # noqa: E501

        :param bulk_transfer_infos: The bulk_transfer_infos of this BulkTransferResponse.  # noqa: E501
        :type: list[BulkTransferInfo]
        """

        self._bulk_transfer_infos = bulk_transfer_infos

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(BulkTransferResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BulkTransferResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other