Data Source=vagrant \\[インスタンス名],2000;Initial 
Catalog=[データベース名];User ID=[ユーザ名];
Password=[パスワード]

SELECT *
FROM purchases
WHERE category = "食費"
AND character_name = "ひつじ仙人";

/*2000, 3000*/