import numpy as np
import pygame as pg


class Matrix:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        points = N * M
        zeros_value = int(30 * (points / 100))
        ones_value = points - zeros_value
        line = [int(i) for i in np.concatenate((np.zeros(zeros_value), np.ones(ones_value)))]
        np.random.shuffle(line)
        self.matrix = np.reshape(line, (N, M))


class CityGrid:
    def __init__(self, N, M):
        self.net = Matrix(N, M)
        self.RES = self.WIDTH, HEIGHT = 1000, 700
        self.coating = 30
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode(self.RES)
        self.surface = pg.Surface(self.RES)

    def draw(self):
        self.surface.fill(pg.Color('black'))
        self.screen.blit(self.surface, (0, 0))
        pg.draw.line(self.screen, pg.Color('yellow'), (960, 50), (960, 650), 4)
        pg.draw.line(self.screen, pg.Color('yellow'), (680, 50), (680, 650), 4)
        pg.draw.line(self.screen, pg.Color('yellow'), (680, 50), (960, 50), 4)
        pg.draw.line(self.screen, pg.Color('yellow'), (680, 650), (960, 650), 4)

    def draw_grid(self):
        left_margin = 40
        upper_margin = 50
        cm = self.net.matrix
        if cm.N > cm.M:
            block_size = 600 // cm.N
        else:
            block_size = 600 // cm.M

        for x in range(len(cm)):
            for y in range(len(cm[x])):
                pg.draw.rect(self.screen, pg.Color(254, 249, 19),
                             ((left_margin + block_size * x) - 3,
                              (upper_margin + block_size * y) - 3,
                              block_size + 3, block_size + 3), 3)
                if cm[x][y] == 0:
                    pg.draw.rect(self.screen, pg.Color(178, 176, 173),
                                 (left_margin + block_size * x, upper_margin + block_size * y,
                                  block_size - 3, block_size - 3))
                if cm[x][y] == 1:
                    pg.draw.rect(self.screen, pg.Color(227, 207, 137),
                                 (left_margin + block_size * x, upper_margin + block_size * y,
                                  block_size - 3, block_size - 3))

    def run(self):
        pg.display.set_caption("Симуляция покрытия")
        while True:
            self.draw()
            for i in pg.event.get():
                if i.type == pg.QUIT:
                    exit()
            # pg.display.flip()
            self.draw_grid()
            pg.display.update()
            self.clock.tick(30)


if __name__ == '__main__':
    app = CityGrid(5, 5)
    app.run()
