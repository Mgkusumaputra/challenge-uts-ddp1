# Kasir Tahan Error

**Difficulty:** Hard  
**Points:** 30  
**Estimated time:** 25 minutes  
**Topics:** Exception handling, loops, conditionals

## Problem Statement

Program menerima N transaksi. Setiap transaksi berupa token harga. Jika token bisa dikonversi menjadi integer non-negatif, tambahkan ke total. Token negatif atau bukan integer dianggap tidak valid dan diabaikan. Cetak total transaksi valid.

## Input Format

Baris pertama N. Baris kedua berisi N token.

## Output Format

Cetak total harga valid.

## Constraints

1 ≤ N ≤ 100000.

## Sample Input 0
```text
6
100 25 abc -10 5 2.5
```

## Sample Output 0
```text
130
```

## Explanation 0

Konversi dan validasi tanda adalah dua pemeriksaan berbeda.

## HackerRank setup notes
- Language: Python 3
- Use standard input/output. Do not print prompts or extra explanatory text.
- Keep the reference solution and additional tests private.
