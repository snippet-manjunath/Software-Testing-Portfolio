
# TEST PLAN – SauceDemo Application

## 1. Project Information

| Field | Details |
|---|---|
| Project Name | Software Testing Portfolio |
| Application Under Test | SauceDemo |
| Application URL | https://www.saucedemo.com/ |
| Testing Type | Functional Testing |
| Testing Approach | Manual and Automation Testing |
| Automation Tool | Selenium WebDriver |
| Programming Language | Python |
| Browser | Google Chrome |

## 2. Objective of Testing

The objective of this testing project is to evaluate the functionality of the SauceDemo online shopping application.

The testing activities aim to:

- Verify user login and authentication.
- Validate product listing and sorting functionality.
- Test shopping cart operations.
- Verify checkout and order completion.
- Identify and document functional defects.
- Validate checkout form input fields.
- Perform automated testing using Selenium WebDriver.

## 3. Scope of Testing

### In Scope

The following modules are included:

1. Login and Authentication
2. Product Listing
3. Product Sorting
4. Add to Cart
5. Remove from Cart
6. Shopping Cart
7. Checkout Process
8. Form Validation
9. Order Confirmation

### Out of Scope

- Payment gateway integration
- Database testing
- Performance and load testing
- Security penetration testing
- Backend API testing

## 4. Testing Strategy

The following testing methods will be used:

### Manual Testing

- Execute test cases manually.
- Verify expected and actual results.
- Identify and document defects.
- Capture screenshots as evidence.
- Record test execution status.

### Automation Testing

- Use Selenium WebDriver with Python.
- Automate login functionality.
- Automate add-to-cart operations.
- Verify cart contents.
- Test product removal.
- Execute automated test cases using Python unittest.
- Validate application behaviour using assertions.
- Record automation execution results.

## 5. Testing Techniques

The following test design techniques are applied:

1. **Equivalence Partitioning**
   - Test valid and invalid login credentials.
   - Test empty and non-empty checkout fields.

2. **Boundary Value Analysis**
   - Test different postal code lengths.
   - Evaluate acceptance of 5-digit, 6-digit and 7-digit inputs.

3. **State Transition Testing**
   - Login and logout.
   - Adding and removing products from cart.
   - Checkout and order confirmation.

4. **Decision Table Testing**
   - Valid and missing checkout details.
   - Different combinations of customer information.

## 6. Test Environment

| Component | Configuration |
|---|---|
| Operating System | macOS |
| Browser | Google Chrome |
| Application | SauceDemo |
| Automation Framework | Selenium WebDriver |
| Programming Language | Python 3.13.11 |
| IDE / Editor | Terminal and Nano |
| Version Control | GitHub |

## 7. Entry Criteria

Testing can begin when:

- Application is accessible.
- Test scenarios are identified.
- Valid and invalid test credentials are available.
- Browser and testing environment are ready.
- Required testing tools are installed.

## 8. Exit Criteria

Testing is considered complete when:

- Planned test cases have been executed or their pending status documented.
- Actual results are recorded.
- Identified defects are documented.
- Automation test execution results are recorded.
- Screenshots and supporting evidence are collected.
- Test summary report is prepared.

## 9. Roles and Responsibilities

| Role | Responsibility |
|---|---|
| Tester | Design and execute test cases |
| Tester | Identify and report defects |
| Tester | Perform Selenium automation |
| Tester | Capture testing evidence |
| Tester | Prepare test documentation and reports |

## 10. Test Schedule

| Activity | Status |
|---|---|
| Test Planning | Completed |
| Test Case Design | Completed |
| Manual Test Execution | Completed |
| Defect Reporting | Completed |
| Selenium Automation | Completed |
| Final Test Reporting | Completed |

## 11. Risks and Limitations

- Application behaviour may vary during testing.
- Temporary browser or network issues may affect execution.
- Some defects may not be consistently reproducible.
- Testing is limited to the selected application modules.
- Payment gateway and performance testing are not included.
- Postal code format validation is an additional testing expectation and not necessarily a built-in SauceDemo requirement.

## 12. Deliverables

The following deliverables are included:

1. Test Plan
2. Test Case Design
3. Test Execution Results
4. Defect Reports
5. Selenium Automation Script
6. Automation Test Results
7. Screenshots and Evidence
8. Final Test Summary Report

## 13. Conclusion

This test plan defines the scope, objectives, strategy, environment and activities for testing the SauceDemo application.

Both manual and automation testing approaches are used to evaluate application functionality and identify potential defects.

The project provides practical experience in test planning, test case design, manual test execution, defect reporting, automation testing and final test reporting.
