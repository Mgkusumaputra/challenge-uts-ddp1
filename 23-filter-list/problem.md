# Filter dan Balik

**Difficulty:** Hard  
**Points:** 30  
**Estimated time:** 25 minutes  
**Topics:** Lists, loops, conditionals, slicing

## Problem Statement

Diberikan N bilangan bulat. Ambil hanya bilangan positif genap, hilangkan duplikat sambil mempertahankan kemunculan pertama, lalu cetak urutan hasil secara terbalik. Jika tidak ada bilangan yang memenuhi, cetak `KOSONG`.

## Input Format

Baris pertama N. Baris kedua N bilangan.

## Output Format

Cetak hasil dipisahkan spasi atau `KOSONG`.

## Constraints

1 ≤ N ≤ 5000; -10^9 ≤ angka ≤ 10^9.

## Sample Input 0
```text
8
2 4 2 -6 7 8 4 0
```

## Sample Output 0
```text
8 4 2
```

## Explanation 0

Saring, deduplikasi berdasarkan kemunculan pertama, lalu balik urutan akhir.

## HackerRank setup notes
- Language: Python 3
- Use standard input/output. Do not print prompts or extra explanatory text.
- Keep the reference solution and additional tests private.
