# Analisis Kata

**Difficulty:** Hard  
**Points:** 30  
**Estimated time:** 25 minutes  
**Topics:** Strings, lists, loops, functions

## Problem Statement

Diberikan sebuah kalimat. Abaikan kapitalisasi dan tanda baca sederhana `.,!?;:`. Temukan kata terpanjang. Jika ada beberapa kata dengan panjang sama, pilih yang muncul paling awal. Cetak kata tersebut dalam huruf kecil.

## Input Format

Satu baris kalimat yang berisi setidaknya satu huruf atau angka.

## Output Format

Cetak kata terpanjang dalam huruf kecil.

## Constraints

Panjang kalimat ≤ 100000.

## Sample Input 0
```text
Python itu seru, belajar Python!
```

## Sample Output 0
```text
belajar
```

## Explanation 0

Gunakan `>` bukan `>=` agar kata pertama tetap dipilih saat panjangnya seri.

## HackerRank setup notes
- Language: Python 3
- Use standard input/output. Do not print prompts or extra explanatory text.
- Keep the reference solution and additional tests private.
