# Transfer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** | 明細番号 半角数字 重複/0はエラー　1～99の範囲で１からの連番とします 1件のみの場合は省略可（項目自体の設定が不要です）  | [optional] 
**transfer_amount** | **str** | 振込金額 半角数字 1以上、整数のみ  | 
**edi_info** | **str** | EDI情報 半角文字 振込許容文字を指定可 ・個人事業主のみ対象の項目のため、個人は対象外となります ・個人の場合は設定しても無効となり、処理に利用しません  | [optional] 
**beneficiary_bank_code** | **str** | 被仕向金融機関番号 半角数字  | 
**beneficiary_bank_name** | **str** | 被仕向金融機関名カナ 半角文字 参考値、処理に利用しません  | [optional] 
**beneficiary_branch_code** | **str** | 被仕向支店番号 半角数字  | 
**beneficiary_branch_name** | **str** | 被仕向支店名カナ 半角文字 参考値、処理に利用しません  | [optional] 
**account_type_code** | **str** | 科目コード（預金種別コード） 半角数字 1：普通、2：当座、4：貯蓄、9：その他  | 
**account_number** | **str** | 口座番号 半角数字 7桁未満の番号は右詰で、前ゼロで埋めること  | 
**beneficiary_name** | **str** | 受取人名 半角文字 振込許容文字を指定可 ただし、一部の非許容文字は、許容文字に変換を行います  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


