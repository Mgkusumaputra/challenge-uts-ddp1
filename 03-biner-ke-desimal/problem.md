# Dari Biner ke Desimal

**Difficulty:** Easy  
**Points:** 10  
**Estimated time:** 12 minutes  
**Topics:** Number systems, strings, loops

## Problem Statement

Diberikan string yang merepresentasikan bilangan biner non-negatif. Hitung nilai desimalnya tanpa memakai `int(teks, 2)`.

## Input Format

Satu string biner yang hanya berisi karakter `0` dan `1`.

## Output Format

Cetak nilai desimalnya.

## Constraints

Panjang string 1 sampai 30.

## Sample Input 0
```text
101101
```

## Sample Output 0
```text
45
```

## Explanation 0

Setiap digit baru menggeser nilai sebelumnya satu posisi biner ke kiri, lalu menambahkan digit.

## HackerRank setup notes
- Language: Python 3
- Use standard input/output. Do not print prompts or extra explanatory text.
- Keep the reference solution and additional tests private.
