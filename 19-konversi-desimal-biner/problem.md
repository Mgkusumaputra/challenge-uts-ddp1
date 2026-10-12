# Desimal ke Biner

**Difficulty:** Medium  
**Points:** 20  
**Estimated time:** 18 minutes  
**Topics:** Number systems, loops, strings

## Problem Statement

Diberikan bilangan bulat non-negatif N. Cetak representasi biner tanpa awalan `0b`. Jika N adalah 0, output harus `0`. Jangan menggunakan `bin()`.

## Input Format

Satu bilangan bulat N.

## Output Format

Representasi biner N.

## Constraints

0 ≤ N ≤ 10^9.

## Sample Input 0
```text
13
```

## Sample Output 0
```text
1101
```

## Explanation 0

Ambil sisa pembagian dua berulang kali. Sisa muncul dari bit paling kanan, jadi tambahkan ke depan.

## HackerRank setup notes
- Language: Python 3
- Use standard input/output. Do not print prompts or extra explanatory text.
- Keep the reference solution and additional tests private.
