
# Final Software Testing Summary Report

## 1. Project Overview

**Application:** SauceDemo  
**Project Type:** Software Testing Portfolio  
**Testing Approach:** Manual Testing and Automation Testing  
**Automation Tool:** Selenium WebDriver  
**Programming Language:** Python  

## 2. Testing Scope

The following application functionalities were tested:

- User Login and Authentication
- Product Listing
- Product Sorting
- Add to Cart
- Remove from Cart
- Shopping Cart Verification
- Checkout Process
- Form Validation
- Order Completion

## 3. Testing Techniques Used

The following testing techniques were applied:

1. Equivalence Partitioning
2. Boundary Value Analysis
3. State Transition Testing
4. Decision Table Testing

## 4. Manual Testing Summary

A total of 21 manual test cases were designed and executed.

| Status | Number of Test Cases |
|---|---:|
| Passed | 15 |
| Failed | 4 |
| Needs Verification | 2 |
| Total | 21 |

### Major Findings

1. Price sorting in ascending order did not work correctly.
2. Price sorting in descending order did not work correctly.
3. Checkout continued even when the Last Name field was empty.
4. Remove button on the Products page did not remove the product.

### Observations Requiring Verification

- Finish button initially appeared unresponsive, but a subsequent order was completed successfully.
- Postal code boundary testing accepted different input formats. Indian six-digit PIN validation was an additional test expectation, not a confirmed SauceDemo requirement.

## 5. Automation Testing Summary

Automation was performed using Selenium WebDriver with Python.

| Test ID | Test Case | Result |
|---|---|---|
| AT01 | Valid Login | PASS |
| AT02 | Invalid Login | PASS |
| AT03 | Add Product to Cart | PASS |
| AT04 | Verify Cart | PASS |
| AT05 | Remove Product from Cart | PASS |

### Automation Execution Summary

- Total Automated Tests: 5
- Passed: 5
- Failed: 0
- Execution Time: 9.769 seconds
- Automation Result: PASS

### Execution Command

`python -m unittest -v saucedemo_automation.py`

## 6. Defect Summary

The manual testing process identified the following major issues:

| Defect | Description | Status |
|---|---|---|
| BUG01 | Price sorting issue | Observed |
| BUG02 | Finish button issue | Needs verification |
| BUG03 | Sorting low to high issue | Observed |
| BUG04 | Sorting high to low issue | Observed |
| BUG05 | Remove button issue on Products page | Observed |
| BUG06 | Last Name validation missing | Observed |

Note: BUG01 should only be included if a corresponding defect report exists. Sorting issues may be grouped into one defect if they share the same root cause.

## 7. Conclusion

The SauceDemo application was tested using both manual and automation testing approaches.

A total of 21 manual test cases were evaluated, and five automated test cases were executed successfully using Selenium WebDriver.

The testing process helped identify functional issues related to product sorting, cart operations, and checkout form validation.

This project provided practical experience in test planning, test case design, test execution, defect reporting, and browser automation.

## 8. Tools and Technologies

- SauceDemo
- Selenium WebDriver
- Python 3.13.11
- Google Chrome
- GitHub
- Markdown
