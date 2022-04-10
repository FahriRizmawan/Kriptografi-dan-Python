ALHPABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


# di dalam fungsi main terdapat variabel pesan, kunci dan mode sebelum program dijalankan
# pada modeSaya anda bisa menetapkan apakah program akan melakukan enkripsi atau dekripsi
def main():
    pesanSaya = """Nim: 19102138, nama: Fahri Rizmawan, isi pesan: ini adalah tugas dua kriptografi kelas TI dua"""
    kunciSaya = 'Informatika19'
    #untuk melakukan proses enkripsi atau dekripsi
    Proses = 'enkripsi'

    if Proses == 'enkripsi':
        ubah = enkripsiPesan(kunciSaya, pesanSaya)
    elif Proses == 'dekripsi':
        ubah = dekripsiPesan(kunciSaya, pesanSaya)

    print('%sed pesan : ' % (Proses.title()))
    print(ubah)
    print()


# pada bagian ini menjelaskan bagaimana enkripsi berjalan
def enkripsiPesan(kunci, pesan):
    return ubahPesan(kunci, pesan, 'enkripsi')


# pada bagian ini menjelaskan bagaimana dekripsi berjalan
def dekripsiPesan(kunci, pesan):
    return ubahPesan(kunci, pesan, 'dekripsi')


def ubahPesan(kunci, pesan, mode):
    ubah = []
    # menyimpan pesan enkripsi dan dekripsi

    kunciIndex = 0
    kunci = kunci.upper()

    for symbol in pesan:
        # akan dilakukan pada seluruh karakter dalam pesan
        nomor = ALHPABET.find(symbol.upper())
        if nomor != -1:  # -1 berarti symbol.upper() tidak ditemukan didalam HURUF
            if mode == 'enkripsi':
                nomor += ALHPABET.find(kunci[kunciIndex])  # tambahkan jika dienkripsi
            elif mode == 'dekripsi':
                nomor -= ALHPABET.find(kunci[kunciIndex])  # kurangi jika melakukan dekripsi

            nomor %= len(ALHPABET)

            # tambahkan pada hasil symbol enkrip/dekrip yang sudah diubahkan
            if symbol.isupper():
                ubah.append(ALHPABET[nomor])
            elif symbol.islower():
                ubah.append(ALHPABET[nomor].lower())

            kunciIndex += 1
            # ubah kunci yang akan dipakai selanjutnya
            if kunciIndex == len(kunci):
                kunciIndex = 0

        else:
            # symbol tidak berada pada Alphabet, maka tambahkan hal tersebut dan ubahkan
            ubah.append(symbol)

    return ''.join(ubah)

# panggil fungsi main untuk menjalankan programnya
if __name__ == '__main__':
    main()
