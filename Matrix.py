from Tile import Tile

class Matrix:

    def __init__(self):
        self.length = 13

        # Main matrix initiation
        self.tiles = [[0 for x in range(self.length)] for y in range(self.length)]

        # Tile( controller_address, port_index )
        #                    0             1             2             3             4             5             6             7             8             9             10           11            12
        self.tiles[0] = [Tile(1,   0), Tile(2,   1), Tile(3,   0), Tile(4,   1), Tile(5,   0), Tile(6,   1), Tile(7,   0), Tile(8,   1), Tile(9,   0), Tile(10,  1), Tile(11,  0), Tile(12,  1), Tile(13,  0)]
        self.tiles[1] = [Tile(14,  0), Tile(15,  1), Tile(16,  0), Tile(17,  1), Tile(18,  0), Tile(19,  1), Tile(20,  0), Tile(21,  1), Tile(22,  0), Tile(23,  1), Tile(24,  0), Tile(25,  1), Tile(26,  0)]
        self.tiles[2] = [Tile(27,  0), Tile(28,  1), Tile(29,  0), Tile(30,  1), Tile(31,  0), Tile(32,  1), Tile(33,  0), Tile(34,  1), Tile(35,  0), Tile(36,  1), Tile(37,  0), Tile(38,  1), Tile(39,  0)]
        self.tiles[3] = [Tile(40,  0), Tile(41,  1), Tile(42,  0), Tile(43,  1), Tile(44,  0), Tile(45,  1), Tile(46,  0), Tile(47,  1), Tile(48,  0), Tile(49,  1), Tile(50,  0), Tile(51,  1), Tile(52,  0)]
        self.tiles[4] = [Tile(53,  0), Tile(54,  1), Tile(55,  0), Tile(56,  1), Tile(57,  0), Tile(58,  1), Tile(59,  0), Tile(60,  1), Tile(61,  0), Tile(62,  1), Tile(63,  0), Tile(64,  1), Tile(65,  0)]
        self.tiles[5] = [Tile(66,  0), Tile(67,  1), Tile(68,  0), Tile(69,  1), Tile(70,  0), Tile(71,  1), Tile(72,  0), Tile(73,  1), Tile(74,  0), Tile(75,  1), Tile(76,  0), Tile(77,  1), Tile(78,  0)]
        self.tiles[6] = [Tile(79,  0), Tile(80,  1), Tile(81,  0), Tile(82,  1), Tile(83,  0), Tile(84,  1), Tile(85,  0), Tile(86,  1), Tile(87,  0), Tile(88,  1), Tile(89,  0), Tile(90,  1), Tile(91,  0)]
        self.tiles[7] = [Tile(92,  0), Tile(93,  1), Tile(94,  0), Tile(95,  1), Tile(96,  0), Tile(97,  1), Tile(98,  0), Tile(99,  1), Tile(100, 0), Tile(101, 1), Tile(102, 0), Tile(103, 1), Tile(104, 0)]
        self.tiles[8] = [Tile(105, 0), Tile(106, 1), Tile(107, 0), Tile(108, 1), Tile(109, 0), Tile(110, 1), Tile(111, 0), Tile(112, 1), Tile(113, 0), Tile(114, 1), Tile(115, 0), Tile(116, 1), Tile(117, 0)]
        self.tiles[9] = [Tile(118, 0), Tile(119, 1), Tile(120, 0), Tile(121, 1), Tile(122, 0), Tile(123, 1), Tile(124, 0), Tile(125, 1), Tile(126, 0), Tile(127, 1), Tile(128, 0), Tile(129, 1), Tile(130, 0)]
        self.tiles[10] =[Tile(131, 0), Tile(132, 1), Tile(133, 0), Tile(134, 1), Tile(135, 0), Tile(136, 1), Tile(137, 0), Tile(138, 1), Tile(139, 0), Tile(140, 1), Tile(141, 0), Tile(142, 1), Tile(143, 0)]
        self.tiles[11] =[Tile(144, 0), Tile(145, 1), Tile(146, 0), Tile(147, 1), Tile(148, 0), Tile(149, 1), Tile(150, 0), Tile(151, 1), Tile(152, 0), Tile(153, 1), Tile(154, 0), Tile(155, 1), Tile(156, 0)]
        self.tiles[12] =[Tile(157, 0), Tile(158, 1), Tile(159, 0), Tile(160, 1), Tile(161, 0), Tile(162, 1), Tile(163, 0), Tile(164, 1), Tile(165, 0), Tile(166, 1), Tile(167, 0), Tile(168, 1), Tile(169, 0)]


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



