
# Final Software Testing Summary Report

## 1. Project Overview

**Application:** SauceDemo  
**Project Type:** Software Testing Portfolio  
**Application URL:** https://www.saucedemo.com/  
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

A total of 21 test cases were designed and evaluated.

| Status | Number of Test Cases |
|---|---:|
| Passed | 14 |
| Failed | 4 |
| Needs Verification | 2 |
| Pending | 1 |
| Total | 21 |

### Major Findings

1. Price sorting in ascending order displayed a Backtrace error.
2. Price sorting in descending order displayed a Backtrace error.
3. Checkout continued even when the Last Name field was empty.
4. Remove button on the Products page appeared unresponsive.

### Observations Requiring Verification

- The Finish button initially appeared unresponsive, but a subsequent order was completed successfully.
- Postal code boundary testing accepted different input formats. Indian six-digit PIN validation was an additional testing requirement, not a confirmed SauceDemo requirement.

### Manual Testing Notes

- TC04 was covered by TC20, which successfully verified locked-out user access.
- TC08 requires further verification because the Finish button worked during a subsequent test.
- TC21 requires further verification because postal code format expectations were additional requirements.

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

The manual testing process identified the following issues:

| Defect ID | Description | Status |
|---|---|---|
| BUG02 | Finish button appeared unresponsive initially | Needs Verification |
| BUG03 | Price sorting low to high | Observed |
| BUG04 | Price sorting high to low | Observed |
| BUG05 | Remove button issue on Products page | Provisional |
| BUG06 | Last Name validation missing | Observed |

**Note:** Postal code format testing is an additional requirement-based finding and is not classified as a confirmed application defect.

## 7. Conclusion

The SauceDemo application was tested using both manual and automation testing approaches.

A total of 21 manual test cases were evaluated. Fourteen passed, four failed, two require further verification and one remains pending.

Five automated test cases were executed successfully using Selenium WebDriver with Python.

The testing process helped identify potential functional issues related to product sorting, cart operations and checkout form validation.

This project provided practical experience in test planning, test case design, test execution, defect reporting, boundary value analysis and browser automation.

## 8. Tools and Technologies

- SauceDemo
- Selenium WebDriver
- Python 3.13.11
- Google Chrome
- GitHub
- Markdown
