# Issue Documentation Table
| Issue                                 | Type            | Line(s) | Description                                            | Fix Approach                                                    |
|--------------------------------------|-----------------|---------|--------------------------------------------------------|-----------------------------------------------------------------|
| Mutable default argument (`logs=[]`) | Bug             | 9       | The default list is shared across function calls       | ✅ Fixed: Changed default to `None` and initialized inside function |
| Bare `except:` clause                 | Bug             | —       | Not present in current code                            | ✅ Already resolved: Specific `except KeyError` used             |
| No input validation                   | Quality         | 18      | `add_item(123, "ten")` accepts invalid types           | ✅ Fixed: Type checks added for `item` (str) and `qty` (int)     |
| Dangerous function `eval()`          | Security        | —       | Not present in current code                            | ✅ No issue: `eval()` is not used                               |
| Files not opened with context manager| Maintainability | 62, 67  | Files opened manually without `with` block             | ✅ Fixed: `with open(...)` used for both load and save           |
| Missing logging configuration        | Quality         | 7       | Using print instead of logging, inconsistent reporting | ✅ Fixed: Logging configured with format and level               |
| Global variable usage (`stock_data`) | Style           | Global  | `stock_data` modified globally                         | ✅ Improved: Avoided `global` keyword; updated via `.clear()` and `.update()` |

# Reflection
## 1. Which issues were the easiest to fix, and which were the hardest? Why?
- Easiest to fix: Missing docstrings (C0116) were the simplest to resolve. They only required adding a brief, descriptive comment under each function, which was straightforward and didn’t affect logic or structure.
- Hardest to fix: Avoiding the global statement (W0603) was more challenging. It required refactoring the load_data() function to return data and updating the main() function to modify the global dictionary without explicitly declaring it. This involved deeper understanding of scope and side effects

## 2. Did the static analysis tools report any false positives? If so, describe one example.
- No clear false positives were observed during this lab. All reported issues were valid and aligned with best practices. However, the line number reported for missing docstrings occasionally pointed to the end of the previous function, which could be misleading at first glance

## 3. How would you integrate static analysis tools into your actual software development workflow?
- Local development: Run tools like pylint, flake8, or bandit as part of pre-commit hooks to catch issues early.
- Continuous Integration (CI): Integrate static analysis into CI pipelines (e.g., GitHub Actions, GitLab CI) to automatically scan code on every push or pull request.
- IDE integration: Use editor plugins to get real-time feedback while coding, reducing context-switching and improving code hygiene continuously.

## 4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?
- Code quality: Improved modularity and reduced reliance on global state, making the code easier to maintain and test.
- Readability: Clearer documentation through consistent docstrings and logging made the code more understandable for future contributors.
- Robustness: Safer handling of file operations and input validation reduced the risk of runtime errors and improved fault tolerance.
