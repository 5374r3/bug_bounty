# Client-side prototype pollution via browser APIs

## This lab is vulnerable to [DOM XSS](https://portswigger.net/web-security/cross-site-scripting/dom-based) via client-side [prototype pollution](https://portswigger.net/web-security/prototype-pollution). The website's developers have noticed a potential gadget and attempted to patch it. However, you can bypass the measures they've taken.

To solve the lab:

1. Find a source that you can use to add arbitrary properties to the global `Object.prototype`.
    
2. Identify a gadget property that allows you to execute arbitrary JavaScript.
    
3. Combine these to call `alert()`.
    

## You can solve this lab manually in your browser, or use [DOM Invader](https://portswigger.net/burp/documentation/desktop/tools/dom-invader) to help you.

This lab is based on real-world vulnerabilities discovered by PortSwigger Research. For more details, check out [Widespread prototype pollution gadgets](https://portswigger.net/research/widespread-prototype-pollution-gadgets) by [Gareth Heyes](https://portswigger.net/research/gareth-heyes).

___

step 1

add into to url `?__proto__[foo]=bar`
go to console type `Object.prototype`
you will see new property added `foo: 'bar'`
it means You've successfully found a prototype pollution source.

![[lab5_object_prototype_foo_bar_property_added.png]]


step 2
observe the code
you will notice `Object.defineProperty()` method to make the `transport_url` unwritable and unconfigurable.

![[lab5_search_logger_configuarable_file.png]]

step 3

![[lab5_value_property.png]]


step 4

test payload `?__proto__[value]=bar`
you will notice in elements tab `<script>` element has been rendered on the page

![[lab5_script_tag_render.png]]


step 5

final payload `?__proto__[value]=data:,alert(1)//`
you will get pop up alert and lab will solved

![[portswigger_wsa/P03_advanced_topics/P24_Prototype-pollution/images/lab5_alert_pop_up.png]]



![[portswigger_wsa/P03_advanced_topics/P24_Prototype-pollution/images/lab5_solved_lab.png]]