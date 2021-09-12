import framework.game
import framework.window
import game as _game


def main():
    window = framework.window.Window(
        title='Snek',
        width=600,
        height=400,
    )
    game = _game.Game(
        window=window,
        fps=60,
    )
    game.run()


if __name__ == '__main__':
    main()
