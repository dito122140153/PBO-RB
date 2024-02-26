class Lagu:
    def __init__(self, penyanyi, judul, tahun):
        self.__penyanyi = penyanyi
        self.__judul = judul
        self.__tahun = tahun

    def get_penyanyi(self):
        return self.__penyanyi

    def get_judul(self):
        return self.__judul

    def get_tahun(self):
        return self.__tahun


class Playlist:
    def __init__(self, daftar_lagu):
        self.__daftar_lagu = daftar_lagu
        self.__lagu_yang_dimainkan_saat_ini = None

    def putar_lagu_pertama(self):
        self.__lagu_yang_dimainkan_saat_ini = 0

    def putar_lagu_terakhir(self):
        self.__lagu_yang_dimainkan_saat_ini = len(self.__daftar_lagu) - 1

    def putar(self):
        if self.__lagu_yang_dimainkan_saat_ini is not None:
            lagu = self.__daftar_lagu[self.__lagu_yang_dimainkan_saat_ini]
            print("Memutar:", lagu.get_judul(), "oleh", lagu.get_penyanyi(), "-", lagu.get_tahun())
        else:
            print("Tidak ada lagu yang diputar.")

    def putar_lagu_selanjutnya(self):
        if self.__lagu_yang_dimainkan_saat_ini is not None:
            self.__lagu_yang_dimainkan_saat_ini = (self.__lagu_yang_dimainkan_saat_ini + 1) % len(self.__daftar_lagu)

    def putar_lagu_sebelumnya(self):
        if self.__lagu_yang_dimainkan_saat_ini is not None:
            self.__lagu_yang_dimainkan_saat_ini = (self.__lagu_yang_dimainkan_saat_ini - 1) % len(self.__daftar_lagu)

    def set_lagu(self, index):
        if 0 <= index < len(self.__daftar_lagu):
            self.__lagu_yang_dimainkan_saat_ini = index

    def mencetak_lagu(self):
        if self.__lagu_yang_dimainkan_saat_ini is not None:
            lagu = self.__daftar_lagu[self.__lagu_yang_dimainkan_saat_ini]
            print("Lagu yang sedang diputar:", lagu.get_judul(), "oleh", lagu.get_penyanyi(), "-", lagu.get_tahun())
        else:
            print("Tidak ada lagu yang sedang diputar.")


# Contoh penggunaan kelas Playlist dan Lagu
lagu1 = Lagu("Travis Scott", "MY EYES", 2024)
lagu2 = Lagu("DAY6", "Shoot Me", 2021)
lagu3 = Lagu("Natori", "Overdose", 2022)

daftar_lagu = [lagu1, lagu2, lagu3]

playlist = Playlist(daftar_lagu)
playlist.putar_lagu_pertama()
playlist.putar()

playlist.putar_lagu_selanjutnya()
playlist.putar()

playlist.putar_lagu_terakhir()
playlist.putar()

playlist.putar_lagu_sebelumnya()
playlist.putar()

playlist.set_lagu(1)
playlist.mencetak_lagu()
