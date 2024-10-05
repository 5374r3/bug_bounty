# DOM XSS via an alternative prototype pollution vector

## This lab is vulnerable to [DOM XSS](https://portswigger.net/web-security/cross-site-scripting/dom-based) via client-side [prototype pollution](https://portswigger.net/web-security/prototype-pollution). To solve the lab:

1. Find a source that you can use to add arbitrary properties to the global `Object.prototype`.
2. Identify a gadget property that allows you to execute arbitrary JavaScript.
3. Combine these to call `alert()`.

You can solve this lab manually in your browser, or use [DOM Invader](https://portswigger.net/burp/documentation/desktop/tools/dom-invader) to help you.

---


step 1

add into to url `?__proto__[evilProperty]=payload`
go to console type `Object.prototype`
you will see new nothing changes
it means You've not found a prototype pollution source

![[lab1_object_prototype_not_polluted.png]]

`If the property was not added to the prototype, try using different techniques, 
`such as switching to dot notation rather than bracket notation, or vice versa:`

step 2

add into to url `?__proto__.evilProperty=payload`
go to console type `Object.prototype`
you will see new property added `evilProperty: 'payload'`
it means You've successfully found a prototype pollution source

![[lab1_object_prototype_polluted.png]]

step 3

go to sources find serachlogger.js file
observe manger.sequence code line

![[lab2_manager_sequence.png]]

add `/?__proto__.sequence=foo`

![[lab2_foo1_not_defined.png]]

go to searchlogger.js

add break point at eval and reload page
you will notice a="foo"

![[lab2_add_break_point_debugger.png]]

step 4

test with `?__proto__.sequence=alert(1)`

![[lab2_synex_error_alert_1.png]]

Hover the mouse over the `manager.sequence` reference and observe that its value is `alert(1)1`. This indicates that we have successfully passed our payload into the sink, but a numeric `1` character is being appended to it, resulting in invalid JavaScript syntax.

![[lab2_alert_1_result_not_lab_solved.png]]

step 5
Add trailing `minus` character to the payload to fix up the final JavaScript syntax:
`?__proto__.sequence=alert(1)-`

![[lab2_add_minus_in_alert_for_payload.png]]

![[portswigger_wsa/P03_advanced_topics/P24_Prototype-pollution/images/lab2_solved_lab.png]]
