# Inconsistent handling of exceptional input

## This lab doesn't adequately validate user input. You can exploit a logic flaw in its account registration process to gain access to administrative functionality. To solve the lab, access the admin panel and delete Carlos

### step1 registration page

![screenshot](./images/lab4_registation_page.png)

### step2

make a string with more than 255 with email address
here 299 words

![screenshot](./images/lab4_email_299_charcter.png)

After registration successfull

![screenshot](./images/lab4_email_address_299_char.png)

total number of charcter is 255

![screenshot](./images/lab4_email_255_charcter_dispay.png)

### step3

make sure @dontwannacry.com comes under 255 then attacker email

![screenshot](./images/lab4_dontwanncry_email_255_with_attacker_email.png)

then regester open /admin page if admin pannel not visiilbe and delete carlos account solve the problem

![screenshot](./images/lab4_email_address_256_character_shown.png)
