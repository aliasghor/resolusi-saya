def faktorial(angka: int) -> int:
  """Sebuah algoritma untuk menghitung faktorial berdasarkan argument angka."""
  if not isinstance(angka,int):
    raise TypeError(f"Error, argument diekspektasikan sebuah int! Tipe data argument anda: {type(angka).__name__}")
  if angka == 1:
    return 1
  return angka * faktorial(angka - 1)

tambah = lambda angka1, angka2: angka1 + angka2

def pangkat(angka1: int, angka2: int) -> int:
  """Sebuah algoritma untuk menghitung pangkat berdasarkan argument angka1 dan angka2."""
  if not isinstance(angka1,int) and not isinstance(angka2,int):
    raise TypeError(f"Error, argument diekspetasikan sebuah tipe data int! Tipe data argument anda: {type(angka1.__name__)} dan {type(angka2).__name__}")
  if angka2 == 1:
    return angka1
  return angka1 * pangkat(angka1,angka2 - 1)

pengurangan = lambda angka1, angka2: angka1 - angka2
