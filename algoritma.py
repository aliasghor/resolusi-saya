# Sebuah algoritma untuk menghitung faktorial berdasarkan num
def faktorial(num: int) -> int:
  if not isinstance(num,int):
    raise ValueError(f"Error, argument diekspektasikan sebuah int! Tipe data argument anda: {type(num).__name__}")
  if num == 1:
    return 1
  return num * faktorial(num - 1)
