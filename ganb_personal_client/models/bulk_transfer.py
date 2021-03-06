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


class BulkTransfer(object):
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
        'item_id': 'str',
        'beneficiary_bank_code': 'str',
        'beneficiary_bank_name': 'str',
        'beneficiary_branch_code': 'str',
        'beneficiary_branch_name': 'str',
        'clearing_house_name': 'str',
        'account_type_code': 'str',
        'account_number': 'str',
        'beneficiary_name': 'str',
        'transfer_amount': 'str',
        'new_code': 'str',
        'edi_info': 'str',
        'transfer_designated_type': 'str',
        'identification': 'str'
    }

    attribute_map = {
        'item_id': 'itemId',
        'beneficiary_bank_code': 'beneficiaryBankCode',
        'beneficiary_bank_name': 'beneficiaryBankName',
        'beneficiary_branch_code': 'beneficiaryBranchCode',
        'beneficiary_branch_name': 'beneficiaryBranchName',
        'clearing_house_name': 'clearingHouseName',
        'account_type_code': 'accountTypeCode',
        'account_number': 'accountNumber',
        'beneficiary_name': 'beneficiaryName',
        'transfer_amount': 'transferAmount',
        'new_code': 'newCode',
        'edi_info': 'ediInfo',
        'transfer_designated_type': 'transferDesignatedType',
        'identification': 'identification'
    }

    def __init__(self, item_id=None, beneficiary_bank_code=None, beneficiary_bank_name=None, beneficiary_branch_code=None, beneficiary_branch_name=None, clearing_house_name=None, account_type_code=None, account_number=None, beneficiary_name=None, transfer_amount=None, new_code=None, edi_info=None, transfer_designated_type=None, identification=None):  # noqa: E501
        """BulkTransfer - a model defined in Swagger"""  # noqa: E501

        self._item_id = None
        self._beneficiary_bank_code = None
        self._beneficiary_bank_name = None
        self._beneficiary_branch_code = None
        self._beneficiary_branch_name = None
        self._clearing_house_name = None
        self._account_type_code = None
        self._account_number = None
        self._beneficiary_name = None
        self._transfer_amount = None
        self._new_code = None
        self._edi_info = None
        self._transfer_designated_type = None
        self._identification = None
        self.discriminator = None

        self.item_id = item_id
        self.beneficiary_bank_code = beneficiary_bank_code
        if beneficiary_bank_name is not None:
            self.beneficiary_bank_name = beneficiary_bank_name
        self.beneficiary_branch_code = beneficiary_branch_code
        if beneficiary_branch_name is not None:
            self.beneficiary_branch_name = beneficiary_branch_name
        if clearing_house_name is not None:
            self.clearing_house_name = clearing_house_name
        self.account_type_code = account_type_code
        self.account_number = account_number
        self.beneficiary_name = beneficiary_name
        self.transfer_amount = transfer_amount
        if new_code is not None:
            self.new_code = new_code
        if edi_info is not None:
            self.edi_info = edi_info
        if transfer_designated_type is not None:
            self.transfer_designated_type = transfer_designated_type
        if identification is not None:
            self.identification = identification

    @property
    def item_id(self):
        """Gets the item_id of this BulkTransfer.  # noqa: E501

        明細番号 半角数字 重複/0はエラー　1～9999とします   # noqa: E501

        :return: The item_id of this BulkTransfer.  # noqa: E501
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this BulkTransfer.

        明細番号 半角数字 重複/0はエラー　1～9999とします   # noqa: E501

        :param item_id: The item_id of this BulkTransfer.  # noqa: E501
        :type: str
        """
        if item_id is None:
            raise ValueError("Invalid value for `item_id`, must not be `None`")  # noqa: E501
        if item_id is not None and len(item_id) > 6:
            raise ValueError("Invalid value for `item_id`, length must be less than or equal to `6`")  # noqa: E501
        if item_id is not None and len(item_id) < 1:
            raise ValueError("Invalid value for `item_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._item_id = item_id

    @property
    def beneficiary_bank_code(self):
        """Gets the beneficiary_bank_code of this BulkTransfer.  # noqa: E501

        被仕向金融機関番号 半角数字   # noqa: E501

        :return: The beneficiary_bank_code of this BulkTransfer.  # noqa: E501
        :rtype: str
        """
        return self._beneficiary_bank_code

    @beneficiary_bank_code.setter
    def beneficiary_bank_code(self, beneficiary_bank_code):
        """Sets the beneficiary_bank_code of this BulkTransfer.

        被仕向金融機関番号 半角数字   # noqa: E501

        :param beneficiary_bank_code: The beneficiary_bank_code of this BulkTransfer.  # noqa: E501
        :type: str
        """
        if beneficiary_bank_code is None:
            raise ValueError("Invalid value for `beneficiary_bank_code`, must not be `None`")  # noqa: E501
        if beneficiary_bank_code is not None and len(beneficiary_bank_code) > 4:
            raise ValueError("Invalid value for `beneficiary_bank_code`, length must be less than or equal to `4`")  # noqa: E501
        if beneficiary_bank_code is not None and len(beneficiary_bank_code) < 4:
            raise ValueError("Invalid value for `beneficiary_bank_code`, length must be greater than or equal to `4`")  # noqa: E501

        self._beneficiary_bank_code = beneficiary_bank_code

    @property
    def beneficiary_bank_name(self):
        """Gets the beneficiary_bank_name of this BulkTransfer.  # noqa: E501

        被仕向金融機関名カナ 半角文字 参考値、処理に利用しません   # noqa: E501

        :return: The beneficiary_bank_name of this BulkTransfer.  # noqa: E501
        :rtype: str
        """
        return self._beneficiary_bank_name

    @beneficiary_bank_name.setter
    def beneficiary_bank_name(self, beneficiary_bank_name):
        """Sets the beneficiary_bank_name of this BulkTransfer.

        被仕向金融機関名カナ 半角文字 参考値、処理に利用しません   # noqa: E501

        :param beneficiary_bank_name: The beneficiary_bank_name of this BulkTransfer.  # noqa: E501
        :type: str
        """
        if beneficiary_bank_name is not None and len(beneficiary_bank_name) > 30:
            raise ValueError("Invalid value for `beneficiary_bank_name`, length must be less than or equal to `30`")  # noqa: E501
        if beneficiary_bank_name is not None and len(beneficiary_bank_name) < 1:
            raise ValueError("Invalid value for `beneficiary_bank_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._beneficiary_bank_name = beneficiary_bank_name

    @property
    def beneficiary_branch_code(self):
        """Gets the beneficiary_branch_code of this BulkTransfer.  # noqa: E501

        被仕向支店番号 半角数字   # noqa: E501

        :return: The beneficiary_branch_code of this BulkTransfer.  # noqa: E501
        :rtype: str
        """
        return self._beneficiary_branch_code

    @beneficiary_branch_code.setter
    def beneficiary_branch_code(self, beneficiary_branch_code):
        """Sets the beneficiary_branch_code of this BulkTransfer.

        被仕向支店番号 半角数字   # noqa: E501

        :param beneficiary_branch_code: The beneficiary_branch_code of this BulkTransfer.  # noqa: E501
        :type: str
        """
        if beneficiary_branch_code is None:
            raise ValueError("Invalid value for `beneficiary_branch_code`, must not be `None`")  # noqa: E501
        if beneficiary_branch_code is not None and len(beneficiary_branch_code) > 3:
            raise ValueError("Invalid value for `beneficiary_branch_code`, length must be less than or equal to `3`")  # noqa: E501
        if beneficiary_branch_code is not None and len(beneficiary_branch_code) < 3:
            raise ValueError("Invalid value for `beneficiary_branch_code`, length must be greater than or equal to `3`")  # noqa: E501

        self._beneficiary_branch_code = beneficiary_branch_code

    @property
    def beneficiary_branch_name(self):
        """Gets the beneficiary_branch_name of this BulkTransfer.  # noqa: E501

        被仕向支店名カナ 半角文字 参考値、処理に利用しません   # noqa: E501

        :return: The beneficiary_branch_name of this BulkTransfer.  # noqa: E501
        :rtype: str
        """
        return self._beneficiary_branch_name

    @beneficiary_branch_name.setter
    def beneficiary_branch_name(self, beneficiary_branch_name):
        """Sets the beneficiary_branch_name of this BulkTransfer.

        被仕向支店名カナ 半角文字 参考値、処理に利用しません   # noqa: E501

        :param beneficiary_branch_name: The beneficiary_branch_name of this BulkTransfer.  # noqa: E501
        :type: str
        """
        if beneficiary_branch_name is not None and len(beneficiary_branch_name) > 15:
            raise ValueError("Invalid value for `beneficiary_branch_name`, length must be less than or equal to `15`")  # noqa: E501
        if beneficiary_branch_name is not None and len(beneficiary_branch_name) < 1:
            raise ValueError("Invalid value for `beneficiary_branch_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._beneficiary_branch_name = beneficiary_branch_name

    @property
    def clearing_house_name(self):
        """Gets the clearing_house_name of this BulkTransfer.  # noqa: E501

        手形交換所番号 半角文字 入力する場合は、ALL０,ALLスペースであること 参考値、処理に利用しません   # noqa: E501

        :return: The clearing_house_name of this BulkTransfer.  # noqa: E501
        :rtype: str
        """
        return self._clearing_house_name

    @clearing_house_name.setter
    def clearing_house_name(self, clearing_house_name):
        """Sets the clearing_house_name of this BulkTransfer.

        手形交換所番号 半角文字 入力する場合は、ALL０,ALLスペースであること 参考値、処理に利用しません   # noqa: E501

        :param clearing_house_name: The clearing_house_name of this BulkTransfer.  # noqa: E501
        :type: str
        """
        if clearing_house_name is not None and len(clearing_house_name) > 4:
            raise ValueError("Invalid value for `clearing_house_name`, length must be less than or equal to `4`")  # noqa: E501
        if clearing_house_name is not None and len(clearing_house_name) < 4:
            raise ValueError("Invalid value for `clearing_house_name`, length must be greater than or equal to `4`")  # noqa: E501

        self._clearing_house_name = clearing_house_name

    @property
    def account_type_code(self):
        """Gets the account_type_code of this BulkTransfer.  # noqa: E501

        科目コード（預金種別コード） 半角数字 1：普通、2：当座、4：貯蓄、9：その他   # noqa: E501

        :return: The account_type_code of this BulkTransfer.  # noqa: E501
        :rtype: str
        """
        return self._account_type_code

    @account_type_code.setter
    def account_type_code(self, account_type_code):
        """Sets the account_type_code of this BulkTransfer.

        科目コード（預金種別コード） 半角数字 1：普通、2：当座、4：貯蓄、9：その他   # noqa: E501

        :param account_type_code: The account_type_code of this BulkTransfer.  # noqa: E501
        :type: str
        """
        if account_type_code is None:
            raise ValueError("Invalid value for `account_type_code`, must not be `None`")  # noqa: E501
        if account_type_code is not None and len(account_type_code) > 1:
            raise ValueError("Invalid value for `account_type_code`, length must be less than or equal to `1`")  # noqa: E501
        if account_type_code is not None and len(account_type_code) < 1:
            raise ValueError("Invalid value for `account_type_code`, length must be greater than or equal to `1`")  # noqa: E501

        self._account_type_code = account_type_code

    @property
    def account_number(self):
        """Gets the account_number of this BulkTransfer.  # noqa: E501

        口座番号 半角数字 7桁未満の番号は右詰で、前ゼロで埋めること   # noqa: E501

        :return: The account_number of this BulkTransfer.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this BulkTransfer.

        口座番号 半角数字 7桁未満の番号は右詰で、前ゼロで埋めること   # noqa: E501

        :param account_number: The account_number of this BulkTransfer.  # noqa: E501
        :type: str
        """
        if account_number is None:
            raise ValueError("Invalid value for `account_number`, must not be `None`")  # noqa: E501
        if account_number is not None and len(account_number) > 7:
            raise ValueError("Invalid value for `account_number`, length must be less than or equal to `7`")  # noqa: E501
        if account_number is not None and len(account_number) < 7:
            raise ValueError("Invalid value for `account_number`, length must be greater than or equal to `7`")  # noqa: E501

        self._account_number = account_number

    @property
    def beneficiary_name(self):
        """Gets the beneficiary_name of this BulkTransfer.  # noqa: E501

        受取人名 半角文字 振込許容文字を指定可 ただし、一部の非許容文字は、許容文字に変換を行います 30文字目まで有効（31文字目以降は切り捨てます）   # noqa: E501

        :return: The beneficiary_name of this BulkTransfer.  # noqa: E501
        :rtype: str
        """
        return self._beneficiary_name

    @beneficiary_name.setter
    def beneficiary_name(self, beneficiary_name):
        """Sets the beneficiary_name of this BulkTransfer.

        受取人名 半角文字 振込許容文字を指定可 ただし、一部の非許容文字は、許容文字に変換を行います 30文字目まで有効（31文字目以降は切り捨てます）   # noqa: E501

        :param beneficiary_name: The beneficiary_name of this BulkTransfer.  # noqa: E501
        :type: str
        """
        if beneficiary_name is None:
            raise ValueError("Invalid value for `beneficiary_name`, must not be `None`")  # noqa: E501
        if beneficiary_name is not None and len(beneficiary_name) > 48:
            raise ValueError("Invalid value for `beneficiary_name`, length must be less than or equal to `48`")  # noqa: E501
        if beneficiary_name is not None and len(beneficiary_name) < 1:
            raise ValueError("Invalid value for `beneficiary_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._beneficiary_name = beneficiary_name

    @property
    def transfer_amount(self):
        """Gets the transfer_amount of this BulkTransfer.  # noqa: E501

        振込金額 半角数字 1以上9,999,999,999円以下　数値のみでカンマ、マイナス不可   # noqa: E501

        :return: The transfer_amount of this BulkTransfer.  # noqa: E501
        :rtype: str
        """
        return self._transfer_amount

    @transfer_amount.setter
    def transfer_amount(self, transfer_amount):
        """Sets the transfer_amount of this BulkTransfer.

        振込金額 半角数字 1以上9,999,999,999円以下　数値のみでカンマ、マイナス不可   # noqa: E501

        :param transfer_amount: The transfer_amount of this BulkTransfer.  # noqa: E501
        :type: str
        """
        if transfer_amount is None:
            raise ValueError("Invalid value for `transfer_amount`, must not be `None`")  # noqa: E501
        if transfer_amount is not None and len(transfer_amount) > 20:
            raise ValueError("Invalid value for `transfer_amount`, length must be less than or equal to `20`")  # noqa: E501
        if transfer_amount is not None and len(transfer_amount) < 1:
            raise ValueError("Invalid value for `transfer_amount`, length must be greater than or equal to `1`")  # noqa: E501

        self._transfer_amount = transfer_amount

    @property
    def new_code(self):
        """Gets the new_code of this BulkTransfer.  # noqa: E501

        新規コード 半角文字 入力する場合は、数値またはスペースであること 参考値、処理に利用しません   # noqa: E501

        :return: The new_code of this BulkTransfer.  # noqa: E501
        :rtype: str
        """
        return self._new_code

    @new_code.setter
    def new_code(self, new_code):
        """Sets the new_code of this BulkTransfer.

        新規コード 半角文字 入力する場合は、数値またはスペースであること 参考値、処理に利用しません   # noqa: E501

        :param new_code: The new_code of this BulkTransfer.  # noqa: E501
        :type: str
        """
        if new_code is not None and len(new_code) > 1:
            raise ValueError("Invalid value for `new_code`, length must be less than or equal to `1`")  # noqa: E501
        if new_code is not None and len(new_code) < 1:
            raise ValueError("Invalid value for `new_code`, length must be greater than or equal to `1`")  # noqa: E501

        self._new_code = new_code

    @property
    def edi_info(self):
        """Gets the edi_info of this BulkTransfer.  # noqa: E501

        EDI情報 半角文字 振込許容文字を指定可   # noqa: E501

        :return: The edi_info of this BulkTransfer.  # noqa: E501
        :rtype: str
        """
        return self._edi_info

    @edi_info.setter
    def edi_info(self, edi_info):
        """Sets the edi_info of this BulkTransfer.

        EDI情報 半角文字 振込許容文字を指定可   # noqa: E501

        :param edi_info: The edi_info of this BulkTransfer.  # noqa: E501
        :type: str
        """
        if edi_info is not None and len(edi_info) > 20:
            raise ValueError("Invalid value for `edi_info`, length must be less than or equal to `20`")  # noqa: E501
        if edi_info is not None and len(edi_info) < 1:
            raise ValueError("Invalid value for `edi_info`, length must be greater than or equal to `1`")  # noqa: E501

        self._edi_info = edi_info

    @property
    def transfer_designated_type(self):
        """Gets the transfer_designated_type of this BulkTransfer.  # noqa: E501

        振込指定区分 半角文字 入力する場合は、7：電信のみ　またはスペースであること 参考値、処理に利用しません（入力にかかわらず、すべて7：電信扱いとなります）   # noqa: E501

        :return: The transfer_designated_type of this BulkTransfer.  # noqa: E501
        :rtype: str
        """
        return self._transfer_designated_type

    @transfer_designated_type.setter
    def transfer_designated_type(self, transfer_designated_type):
        """Sets the transfer_designated_type of this BulkTransfer.

        振込指定区分 半角文字 入力する場合は、7：電信のみ　またはスペースであること 参考値、処理に利用しません（入力にかかわらず、すべて7：電信扱いとなります）   # noqa: E501

        :param transfer_designated_type: The transfer_designated_type of this BulkTransfer.  # noqa: E501
        :type: str
        """
        if transfer_designated_type is not None and len(transfer_designated_type) > 1:
            raise ValueError("Invalid value for `transfer_designated_type`, length must be less than or equal to `1`")  # noqa: E501
        if transfer_designated_type is not None and len(transfer_designated_type) < 1:
            raise ValueError("Invalid value for `transfer_designated_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._transfer_designated_type = transfer_designated_type

    @property
    def identification(self):
        """Gets the identification of this BulkTransfer.  # noqa: E501

        識別表示 半角文字 本項目が「Y」であればEDI情報は振込先に通知、または省略/NULL/スペースであれば振込先には通知しません   # noqa: E501

        :return: The identification of this BulkTransfer.  # noqa: E501
        :rtype: str
        """
        return self._identification

    @identification.setter
    def identification(self, identification):
        """Sets the identification of this BulkTransfer.

        識別表示 半角文字 本項目が「Y」であればEDI情報は振込先に通知、または省略/NULL/スペースであれば振込先には通知しません   # noqa: E501

        :param identification: The identification of this BulkTransfer.  # noqa: E501
        :type: str
        """
        if identification is not None and len(identification) > 1:
            raise ValueError("Invalid value for `identification`, length must be less than or equal to `1`")  # noqa: E501
        if identification is not None and len(identification) < 1:
            raise ValueError("Invalid value for `identification`, length must be greater than or equal to `1`")  # noqa: E501

        self._identification = identification

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
        if issubclass(BulkTransfer, dict):
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
        if not isinstance(other, BulkTransfer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
