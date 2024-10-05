# Source code disclosure via backup files

## This lab leaks its source code via backup files in a hidden directory. To solve the lab, identify and submit the database password, which is hard-coded in the leaked source code.

---

### step 1

open lap
add _/robots.txt_ at the end of url
User-agent: \*
Disallow: /backup
open /backup

### step2

send to reapter
ConnectionBuilder connectionBuilder = ConnectionBuilder.from(
"org.postgresql.Driver",
"postgresql",
"localhost",
5432,
"postgres",
"postgres",
"\*831ilmxnnipuf9hxwuz5e1cbsm6jls9e\*"
).withAutoCommit();
submit the password
