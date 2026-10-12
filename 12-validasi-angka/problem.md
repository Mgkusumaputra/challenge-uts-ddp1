# Validasi Input Angka

**Difficulty:** Medium  
**Points:** 20  
**Estimated time:** 15 minutes  
**Topics:** Exception handling, loops

## Problem Statement

Diberikan N token teks. Untuk setiap token, coba ubah menjadi bilangan bulat. Cetak jumlah token yang berhasil dikonversi menjadi integer. Token yang gagal tidak dihitung.

## Input Format

Baris pertama N, baris kedua berisi N token dipisahkan spasi.

## Output Format

Cetak jumlah token valid sebagai integer.

## Constraints

1 ≤ N ≤ 10000. Token tidak mengandung spasi.

## Sample Input 0
```text
5
12 abc -3 4.2 0
```

## Sample Output 0
```text
3
```

## Explanation 0

`int("4.2")` memunculkan ValueError, sedangkan `int("-3")` valid.

## HackerRank setup notes
- Language: Python 3
- Use standard input/output. Do not print prompts or extra explanatory text.
- Keep the reference solution and additional tests private.
