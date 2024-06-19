def faktorial(angka: int) -> int:
  """Sebuah algoritma untuk menghitung faktorial berdasarkan argument angka."""
  if not isinstance(num,int):
    raise ValueError(f"Error, argument diekspektasikan sebuah int! Tipe data argument anda: {type(num).__name__}")
  if num == 1:
    return 1
  return num * faktorial(num - 1)

def tambah(angka: int) -> int:
  """Sebuah algoritma untuk menghitung tambah berdasarkan argument angka."""
  if not isinstance(angka,int):
    raise ValueError(f"Error, argument diekspektasikan sebuah int! Tipe data argument anda: {type(angka).__name__}")
  if angka == 0:
    return 0
  return num + tambah(angka - 1)
