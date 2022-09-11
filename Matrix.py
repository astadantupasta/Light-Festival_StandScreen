from Tile import Tile
import pygame

class Matrix:

    def __init__(self):
        self.length = 13

        a2 = pygame.mixer.Sound("static\\piano\\a2.wav")
        a3 = pygame.mixer.Sound("static\\piano\\a3.wav")
        a4 = pygame.mixer.Sound("static\\piano\\a4.wav")
        a5 = pygame.mixer.Sound("static\\piano\\a5.wav")
        a6 = pygame.mixer.Sound("static\\piano\\a6.wav")
        b2 = pygame.mixer.Sound("static\\piano\\b2.wav")
        b3 = pygame.mixer.Sound("static\\piano\\b3.wav")
        b4 = pygame.mixer.Sound("static\\piano\\b4.wav")
        b5 = pygame.mixer.Sound("static\\piano\\b5.wav")
        b6 = pygame.mixer.Sound("static\\piano\\b6.wav")
        c2 = pygame.mixer.Sound("static\\piano\\c2.wav")
        c3 = pygame.mixer.Sound("static\\piano\\c3.wav")
        c4 = pygame.mixer.Sound("static\\piano\\c4.wav")
        c5 = pygame.mixer.Sound("static\\piano\\c5.wav")
        c6 = pygame.mixer.Sound("static\\piano\\c6.wav")
        d2 = pygame.mixer.Sound("static\\piano\\d2.wav")
        d3 = pygame.mixer.Sound("static\\piano\\d3.wav")
        d4 = pygame.mixer.Sound("static\\piano\\d4.wav")
        d5 = pygame.mixer.Sound("static\\piano\\d5.wav")
        d6 = pygame.mixer.Sound("static\\piano\\d6.wav")
        e2 = pygame.mixer.Sound("static\\piano\\e2.wav")
        e3 = pygame.mixer.Sound("static\\piano\\e3.wav")
        e4 = pygame.mixer.Sound("static\\piano\\e4.wav")
        e5 = pygame.mixer.Sound("static\\piano\\e5.wav")
        e6 = pygame.mixer.Sound("static\\piano\\e6.wav")
        f2 = pygame.mixer.Sound("static\\piano\\f2.wav")
        f3 = pygame.mixer.Sound("static\\piano\\f3.wav")
        f4 = pygame.mixer.Sound("static\\piano\\f4.wav")
        f5 = pygame.mixer.Sound("static\\piano\\f5.wav")
        f6 = pygame.mixer.Sound("static\\piano\\f6.wav")
        g2 = pygame.mixer.Sound("static\\piano\\g2.wav")
        g3 = pygame.mixer.Sound("static\\piano\\g3.wav")
        g4 = pygame.mixer.Sound("static\\piano\\g4.wav")
        g5 = pygame.mixer.Sound("static\\piano\\g5.wav")
        g6 = pygame.mixer.Sound("static\\piano\\g6.wav")

        # Main matrix initiation
        self.tiles = [[0 for x in range(self.length)] for y in range(self.length)]

        # Tile( controller_address, port_index, sound )
        #                     0                 1                 2                 3                 4                 5                 6                 7                 8                 9                 10                11                12
        self.tiles[0] = [Tile(1,   0, a2), Tile(2,   1, b2), Tile(3,   0, c2), Tile(4,   1, d2), Tile(5,   0, e2), Tile(6,   1, f2), Tile(7,   0, g2), Tile(8,   1, a3), Tile(9,   0, b3), Tile(10,  1, c3), Tile(11,  0, d3), Tile(12,  1, e3), Tile(13,  0, f3)]
        self.tiles[1] = [Tile(14,  0, g3), Tile(15,  1, a4), Tile(16,  0, b4), Tile(17,  1, c4), Tile(18,  0, d4), Tile(19,  1, e4), Tile(20,  0, f4), Tile(21,  1, g4), Tile(22,  0, a5), Tile(23,  1, b5), Tile(24,  0, c5), Tile(25,  1, d5), Tile(26,  0, e5)]
        self.tiles[2] = [Tile(27,  0, f5), Tile(28,  1, g5), Tile(29,  0, a6), Tile(30,  1, b6), Tile(31,  0, c6), Tile(32,  1, d6), Tile(33,  0, e6), Tile(34,  1, f6), Tile(35,  0, g6), Tile(36,  1, a2), Tile(37,  0, b2), Tile(38,  1, c2), Tile(39,  0, d2)]
        self.tiles[3] = [Tile(40,  0, e2), Tile(41,  1, f2), Tile(42,  0, g2), Tile(43,  1, a3), Tile(44,  0, b3), Tile(45,  1, c3), Tile(46,  0, d3), Tile(47,  1, e3), Tile(48,  0, f3), Tile(49,  1, g3), Tile(50,  0, a4), Tile(51,  1, b4), Tile(52,  0, d4)]
        self.tiles[4] = [Tile(53,  0, e4), Tile(54,  1, f4), Tile(55,  0, g4), Tile(56,  1, a5), Tile(57,  0, b5), Tile(58,  1, c5), Tile(59,  0, d5), Tile(60,  1, e5), Tile(61,  0, f5), Tile(62,  1, g5), Tile(63,  0, a6), Tile(64,  1, b6), Tile(65,  0, c6)]
        self.tiles[5] = [Tile(66,  0, d6), Tile(67,  1, e6), Tile(68,  0, f6), Tile(69,  1, g6), Tile(70,  0, a2), Tile(71,  1, b2), Tile(72,  0, c2), Tile(73,  1, d2), Tile(74,  0, e2), Tile(75,  1, f2), Tile(76,  0, g2), Tile(77,  1, a3), Tile(78,  0, b3)]
        self.tiles[6] = [Tile(79,  0, c3), Tile(80,  1, d3), Tile(81,  0, e3), Tile(82,  1, f3), Tile(83,  0, g3), Tile(84,  1, a4), Tile(85,  0, b4), Tile(86,  1, c4), Tile(87,  0, d4), Tile(88,  1, e4), Tile(89,  0, f4), Tile(90,  1, g4), Tile(91,  0, a5)]
        self.tiles[7] = [Tile(92,  0, b5), Tile(93,  1, c5), Tile(94,  0, d5), Tile(95,  1, e5), Tile(96,  0, f5), Tile(97,  1, g5), Tile(98,  0, a6), Tile(99,  1, b6), Tile(100, 0, c6), Tile(101, 1, d6), Tile(102, 0, e6), Tile(103, 1, f6), Tile(104, 0, g6)]
        self.tiles[8] = [Tile(105, 0, a2), Tile(106, 1, b2), Tile(107, 0, c2), Tile(108, 1, d2), Tile(109, 0, e2), Tile(110, 1, f2), Tile(111, 0, g2), Tile(112, 1, a3), Tile(113, 0, b3), Tile(114, 1, c3), Tile(115, 0, d3), Tile(116, 1, e3), Tile(117, 0, f3)]
        self.tiles[9] = [Tile(118, 0, g3), Tile(119, 1, a4), Tile(120, 0, b4), Tile(121, 1, c4), Tile(122, 0, d4), Tile(123, 1, e4), Tile(124, 0, f4), Tile(125, 1, g4), Tile(126, 0, a5), Tile(127, 1, b5), Tile(128, 0, c5), Tile(129, 1, d5), Tile(130, 0, e5)]
        self.tiles[10] =[Tile(131, 0, f5), Tile(132, 1, g5), Tile(133, 0, a6), Tile(134, 1, b6), Tile(135, 0, c6), Tile(136, 1, d6), Tile(137, 0, e6), Tile(138, 1, f6), Tile(139, 0, g6), Tile(140, 1, a2), Tile(141, 0, b2), Tile(142, 1, c2), Tile(143, 0, d2)]
        self.tiles[11] =[Tile(144, 0, e2), Tile(145, 1, f2), Tile(146, 0, g2), Tile(147, 1, a3), Tile(148, 0, b3), Tile(149, 1, c3), Tile(150, 0, d3), Tile(151, 1, e3), Tile(152, 0, f3), Tile(153, 1, g3), Tile(154, 0, a4), Tile(155, 1, b4), Tile(156, 0, c4)]
        self.tiles[12] =[Tile(157, 0, d4), Tile(158, 1, e4), Tile(159, 0, f4), Tile(160, 1, g4), Tile(161, 0, a5), Tile(162, 1, b5), Tile(163, 0, c5), Tile(164, 1, d5), Tile(165, 0, e5), Tile(166, 1, f5), Tile(167, 0, g5), Tile(168, 1, a6), Tile(169, 0, b6)]


    def get_tile(self, x, y):
        return self.tiles[x][y] 

    def enable_all_tiles(self, color):
        for x in range(self.length):
            for y in range(self.length):
                self.tiles[x][y].enable(color)

    def disable_all_tiles(self, color):
        for x in range(self.length):
            for y in range(self.length):
                self.tiles[x][y].disable(color)



