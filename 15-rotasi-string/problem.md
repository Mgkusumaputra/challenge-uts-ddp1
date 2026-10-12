# Rotasi String

**Difficulty:** Medium  
**Points:** 20  
**Estimated time:** 18 minutes  
**Topics:** Strings, modulo, slicing

## Problem Statement

Diberikan string S dan bilangan bulat K non-negatif. Lakukan rotasi ke kiri sebanyak K posisi. Jika K lebih panjang dari string, rotasi tetap berlaku secara siklik.

## Input Format

Baris pertama string S. Baris kedua K.

## Output Format

String setelah rotasi kiri.

## Constraints

1 ≤ panjang S ≤ 100000; 0 ≤ K ≤ 10^9.

## Sample Input 0
```text
HACKERRANK
3
```

## Sample Output 0
```text
KERRANKHAC
```

## Explanation 0

Kurangi K modulo panjang string agar jumlah rotasi berada dalam rentang yang diperlukan.

## HackerRank setup notes
- Language: Python 3
- Use standard input/output. Do not print prompts or extra explanatory text.
- Keep the reference solution and additional tests private.
