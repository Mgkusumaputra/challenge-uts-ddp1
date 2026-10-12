# Jejak Loop

**Difficulty:** Medium  
**Points:** 20  
**Estimated time:** 15 minutes  
**Topics:** Loops, modulo, tracing

## Problem Statement

Diberikan N bilangan. Untuk setiap bilangan, cetak `GENAP` jika genap dan `GANJIL` jika ganjil. Output harus mempertahankan urutan input, satu hasil per baris.

## Input Format

Baris pertama N. Berikutnya N bilangan, bisa dipisahkan spasi atau baris baru.

## Output Format

N baris, masing-masing `GENAP` atau `GANJIL`.

## Constraints

1 ≤ N ≤ 100000; -10^9 ≤ angka ≤ 10^9.

## Sample Input 0
```text
4
2 7 0 -3
```

## Sample Output 0
```text
GENAP
GANJIL
GENAP
GANJIL
```

## Explanation 0

Modulo tetap dapat dipakai untuk bilangan negatif; sisa 0 berarti genap.

## HackerRank setup notes
- Language: Python 3
- Use standard input/output. Do not print prompts or extra explanatory text.
- Keep the reference solution and additional tests private.
