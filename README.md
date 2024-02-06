# Test for HugMarket

Based on email from Jana Derichova:
>Napiš funkci: def solution(A); která, má pole A s N celými čísly a vrací nejmenší kladné celé číslo (větší než 0), které se v poli A nevyskytuje.
>Například, pro pole A = [1, 3, 6, 4, 1, 2] by funkce měla vrátit 5.
> 
>Pro pole A = [1, 2, 3] by měla funkce vrátit 4.
> 
>Pro pole A = [-1, -3] by měla funkce vrátit 1.
> 
>Napiš efektivní algoritmus pro následující předpoklady:
>N je celé číslo v rozmezí [1..100 000];
>
>každý prvek pole A je celé číslo v rozmezí [-1 000 000..1 000 000].

I created two functions one *slow* (using list) and second *fast* (using dictionary)

## Executing program
Simply run `python3 main.py --list {whatever list of numbers}`

## Executing test
1. Create virtual environment `python3 -m venv venv`
2. Source your virtual environment `source venv/bin/activate`
3. Execute to install dependencies:
    ```bash
   pip install -r requirements.txt
   ```
4. Run tests with: `pytest -s`

### To run individual TestClasses
Run `pytest -s test_solution.py::{TestFastSolution|TestSlowSolution}`

# Have a nice day and happy hacking 😎!!
