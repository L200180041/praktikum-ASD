#No 14
def formatRupiah(n):
    x = '{:,}'.format(n).replace(',', '.')
    return "Rp " + x
