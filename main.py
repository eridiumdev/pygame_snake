import framework.game
import framework.window
import game as _game
import config


def main():
    window = framework.window.Window(
        title=config.WINDOW_TITLE,
        width=config.WINDOW_WIDTH,
        height=config.WINDOW_HEIGHT,
    )
    game = _game.Game(
        window=window,
        fps=config.GAME_FPS,
    )
    game.run()


if __name__ == '__main__':
    main()
