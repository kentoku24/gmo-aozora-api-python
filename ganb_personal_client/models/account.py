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


class Account(object):
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
        'branch_code': 'str',
        'branch_name': 'str',
        'account_type_code': 'str',
        'account_type_name': 'str',
        'account_number': 'str',
        'primary_account_code': 'str',
        'primary_account_code_name': 'str',
        'account_name': 'str',
        'account_name_kana': 'str',
        'currency_code': 'str',
        'currency_name': 'str',
        'transfer_limit_amount': 'str'
    }

    attribute_map = {
        'account_id': 'accountId',
        'branch_code': 'branchCode',
        'branch_name': 'branchName',
        'account_type_code': 'accountTypeCode',
        'account_type_name': 'accountTypeName',
        'account_number': 'accountNumber',
        'primary_account_code': 'primaryAccountCode',
        'primary_account_code_name': 'primaryAccountCodeName',
        'account_name': 'accountName',
        'account_name_kana': 'accountNameKana',
        'currency_code': 'currencyCode',
        'currency_name': 'currencyName',
        'transfer_limit_amount': 'transferLimitAmount'
    }

    def __init__(self, account_id=None, branch_code=None, branch_name=None, account_type_code=None, account_type_name=None, account_number=None, primary_account_code=None, primary_account_code_name=None, account_name=None, account_name_kana=None, currency_code=None, currency_name=None, transfer_limit_amount=None):  # noqa: E501
        """Account - a model defined in Swagger"""  # noqa: E501

        self._account_id = None
        self._branch_code = None
        self._branch_name = None
        self._account_type_code = None
        self._account_type_name = None
        self._account_number = None
        self._primary_account_code = None
        self._primary_account_code_name = None
        self._account_name = None
        self._account_name_kana = None
        self._currency_code = None
        self._currency_name = None
        self._transfer_limit_amount = None
        self.discriminator = None

        self.account_id = account_id
        if branch_code is not None:
            self.branch_code = branch_code
        if branch_name is not None:
            self.branch_name = branch_name
        self.account_type_code = account_type_code
        self.account_type_name = account_type_name
        if account_number is not None:
            self.account_number = account_number
        if primary_account_code is not None:
            self.primary_account_code = primary_account_code
        if primary_account_code_name is not None:
            self.primary_account_code_name = primary_account_code_name
        if account_name is not None:
            self.account_name = account_name
        if account_name_kana is not None:
            self.account_name_kana = account_name_kana
        self.currency_code = currency_code
        self.currency_name = currency_name
        if transfer_limit_amount is not None:
            self.transfer_limit_amount = transfer_limit_amount

    @property
    def account_id(self):
        """Gets the account_id of this Account.  # noqa: E501

        口座ID 半角英数字 口座を識別するID   # noqa: E501

        :return: The account_id of this Account.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this Account.

        口座ID 半角英数字 口座を識別するID   # noqa: E501

        :param account_id: The account_id of this Account.  # noqa: E501
        :type: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501
        if account_id is not None and len(account_id) > 29:
            raise ValueError("Invalid value for `account_id`, length must be less than or equal to `29`")  # noqa: E501
        if account_id is not None and len(account_id) < 12:
            raise ValueError("Invalid value for `account_id`, length must be greater than or equal to `12`")  # noqa: E501

        self._account_id = account_id

    @property
    def branch_code(self):
        """Gets the branch_code of this Account.  # noqa: E501

        支店コード 半角数字 科目コードが以下の場合のみ設定されます 該当しない場合は項目自体を設定しません ・01=普通預金（有利息） ・02=普通預金（決済用）   # noqa: E501

        :return: The branch_code of this Account.  # noqa: E501
        :rtype: str
        """
        return self._branch_code

    @branch_code.setter
    def branch_code(self, branch_code):
        """Sets the branch_code of this Account.

        支店コード 半角数字 科目コードが以下の場合のみ設定されます 該当しない場合は項目自体を設定しません ・01=普通預金（有利息） ・02=普通預金（決済用）   # noqa: E501

        :param branch_code: The branch_code of this Account.  # noqa: E501
        :type: str
        """
        if branch_code is not None and len(branch_code) > 3:
            raise ValueError("Invalid value for `branch_code`, length must be less than or equal to `3`")  # noqa: E501
        if branch_code is not None and len(branch_code) < 3:
            raise ValueError("Invalid value for `branch_code`, length must be greater than or equal to `3`")  # noqa: E501

        self._branch_code = branch_code

    @property
    def branch_name(self):
        """Gets the branch_name of this Account.  # noqa: E501

        支店名 全角文字 科目コードが以下の場合のみ設定されます 該当しない場合は項目自体を設定しません ・01=普通預金（有利息） ・02=普通預金（決済用）   # noqa: E501

        :return: The branch_name of this Account.  # noqa: E501
        :rtype: str
        """
        return self._branch_name

    @branch_name.setter
    def branch_name(self, branch_name):
        """Sets the branch_name of this Account.

        支店名 全角文字 科目コードが以下の場合のみ設定されます 該当しない場合は項目自体を設定しません ・01=普通預金（有利息） ・02=普通預金（決済用）   # noqa: E501

        :param branch_name: The branch_name of this Account.  # noqa: E501
        :type: str
        """
        if branch_name is not None and len(branch_name) > 30:
            raise ValueError("Invalid value for `branch_name`, length must be less than or equal to `30`")  # noqa: E501
        if branch_name is not None and len(branch_name) < 1:
            raise ValueError("Invalid value for `branch_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._branch_name = branch_name

    @property
    def account_type_code(self):
        """Gets the account_type_code of this Account.  # noqa: E501

        科目コード 半角数字 ・01=普通預金（有利息） ・02=普通預金（決済用） ・11=円定期預金 ・51=外貨普通預金 ・81=証券コネクト口座   # noqa: E501

        :return: The account_type_code of this Account.  # noqa: E501
        :rtype: str
        """
        return self._account_type_code

    @account_type_code.setter
    def account_type_code(self, account_type_code):
        """Sets the account_type_code of this Account.

        科目コード 半角数字 ・01=普通預金（有利息） ・02=普通預金（決済用） ・11=円定期預金 ・51=外貨普通預金 ・81=証券コネクト口座   # noqa: E501

        :param account_type_code: The account_type_code of this Account.  # noqa: E501
        :type: str
        """
        if account_type_code is None:
            raise ValueError("Invalid value for `account_type_code`, must not be `None`")  # noqa: E501
        if account_type_code is not None and len(account_type_code) > 2:
            raise ValueError("Invalid value for `account_type_code`, length must be less than or equal to `2`")  # noqa: E501
        if account_type_code is not None and len(account_type_code) < 2:
            raise ValueError("Invalid value for `account_type_code`, length must be greater than or equal to `2`")  # noqa: E501

        self._account_type_code = account_type_code

    @property
    def account_type_name(self):
        """Gets the account_type_name of this Account.  # noqa: E501

        科目名 全角文字 科目コードの名称   # noqa: E501

        :return: The account_type_name of this Account.  # noqa: E501
        :rtype: str
        """
        return self._account_type_name

    @account_type_name.setter
    def account_type_name(self, account_type_name):
        """Sets the account_type_name of this Account.

        科目名 全角文字 科目コードの名称   # noqa: E501

        :param account_type_name: The account_type_name of this Account.  # noqa: E501
        :type: str
        """
        if account_type_name is None:
            raise ValueError("Invalid value for `account_type_name`, must not be `None`")  # noqa: E501
        if account_type_name is not None and len(account_type_name) > 10:
            raise ValueError("Invalid value for `account_type_name`, length must be less than or equal to `10`")  # noqa: E501
        if account_type_name is not None and len(account_type_name) < 1:
            raise ValueError("Invalid value for `account_type_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._account_type_name = account_type_name

    @property
    def account_number(self):
        """Gets the account_number of this Account.  # noqa: E501

        口座番号 半角数字 科目コードが以下の場合のみ設定されます 該当しない場合は項目自体を設定しません ・01=普通預金（有利息） ・02=普通預金（決済用）   # noqa: E501

        :return: The account_number of this Account.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this Account.

        口座番号 半角数字 科目コードが以下の場合のみ設定されます 該当しない場合は項目自体を設定しません ・01=普通預金（有利息） ・02=普通預金（決済用）   # noqa: E501

        :param account_number: The account_number of this Account.  # noqa: E501
        :type: str
        """
        if account_number is not None and len(account_number) > 7:
            raise ValueError("Invalid value for `account_number`, length must be less than or equal to `7`")  # noqa: E501
        if account_number is not None and len(account_number) < 7:
            raise ValueError("Invalid value for `account_number`, length must be greater than or equal to `7`")  # noqa: E501

        self._account_number = account_number

    @property
    def primary_account_code(self):
        """Gets the primary_account_code of this Account.  # noqa: E501

        代表口座コード 半角数字 ・1=代表口座 ・2=追加口座 科目コードが以下の場合のみ設定されます 該当しない場合は項目自体を設定しません ・01=普通預金（有利息） ・02=普通預金（決済用）   # noqa: E501

        :return: The primary_account_code of this Account.  # noqa: E501
        :rtype: str
        """
        return self._primary_account_code

    @primary_account_code.setter
    def primary_account_code(self, primary_account_code):
        """Sets the primary_account_code of this Account.

        代表口座コード 半角数字 ・1=代表口座 ・2=追加口座 科目コードが以下の場合のみ設定されます 該当しない場合は項目自体を設定しません ・01=普通預金（有利息） ・02=普通預金（決済用）   # noqa: E501

        :param primary_account_code: The primary_account_code of this Account.  # noqa: E501
        :type: str
        """
        if primary_account_code is not None and len(primary_account_code) > 1:
            raise ValueError("Invalid value for `primary_account_code`, length must be less than or equal to `1`")  # noqa: E501
        if primary_account_code is not None and len(primary_account_code) < 1:
            raise ValueError("Invalid value for `primary_account_code`, length must be greater than or equal to `1`")  # noqa: E501

        self._primary_account_code = primary_account_code

    @property
    def primary_account_code_name(self):
        """Gets the primary_account_code_name of this Account.  # noqa: E501

        代表口座コード名 全角文字 科目コードが以下の場合のみ設定されます 該当しない場合は項目自体を設定しません ・01=普通預金（有利息） ・02=普通預金（決済用）   # noqa: E501

        :return: The primary_account_code_name of this Account.  # noqa: E501
        :rtype: str
        """
        return self._primary_account_code_name

    @primary_account_code_name.setter
    def primary_account_code_name(self, primary_account_code_name):
        """Sets the primary_account_code_name of this Account.

        代表口座コード名 全角文字 科目コードが以下の場合のみ設定されます 該当しない場合は項目自体を設定しません ・01=普通預金（有利息） ・02=普通預金（決済用）   # noqa: E501

        :param primary_account_code_name: The primary_account_code_name of this Account.  # noqa: E501
        :type: str
        """
        if primary_account_code_name is not None and len(primary_account_code_name) > 4:
            raise ValueError("Invalid value for `primary_account_code_name`, length must be less than or equal to `4`")  # noqa: E501
        if primary_account_code_name is not None and len(primary_account_code_name) < 1:
            raise ValueError("Invalid value for `primary_account_code_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._primary_account_code_name = primary_account_code_name

    @property
    def account_name(self):
        """Gets the account_name of this Account.  # noqa: E501

        口座名義 全角文字 科目コードが以下の場合のみ設定されます 該当しない場合は項目自体を設定しません ・01=普通預金（有利息） ・02=普通預金（決済用）   # noqa: E501

        :return: The account_name of this Account.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this Account.

        口座名義 全角文字 科目コードが以下の場合のみ設定されます 該当しない場合は項目自体を設定しません ・01=普通預金（有利息） ・02=普通預金（決済用）   # noqa: E501

        :param account_name: The account_name of this Account.  # noqa: E501
        :type: str
        """
        if account_name is not None and len(account_name) > 48:
            raise ValueError("Invalid value for `account_name`, length must be less than or equal to `48`")  # noqa: E501
        if account_name is not None and len(account_name) < 1:
            raise ValueError("Invalid value for `account_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._account_name = account_name

    @property
    def account_name_kana(self):
        """Gets the account_name_kana of this Account.  # noqa: E501

        口座名義カナ 半角文字 科目コードが以下の場合のみ設定されます 該当しない場合は項目自体を設定しません ・01=普通預金（有利息） ・02=普通預金（決済用）   # noqa: E501

        :return: The account_name_kana of this Account.  # noqa: E501
        :rtype: str
        """
        return self._account_name_kana

    @account_name_kana.setter
    def account_name_kana(self, account_name_kana):
        """Sets the account_name_kana of this Account.

        口座名義カナ 半角文字 科目コードが以下の場合のみ設定されます 該当しない場合は項目自体を設定しません ・01=普通預金（有利息） ・02=普通預金（決済用）   # noqa: E501

        :param account_name_kana: The account_name_kana of this Account.  # noqa: E501
        :type: str
        """
        if account_name_kana is not None and len(account_name_kana) > 48:
            raise ValueError("Invalid value for `account_name_kana`, length must be less than or equal to `48`")  # noqa: E501
        if account_name_kana is not None and len(account_name_kana) < 1:
            raise ValueError("Invalid value for `account_name_kana`, length must be greater than or equal to `1`")  # noqa: E501

        self._account_name_kana = account_name_kana

    @property
    def currency_code(self):
        """Gets the currency_code of this Account.  # noqa: E501

        通貨コード 半角文字 ISO4217に準拠した通貨コード   # noqa: E501

        :return: The currency_code of this Account.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this Account.

        通貨コード 半角文字 ISO4217に準拠した通貨コード   # noqa: E501

        :param currency_code: The currency_code of this Account.  # noqa: E501
        :type: str
        """
        if currency_code is None:
            raise ValueError("Invalid value for `currency_code`, must not be `None`")  # noqa: E501
        if currency_code is not None and len(currency_code) > 3:
            raise ValueError("Invalid value for `currency_code`, length must be less than or equal to `3`")  # noqa: E501
        if currency_code is not None and len(currency_code) < 3:
            raise ValueError("Invalid value for `currency_code`, length must be greater than or equal to `3`")  # noqa: E501

        self._currency_code = currency_code

    @property
    def currency_name(self):
        """Gets the currency_name of this Account.  # noqa: E501

        通貨名 全角文字 ISO4217に準拠した通貨コードの当行での名称   # noqa: E501

        :return: The currency_name of this Account.  # noqa: E501
        :rtype: str
        """
        return self._currency_name

    @currency_name.setter
    def currency_name(self, currency_name):
        """Sets the currency_name of this Account.

        通貨名 全角文字 ISO4217に準拠した通貨コードの当行での名称   # noqa: E501

        :param currency_name: The currency_name of this Account.  # noqa: E501
        :type: str
        """
        if currency_name is None:
            raise ValueError("Invalid value for `currency_name`, must not be `None`")  # noqa: E501
        if currency_name is not None and len(currency_name) > 10:
            raise ValueError("Invalid value for `currency_name`, length must be less than or equal to `10`")  # noqa: E501
        if currency_name is not None and len(currency_name) < 1:
            raise ValueError("Invalid value for `currency_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._currency_name = currency_name

    @property
    def transfer_limit_amount(self):
        """Gets the transfer_limit_amount of this Account.  # noqa: E501

        振込限度額 半角数字 科目コードが以下の場合のみ設定されます 該当しない場合は項目自体を設定しません ・01=普通預金（有利息） ・02=普通預金（決済用）   # noqa: E501

        :return: The transfer_limit_amount of this Account.  # noqa: E501
        :rtype: str
        """
        return self._transfer_limit_amount

    @transfer_limit_amount.setter
    def transfer_limit_amount(self, transfer_limit_amount):
        """Sets the transfer_limit_amount of this Account.

        振込限度額 半角数字 科目コードが以下の場合のみ設定されます 該当しない場合は項目自体を設定しません ・01=普通預金（有利息） ・02=普通預金（決済用）   # noqa: E501

        :param transfer_limit_amount: The transfer_limit_amount of this Account.  # noqa: E501
        :type: str
        """
        if transfer_limit_amount is not None and len(transfer_limit_amount) > 12:
            raise ValueError("Invalid value for `transfer_limit_amount`, length must be less than or equal to `12`")  # noqa: E501
        if transfer_limit_amount is not None and len(transfer_limit_amount) < 1:
            raise ValueError("Invalid value for `transfer_limit_amount`, length must be greater than or equal to `1`")  # noqa: E501

        self._transfer_limit_amount = transfer_limit_amount

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
        if issubclass(Account, dict):
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
        if not isinstance(other, Account):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
