
from this import d
from IGame import IGame
from Tile import Tile
from Matrix import Matrix
import random
import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# By years
c_2021 = (165, 15, 21)
c_2020_2019_2017_2016_2015 = (103, 0, 13)
c_2018 = (165, 15, 21)
c_2014_2013_2010 = (203, 24, 29)
c_2012_2011_2009_2003_2002_1998 = (239, 59, 44)
c_2008_2004_2001 = (251, 106, 74)
c_2000_1999_1996_1991_1988_1981 = (252, 187, 161)
c_1997_1995_1990 = (252, 146, 114)
c_1994_1993_1989_1987_1983_1980 = (254, 224, 210)
c_1992_1986_1979_1955_1946_1942 = (222, 235, 247)
c_1985_1984_1982_1975_1971_1963_1960_1954_1954_1953_1947_1945_1944_1943_1940_1939 = (198, 219, 239)
c_1978_1976_1973_1970_1968_1967_1951_1957_1938_1937_1936_1934_1930_1932 = (107, 174, 214)
c_1977_1974_1972_1969_1965_1964_1962_1961_1959_1956_1950_1949_1948_1941_1933_1928 = (158, 202, 225)
c_1966_1958_1952_1929_1927_1926_1923_1922 = (66, 146, 198)
c_1935_1931_1925_1924 = (33, 113, 181)


class Intro(IGame):
    def __init__(self):
        self.size = 13
        self.time = 0
        self.repeat = 0

        self.first_sqr = [[0,0], [0,1], [0,2], [0,3], [0,4], [0,5],[0,6], [0,7], [0,8], [0,9], [0,10], [0,11], [0,12],
                    [1,0], [2,0], [3,0], [4,0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0], [11, 0], [12, 0],
                    [12, 1], [12, 2], [12, 3], [12, 4], [12, 5], [12, 6], [12, 7], [12, 8], [12, 9], [12, 10], [12, 11], [12, 12],
                    [1, 12], [2, 12], [3, 12], [4, 12], [5, 12], [6, 12], [7, 12], [8, 12], [9, 12], [10, 12], [11, 12]]

        self.second_sqr = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1], [11, 1],
                    [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [1, 11],
                    [2, 11], [3, 11], [4, 11], [5, 11], [6, 11], [7, 11], [8, 11], [9, 11], [10, 11], [11, 11],
                    [11, 2], [11, 3], [11, 4], [11, 5], [11, 6], [11, 7], [11, 8], [11, 9], [11, 10]]

        self.third_sqr = [[2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [2, 10],
                    [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2], [9, 2], [10, 2],
                    [10, 3], [10, 4], [10, 5], [10, 6], [10, 7], [10, 8], [10, 9], [10, 10],
                    [3, 10], [4, 10], [5, 10], [6, 10], [7, 10], [8, 10], [9, 10]]
        
        self.forth_sqr = [[3, 3], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8], [3, 9],
                    [4, 3], [5, 3], [6, 3], [7, 3], [8, 3], [9, 3],
                    [4, 9], [5, 9], [6, 9], [7, 9], [8, 9], [9, 9],
                    [9, 3], [9, 4], [9, 5], [9, 6], [9, 7], [9, 8]]
        
        self.fifth_sqr = [[4, 4], [4, 5], [4, 6], [4, 7], [4, 8],
                    [8, 4], [8, 5], [8, 6], [8, 7], [8, 8],
                    [5, 4], [6, 4], [7, 4],
                    [5, 8], [6, 8], [7, 8]]

        self.sixth_sqr = [[5, 5], [5, 6], [5, 7], 
                    [7, 5], [7, 6], [7, 7], 
                    [6, 7], [6, 5]]
        
        self.seventh_sqr = [[6,6]]

        self.footprint = [[2, 2], [2, 3], [2, 4], [3, 2], [3, 4], [4, 2], [4, 3], [4, 4],
                        [2, 8], [2, 9], [2, 10], [3, 8], [3, 10], [4, 8], [4, 9], [4, 10],
                        [5, 5], [5, 6], [5, 7], [6, 5], [6, 7], [7, 5], [7, 6], [7, 7],
                        [8, 2], [8, 3], [8, 4], [9, 2], [9, 4], [10, 2], [10, 3], [10, 4], 
                        [8, 8], [8, 9], [8, 10], [9, 8], [9, 10], [10, 8], [10, 9], [10, 10]]

        self.n_2022 = [[1, 3], [1, 4], [1, 5], [2, 5], [3, 5], [3, 4], [3, 3], [4, 3], [5, 3], [5, 4], [5, 5],
                        [1, 7], [1, 8], [1, 9], [2, 7], [2, 9], [3, 7], [3, 9], [4, 7], [4, 9], [5, 7], [5, 8], [5, 9], 
                        [7, 3], [7, 4], [7, 5], [8, 5], [9, 3], [9, 4], [9, 5], [10, 3], [11, 3], [11, 4], [11, 5],
                        [7, 7], [7, 8], [7, 9], [8, 9], [9, 7], [9, 8], [9, 9], [10, 7], [11, 7], [11, 8], [11, 9]]

        self.n_1922 = [[7, 3], [7, 4], [7, 5], [8, 5], [9, 3], [9, 4], [9, 5], [10, 3], [11, 3], [11, 4], [11, 5],
                        [7, 7], [7, 8], [7, 9], [8, 9], [9, 7], [9, 8], [9, 9], [10, 7], [11, 7], [11, 8], [11, 9],
                        [1, 3], [1, 4], [2, 4], [3, 4], [4, 4], [5, 4], [1, 7], [1, 8], [1, 9], [2, 7], [2, 9], [3, 7], 
                        [3, 8], [3, 9], [4, 9], [5, 7], [5, 8], [5, 9]]

    def get_music(self):
        return 'static\\music\\Intro.wav'

    def start_game(self, matrix):
        matrix.disable_all_tiles(BLACK)
        pygame.mixer.music.load(self.get_music())
        pygame.mixer.music.play(1)

    def end_game(self, matrix):
        matrix.disable_all_tiles(BLACK)
        pygame.mixer.music.stop()

    def react_to_click(self, matrix, x, y):
        if self.time < 65:
            self.time += 1
            matrix.color_all(BLACK)
        else:
            if self.repeat > 30:
                self.time += 1
                self.repeat = 0
                matrix.color_all(BLACK)
            self.repeat += 1

        match self.time:
            case 1:
                matrix.color_given_tiles(self.first_sqr, c_1966_1958_1952_1929_1927_1926_1923_1922)
                matrix.color_given_tiles(self.n_1922, WHITE)
            case 2:
                matrix.color_given_tiles(self.second_sqr, c_1966_1958_1952_1929_1927_1926_1923_1922)
                matrix.color_given_tiles(self.n_1922, WHITE)
            case 3: 
                matrix.color_given_tiles(self.third_sqr, c_1935_1931_1925_1924)
                matrix.color_given_tiles(self.n_1922, WHITE)
            case 4:
                matrix.color_given_tiles(self.forth_sqr, c_1935_1931_1925_1924)
                matrix.color_given_tiles(self.n_1922, WHITE)
            case 5:
                matrix.color_given_tiles(self.fifth_sqr, c_1966_1958_1952_1929_1927_1926_1923_1922)
            case 6:
                matrix.color_given_tiles(self.sixth_sqr, c_1966_1958_1952_1929_1927_1926_1923_1922)
            case 7:
                matrix.color_column(3, c_1977_1974_1972_1969_1965_1964_1962_1961_1959_1956_1950_1949_1948_1941_1933_1928)
            case 8:
                matrix.color_column(9, c_1966_1958_1952_1929_1927_1926_1923_1922)
            case 9:
                matrix.color_given_tiles(self.first_sqr, c_1978_1976_1973_1970_1968_1967_1951_1957_1938_1937_1936_1934_1930_1932)
            case 10:
                matrix.color_given_tiles(self.second_sqr, c_1935_1931_1925_1924)
            case 11:
                matrix.color_given_tiles(self.third_sqr, c_1978_1976_1973_1970_1968_1967_1951_1957_1938_1937_1936_1934_1930_1932)
            case 12:
                matrix.color_given_tiles(self.forth_sqr, c_1977_1974_1972_1969_1965_1964_1962_1961_1959_1956_1950_1949_1948_1941_1933_1928)
            case 13:
                matrix.color_given_tiles(self.fifth_sqr, c_1977_1974_1972_1969_1965_1964_1962_1961_1959_1956_1950_1949_1948_1941_1933_1928)
            case 14:
                matrix.color_given_tiles(self.sixth_sqr, c_1978_1976_1973_1970_1968_1967_1951_1957_1938_1937_1936_1934_1930_1932)
            case 15:
                matrix.color_row(3, c_1935_1931_1925_1924)
            case 16:
                matrix.color_row(9, c_1978_1976_1973_1970_1968_1967_1951_1957_1938_1937_1936_1934_1930_1932)
                #1936
            case 17:
                matrix.color_column(1, c_1978_1976_1973_1970_1968_1967_1951_1957_1938_1937_1936_1934_1930_1932)
            case 18:
                matrix.color_column(1, c_1978_1976_1973_1970_1968_1967_1951_1957_1938_1937_1936_1934_1930_1932)
                matrix.color_column(3, c_1978_1976_1973_1970_1968_1967_1951_1957_1938_1937_1936_1934_1930_1932)
            case 19:
                matrix.color_column(1, c_1985_1984_1982_1975_1971_1963_1960_1954_1954_1953_1947_1945_1944_1943_1940_1939)
                matrix.color_column(3, c_1985_1984_1982_1975_1971_1963_1960_1954_1954_1953_1947_1945_1944_1943_1940_1939)
                matrix.color_column(5, c_1985_1984_1982_1975_1971_1963_1960_1954_1954_1953_1947_1945_1944_1943_1940_1939)
            case 20:
                matrix.color_column(1, c_1985_1984_1982_1975_1971_1963_1960_1954_1954_1953_1947_1945_1944_1943_1940_1939)
                matrix.color_column(3, c_1985_1984_1982_1975_1971_1963_1960_1954_1954_1953_1947_1945_1944_1943_1940_1939)
                matrix.color_column(5, c_1985_1984_1982_1975_1971_1963_1960_1954_1954_1953_1947_1945_1944_1943_1940_1939)
                matrix.color_column(7, c_1985_1984_1982_1975_1971_1963_1960_1954_1954_1953_1947_1945_1944_1943_1940_1939)
            case 21:
                matrix.color_column(1, c_1977_1974_1972_1969_1965_1964_1962_1961_1959_1956_1950_1949_1948_1941_1933_1928)
                matrix.color_column(3, c_1977_1974_1972_1969_1965_1964_1962_1961_1959_1956_1950_1949_1948_1941_1933_1928)
                matrix.color_column(5, c_1977_1974_1972_1969_1965_1964_1962_1961_1959_1956_1950_1949_1948_1941_1933_1928)
                matrix.color_column(7, c_1977_1974_1972_1969_1965_1964_1962_1961_1959_1956_1950_1949_1948_1941_1933_1928)
                matrix.color_column(9, c_1977_1974_1972_1969_1965_1964_1962_1961_1959_1956_1950_1949_1948_1941_1933_1928)
            case 22:
                matrix.color_column(1, c_1992_1986_1979_1955_1946_1942)
                matrix.color_column(3, c_1992_1986_1979_1955_1946_1942)
                matrix.color_column(5, c_1992_1986_1979_1955_1946_1942)
                matrix.color_column(7, c_1992_1986_1979_1955_1946_1942)
                matrix.color_column(9, c_1992_1986_1979_1955_1946_1942)
                matrix.color_column(11, c_1992_1986_1979_1955_1946_1942)
                #1942
            case 23:
                matrix.color_given_tiles(self.fifth_sqr, c_1985_1984_1982_1975_1971_1963_1960_1954_1954_1953_1947_1945_1944_1943_1940_1939)
            case 24:
                matrix.color_given_tiles(self.third_sqr, c_1985_1984_1982_1975_1971_1963_1960_1954_1954_1953_1947_1945_1944_1943_1940_1939)
            case 25:
                matrix.color_row(1, c_1985_1984_1982_1975_1971_1963_1960_1954_1954_1953_1947_1945_1944_1943_1940_1939)
            case 26:
                matrix.color_row(1, c_1992_1986_1979_1955_1946_1942)
                matrix.color_row(3, c_1992_1986_1979_1955_1946_1942)
            case 27:
                matrix.color_row(1, c_1985_1984_1982_1975_1971_1963_1960_1954_1954_1953_1947_1945_1944_1943_1940_1939)
                matrix.color_row(3, c_1985_1984_1982_1975_1971_1963_1960_1954_1954_1953_1947_1945_1944_1943_1940_1939)
                matrix.color_row(5, c_1985_1984_1982_1975_1971_1963_1960_1954_1954_1953_1947_1945_1944_1943_1940_1939)
            case 28:
                matrix.color_row(1, c_1977_1974_1972_1969_1965_1964_1962_1961_1959_1956_1950_1949_1948_1941_1933_1928)
                matrix.color_row(3, c_1977_1974_1972_1969_1965_1964_1962_1961_1959_1956_1950_1949_1948_1941_1933_1928)
                matrix.color_row(5, c_1977_1974_1972_1969_1965_1964_1962_1961_1959_1956_1950_1949_1948_1941_1933_1928)
                matrix.color_row(7, c_1977_1974_1972_1969_1965_1964_1962_1961_1959_1956_1950_1949_1948_1941_1933_1928)
            case 29:
                matrix.color_row(1, c_1977_1974_1972_1969_1965_1964_1962_1961_1959_1956_1950_1949_1948_1941_1933_1928)
                matrix.color_row(3, c_1977_1974_1972_1969_1965_1964_1962_1961_1959_1956_1950_1949_1948_1941_1933_1928)
                matrix.color_row(5, c_1977_1974_1972_1969_1965_1964_1962_1961_1959_1956_1950_1949_1948_1941_1933_1928)
                matrix.color_row(7, c_1977_1974_1972_1969_1965_1964_1962_1961_1959_1956_1950_1949_1948_1941_1933_1928)
                matrix.color_row(9, c_1977_1974_1972_1969_1965_1964_1962_1961_1959_1956_1950_1949_1948_1941_1933_1928)
            case 30:
                matrix.color_row(1, c_1977_1974_1972_1969_1965_1964_1962_1961_1959_1956_1950_1949_1948_1941_1933_1928)
                matrix.color_row(3, c_1977_1974_1972_1969_1965_1964_1962_1961_1959_1956_1950_1949_1948_1941_1933_1928)
                matrix.color_row(5, c_1977_1974_1972_1969_1965_1964_1962_1961_1959_1956_1950_1949_1948_1941_1933_1928)
                matrix.color_row(7, c_1977_1974_1972_1969_1965_1964_1962_1961_1959_1956_1950_1949_1948_1941_1933_1928)
                matrix.color_row(9, c_1977_1974_1972_1969_1965_1964_1962_1961_1959_1956_1950_1949_1948_1941_1933_1928)
                matrix.color_row(11, c_1977_1974_1972_1969_1965_1964_1962_1961_1959_1956_1950_1949_1948_1941_1933_1928)
                #1950
            case 31:
                matrix.color_given_tiles(self.fifth_sqr, c_1978_1976_1973_1970_1968_1967_1951_1957_1938_1937_1936_1934_1930_1932)
            case 32:
                matrix.color_given_tiles(self.third_sqr, c_1966_1958_1952_1929_1927_1926_1923_1922)
            case 33:
                matrix.color_random_tile(30, c_1985_1984_1982_1975_1971_1963_1960_1954_1954_1953_1947_1945_1944_1943_1940_1939)
            case 34:
                matrix.color_random_tile(30, c_1985_1984_1982_1975_1971_1963_1960_1954_1954_1953_1947_1945_1944_1943_1940_1939)
            case 35:
                matrix.color_random_tile(30, c_1992_1986_1979_1955_1946_1942)
            case 36:
                matrix.color_random_tile(30, c_1977_1974_1972_1969_1965_1964_1962_1961_1959_1956_1950_1949_1948_1941_1933_1928)
            case 37:
                matrix.color_random_tile(30, c_1978_1976_1973_1970_1968_1967_1951_1957_1938_1937_1936_1934_1930_1932)
            case 38:
                matrix.color_random_tile(30, c_1966_1958_1952_1929_1927_1926_1923_1922)
            case 39:
                matrix.color_random_tile(30, c_1977_1974_1972_1969_1965_1964_1962_1961_1959_1956_1950_1949_1948_1941_1933_1928)
                #1959
            case 40:
                matrix.color_random_tile(30, c_1985_1984_1982_1975_1971_1963_1960_1954_1954_1953_1947_1945_1944_1943_1940_1939)
            case 41:
                matrix.color_random_tile(30, c_1977_1974_1972_1969_1965_1964_1962_1961_1959_1956_1950_1949_1948_1941_1933_1928)
            case 42:
                matrix.color_random_tile(30, c_1977_1974_1972_1969_1965_1964_1962_1961_1959_1956_1950_1949_1948_1941_1933_1928)
            case 43:
                matrix.color_random_tile(30, c_1985_1984_1982_1975_1971_1963_1960_1954_1954_1953_1947_1945_1944_1943_1940_1939)
            case 44:
                matrix.color_random_tile(30, c_1977_1974_1972_1969_1965_1964_1962_1961_1959_1956_1950_1949_1948_1941_1933_1928)
            case 45:
                matrix.color_random_tile(30, c_1977_1974_1972_1969_1965_1964_1962_1961_1959_1956_1950_1949_1948_1941_1933_1928)
            case 46:
                matrix.color_random_tile(30, c_1966_1958_1952_1929_1927_1926_1923_1922)
            case 47:
                matrix.color_random_tile(30, c_1978_1976_1973_1970_1968_1967_1951_1957_1938_1937_1936_1934_1930_1932)
            case 48:
                matrix.color_random_tile(30, c_1977_1974_1972_1969_1965_1964_1962_1961_1959_1956_1950_1949_1948_1941_1933_1928)
            case 49:
                matrix.color_random_tile(30, c_1978_1976_1973_1970_1968_1967_1951_1957_1938_1937_1936_1934_1930_1932)
            case 50:
                matrix.color_random_tile(30, c_1985_1984_1982_1975_1971_1963_1960_1954_1954_1953_1947_1945_1944_1943_1940_1939)
            case 51:
                matrix.color_random_tile(30, c_1977_1974_1972_1969_1965_1964_1962_1961_1959_1956_1950_1949_1948_1941_1933_1928)
            case 52:
                matrix.color_random_tile(30, c_1978_1976_1973_1970_1968_1967_1951_1957_1938_1937_1936_1934_1930_1932)
            case 53:
                matrix.color_random_tile(30, c_1977_1974_1972_1969_1965_1964_1962_1961_1959_1956_1950_1949_1948_1941_1933_1928)
            case 54:
                matrix.color_random_tile(30, c_1985_1984_1982_1975_1971_1963_1960_1954_1954_1953_1947_1945_1944_1943_1940_1939)
            case 55:
                matrix.color_random_tile(30, c_1978_1976_1973_1970_1968_1967_1951_1957_1938_1937_1936_1934_1930_1932)
            case 56:
                matrix.color_random_tile(30, c_1977_1974_1972_1969_1965_1964_1962_1961_1959_1956_1950_1949_1948_1941_1933_1928)
            case 57:
                matrix.color_random_tile(30, c_1978_1976_1973_1970_1968_1967_1951_1957_1938_1937_1936_1934_1930_1932)
            case 58:
                matrix.color_random_tile(30, c_1992_1986_1979_1955_1946_1942)
            case 59:
                matrix.color_random_tile(30, c_1994_1993_1989_1987_1983_1980)
            case 60:
                matrix.color_random_tile(30, c_2000_1999_1996_1991_1988_1981)
            case 61:
                matrix.color_random_tile(30, c_1985_1984_1982_1975_1971_1963_1960_1954_1954_1953_1947_1945_1944_1943_1940_1939)
            case 62:
                matrix.color_random_tile(30, c_1994_1993_1989_1987_1983_1980)
            case 63:
                matrix.color_random_tile(30, c_1985_1984_1982_1975_1971_1963_1960_1954_1954_1953_1947_1945_1944_1943_1940_1939)
            case 64:
                matrix.color_random_tile(30, c_1985_1984_1982_1975_1971_1963_1960_1954_1954_1953_1947_1945_1944_1943_1940_1939)
                # 1985
            case 65:
                matrix.fade_in( c_1992_1986_1979_1955_1946_1942, self.seventh_sqr)
                matrix.fade_in( c_1992_1986_1979_1955_1946_1942, self.sixth_sqr)
            case 66:
                matrix.color_given_tiles(self.seventh_sqr, c_1992_1986_1979_1955_1946_1942)
                matrix.color_given_tiles(self.sixth_sqr, c_1992_1986_1979_1955_1946_1942)
                matrix.fade_in( c_1994_1993_1989_1987_1983_1980, self.fifth_sqr)
            case 67:
                matrix.color_given_tiles(self.seventh_sqr, c_1992_1986_1979_1955_1946_1942)
                matrix.color_given_tiles(self.sixth_sqr, c_1992_1986_1979_1955_1946_1942)
                matrix.color_given_tiles(self.fifth_sqr,  c_1994_1993_1989_1987_1983_1980)
                matrix.fade_in( c_2000_1999_1996_1991_1988_1981, self.forth_sqr)
            case 68:
                matrix.color_given_tiles(self.seventh_sqr, c_1992_1986_1979_1955_1946_1942)
                matrix.color_given_tiles(self.sixth_sqr, c_1992_1986_1979_1955_1946_1942)
                matrix.color_given_tiles(self.fifth_sqr,  c_1994_1993_1989_1987_1983_1980)
                matrix.color_given_tiles(self.forth_sqr, c_2000_1999_1996_1991_1988_1981)
                matrix.fade_in( c_1994_1993_1989_1987_1983_1980, self.third_sqr)
            case 69:
                matrix.color_given_tiles(self.seventh_sqr, c_1992_1986_1979_1955_1946_1942)
                matrix.color_given_tiles(self.sixth_sqr, c_1992_1986_1979_1955_1946_1942)
                matrix.color_given_tiles(self.fifth_sqr,  c_1994_1993_1989_1987_1983_1980)
                matrix.color_given_tiles(self.forth_sqr, c_2000_1999_1996_1991_1988_1981)
                matrix.color_given_tiles(self.third_sqr, c_1994_1993_1989_1987_1983_1980)
                matrix.fade_in( c_1997_1995_1990, self.second_sqr)
            case 70:
                matrix.color_given_tiles(self.seventh_sqr, c_1992_1986_1979_1955_1946_1942)
                matrix.color_given_tiles(self.sixth_sqr, c_1992_1986_1979_1955_1946_1942)
                matrix.color_given_tiles(self.fifth_sqr,  c_1994_1993_1989_1987_1983_1980)
                matrix.color_given_tiles(self.forth_sqr, c_2000_1999_1996_1991_1988_1981)
                matrix.color_given_tiles(self.third_sqr, c_1994_1993_1989_1987_1983_1980)
                matrix.color_given_tiles(self.second_sqr, c_1997_1995_1990)
                matrix.fade_in( c_2000_1999_1996_1991_1988_1981, self.first_sqr)
            case 71:
                matrix.fade_in_all(c_1992_1986_1979_1955_1946_1942)
            case 72:
                matrix.fade_in_all(c_1994_1993_1989_1987_1983_1980)
            case 73:
                matrix.fade_in( c_1994_1993_1989_1987_1983_1980, self.third_sqr)
                # 1994
            case 74:
                matrix.color_given_tiles(self.third_sqr, c_1994_1993_1989_1987_1983_1980)
                matrix.fade_in( c_1997_1995_1990, self.fifth_sqr)
            case 75:
                matrix.color_given_tiles(self.third_sqr, c_1994_1993_1989_1987_1983_1980)
                matrix.color_given_tiles(self.fifth_sqr, c_1997_1995_1990)
                matrix.fade_in(c_2000_1999_1996_1991_1988_1981, self.first_sqr)
            case 76:
                matrix.color_given_tiles(self.third_sqr, c_1994_1993_1989_1987_1983_1980)
                matrix.color_given_tiles(self.fifth_sqr, c_1997_1995_1990)
                matrix.color_given_tiles(self.first_sqr, c_2000_1999_1996_1991_1988_1981)
                matrix.fade_in(c_1997_1995_1990, self.sixth_sqr)
                matrix.fade_in(c_1997_1995_1990, self.seventh_sqr)
            case 77:
                matrix.color_given_tiles(self.third_sqr, c_1994_1993_1989_1987_1983_1980)
                matrix.color_given_tiles(self.fifth_sqr, c_1997_1995_1990)
                matrix.color_given_tiles(self.first_sqr, c_2000_1999_1996_1991_1988_1981)
                matrix.color_given_tiles(self.sixth_sqr, c_1997_1995_1990)
                matrix.color_given_tiles(self.seventh_sqr, c_1997_1995_1990)
                matrix.fade_in(c_2012_2011_2009_2003_2002_1998, self.second_sqr)
            case 78:
                matrix.color_given_tiles(self.third_sqr, c_1994_1993_1989_1987_1983_1980)
                matrix.color_given_tiles(self.fifth_sqr, c_1997_1995_1990)
                matrix.color_given_tiles(self.first_sqr, c_2000_1999_1996_1991_1988_1981)
                matrix.color_given_tiles(self.sixth_sqr, c_1997_1995_1990)
                matrix.color_given_tiles(self.seventh_sqr, c_1997_1995_1990)
                matrix.color_given_tiles(self.second_sqr, c_2012_2011_2009_2003_2002_1998)
                matrix.fade_in(c_2000_1999_1996_1991_1988_1981, self.forth_sqr)
            case 79:
                matrix.fade_in_all(c_2000_1999_1996_1991_1988_1981)
            case 80:
                matrix.fade_in_all(c_2008_2004_2001)
            case 81:
                matrix.fade_in(c_2012_2011_2009_2003_2002_1998, self.fifth_sqr)
                matrix.fade_in(c_2012_2011_2009_2003_2002_1998, self.third_sqr)
            case 82:
                matrix.fade_in(c_2012_2011_2009_2003_2002_1998, self.second_sqr)
            case 83:
                matrix.fade_in(c_2008_2004_2001, self.sixth_sqr)
                matrix.fade_in(c_2008_2004_2001, self.first_sqr)
            case 84:
                matrix.fade_in(c_2012_2011_2009_2003_2002_1998, self.third_sqr)
            case 85:
                matrix.fade_in(c_2012_2011_2009_2003_2002_1998, self.fifth_sqr)
                matrix.fade_in(c_2012_2011_2009_2003_2002_1998, self.second_sqr)
                #2006
            case 86:
                matrix.fade_in(c_2012_2011_2009_2003_2002_1998, self.second_sqr)
            case 87:
                matrix.fade_in(c_2008_2004_2001, self.sixth_sqr)
                matrix.fade_in(c_2008_2004_2001, self.third_sqr)
            case 88:
                matrix.fade_in(c_2012_2011_2009_2003_2002_1998, self.sixth_sqr)
            case 89:
                matrix.fade_in(c_2014_2013_2010, self.footprint)
            case 90:
                matrix.fade_in(c_2012_2011_2009_2003_2002_1998, self.second_sqr)
            case 91:
                matrix.fade_in(c_2012_2011_2009_2003_2002_1998, self.footprint)
            case 92:
                matrix.fade_in(c_2014_2013_2010, self.forth_sqr)
            case 93:
                matrix.fade_in(c_2014_2013_2010, self.footprint)
            case 94:
                matrix.fade_in(c_2020_2019_2017_2016_2015, self.first_sqr)
            case 95:
                matrix.fade_in(c_2020_2019_2017_2016_2015, self.footprint)
            case 96:
                matrix.fade_in_all(c_2020_2019_2017_2016_2015)
                matrix.fade_in(WHITE, self.n_2022)
            case 97:
                matrix.fade_in_all(c_2018)
                matrix.color_given_tiles(self.n_2022, WHITE)
            case 98:
                matrix.fade_in_all(c_2020_2019_2017_2016_2015)
                matrix.color_given_tiles(self.n_2022, WHITE)
            case 99:
                matrix.fade_in_all(c_2020_2019_2017_2016_2015)
                matrix.color_given_tiles(self.n_2022, WHITE)
            
            case default:
                matrix.fade_in_all(c_2021)
                matrix.color_given_tiles(self.n_2022, WHITE)


    def react_to_unclick(self, matrix, x, y):
        pass

    def react_to_standing(self, matrix, x, y):
        pass







    

