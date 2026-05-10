# Regular Expressions

## Description

This project covers the fundamentals of regular expressions (regex) using Ruby. Regular expressions are patterns used to match character combinations in strings. In Ruby, regex patterns are built with the `Regexp` class and used with methods like `match`, `=~`, and `scan`.

All scripts accept one argument and pass it to a regular expression matching method, printing matches to standard output.

## Requirements

- Ruby 2.1.5 or higher
- All scripts are executable
- Scripts must pass the argument to a regular expression method (not use `if/else` or other logic)

## Project Structure

```
alu-scripting/
└── regular_expressions/
    └── 0-simply_match_school.rb
```

## Tasks

### 0. Simply matching School

**File:** `regular_expressions/0-simply_match_school.rb`

Matches the word `School` in the given argument using a Ruby regular expression.

**Usage:**
```bash
./0-simply_match_school.rb School | cat -e
School$

./0-simply_match_school.rb "Best School" | cat -e
School$

./0-simply_match_school.rb "School Best School" | cat -e
SchoolSchool$

./0-simply_match_school.rb "Grace Hopper" | cat -e
$
```

## How to Run

Make the script executable and pass a string argument:

```bash
chmod +x regular_expressions/0-simply_match_school.rb
./regular_expressions/0-simply_match_school.rb "your string here"
```

## Repository

- **GitHub repository:** alu-scripting
- **Directory:** regular_expressions
- **Author:** Orion Kabeza
