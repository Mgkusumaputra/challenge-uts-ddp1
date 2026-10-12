# Pemroses Log Aktivitas

**Difficulty:** Hard  
**Points:** 30  
**Estimated time:** 30 minutes  
**Topics:** Strings, lists, functions, conditionals, loops

## Problem Statement

Sebuah sistem mencatat N baris log dengan format `NAMA STATUS DURASI`, dipisahkan spasi. STATUS bernilai `OK` atau `FAIL`; DURASI integer non-negatif. Hitung jumlah log `OK` dan total durasi dari log `OK` saja. Nama tidak mengandung spasi.

## Input Format

Baris pertama N, diikuti N baris log.

## Output Format

Cetak `jumlah_ok total_durasi_ok`.

## Constraints

1 ≤ N ≤ 100000; 0 ≤ durasi ≤ 10^6.

## Sample Input 0
```text
4
api OK 12
db FAIL 20
web OK 8
cache OK 5
```

## Sample Output 0
```text
3 25
```

## Explanation 0

Gunakan fungsi untuk memisahkan parsing satu baris log dari perhitungan agregat.

## HackerRank setup notes
- Language: Python 3
- Use standard input/output. Do not print prompts or extra explanatory text.
- Keep the reference solution and additional tests private.
