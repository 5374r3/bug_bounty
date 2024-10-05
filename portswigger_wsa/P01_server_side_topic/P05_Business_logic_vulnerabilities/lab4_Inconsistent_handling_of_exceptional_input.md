# Inconsistent handling of exceptional input

## This lab doesn't adequately validate user input. You can exploit a logic flaw in its account registration process to gain access to administrative functionality. To solve the lab, access the admin panel and delete Carlos

---

### step 1 registration page

![screenshot](images/lab4_registation_page.jpg)

### step2

make a string with more than 255 with email address
here 299 words

![screenshot](images/lab4_email_299_charcter.jpg)

After registration successfull

![screenshot](images/lab4_email_address_299_char.jpg)

total number of charcter is 255

![screenshot](images/lab4_email_255_charcter_dispay.jpg)

### step3

make sure @dontwannacry.com comes under 255 then attacker email

![screenshot](images/lab4_dontwanncry_email_255_with_attacker_email.jpg)

then regester open /admin page if admin pannel not visiilbe and delete carlos account solve the problem

![screenshot](images/lab4_email_address_256_character_shown.jpg)
