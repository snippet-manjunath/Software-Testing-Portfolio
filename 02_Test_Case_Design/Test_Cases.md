# Test Case Design – SauceDemo

**Application:** Online Shopping Application  
**Testing Type:** Functional Testing  
**Tool:** Google Chrome  
**Project:** Software Testing Portfolio

## 1. Login Module

| ID | Test Scenario | Expected Result | Status |
|---|---|---|---|
| TC01 | Login with valid credentials | Login successful | Pending |
| TC02 | Login with invalid password | Error message displayed | Pending |
| TC03 | Login with empty username and password | Validation/error displayed | Pending |
| TC04 | Login with locked-out user | Access denied with error | Pending |

## 2. Product Module

| ID | Test Scenario | Expected Result | Status |
|---|---|---|---|
| TC05 | View available products | Products displayed | Pending |
| TC06 | Sort products by price low to high | Prices arranged in ascending order | Pending |
| TC07 | Sort products by price high to low | Prices arranged in descending order | Pending |

## 3. Shopping Cart Module

| ID | Test Scenario | Expected Result | Status |
|---|---|---|---|
| TC09 | Add product to cart | Product added successfully | Pending |
| TC10 | Remove product from cart | Product removed successfully | Pending |
| TC11 | Add multiple products | All selected products displayed | Pending |

## 4. Checkout Module

| ID | Test Scenario | Expected Result | Status |
|---|---|---|---|
| TC12 | Checkout with valid customer details | Continue to overview page | Pending |
| TC13 | Checkout with missing first name | Validation message displayed | Pending |
| TC14 | Checkout with missing last name | Validation message displayed | Pending |
| TC15 | Checkout with missing postal code | Validation message displayed | Pending |
| TC08 | Click Finish on checkout overview | Order confirmation displayed | Fail – Observed, pending verification |

## 5. Order Module

| ID | Test Scenario | Expected Result | Status |
|---|---|---|---|
| TC16 | Complete an order | Order confirmation displayed | Pending |
| TC17 | Return to products after order | Products page displayed | Pending |
| TC18 | Verify cart after checkout | Cart reflects completed order | Pending |

## Testing Techniques

1. Equivalence Partitioning – Valid and invalid login credentials.
2. Boundary Value Analysis – Checkout input fields and quantity limits, where applicable.
3. State Transition Testing – Login, cart and checkout flow.
4. Decision Table Testing – Combinations of valid and missing checkout details.

**Note:** Pending means not yet executed. Update actual results and status only after performing each test.
