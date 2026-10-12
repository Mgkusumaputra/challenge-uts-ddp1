# Tarif Parkir

**Difficulty:** Easy  
**Points:** 10  
**Estimated time:** 12 minutes  
**Topics:** Conditionals, arithmetic

## Problem Statement

Tarif parkir adalah Rp2.000 untuk jam pertama atau bagian darinya, lalu Rp1.000 untuk setiap jam berikutnya atau bagian darinya. Diberikan lama parkir dalam menit, hitung tarif total. Minimal lama parkir 1 menit.

## Input Format

Satu bilangan bulat m, lama parkir dalam menit.

## Output Format

Satu bilangan bulat tarif dalam rupiah.

## Constraints

1 ≤ m ≤ 1440

## Sample Input 0
```text
125
```

## Sample Output 0
```text
4000
```

## Explanation 0

Pembulatan ke atas bisa dilakukan dengan `(m + 59) // 60`.

## HackerRank setup notes
- Language: Python 3
- Use standard input/output. Do not print prompts or extra explanatory text.
- Keep the reference solution and additional tests private.
