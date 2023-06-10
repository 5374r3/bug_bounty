# Insufficient workflow validation

## This lab makes flawed assumptions about the sequence of events in the purchasing workflow. To solve the lab, exploit this flaw to buy a "Lightweight l33t leather jacket".

## You can log in to your own account using the following credentials: `wiener:peter`

### step1

login user id and password order any item with below credit balance
place the order
go to burpsuit and check the page confirm order

```javascript
GET /cart/order-confirmation?order-confirmed=true HTTP/1.1
```

notice here `order-confirmed=true`

### step2

order "Lightweight l33t leather jacket" and place the order and intercept

```javascript
POST /cart/checkout HTTP/1.1
```

change this to

```javascript
GET /cart/order-confirmation?order-confirmed=true HTTP/1.1
```

and forward and intercept off
