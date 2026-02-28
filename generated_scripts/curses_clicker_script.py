#!/usr/bin/env python3
import curses, random, time

EMOJIS = [
    r"""
    ʕ•ᴥ•ʔ 
    """,
    r"""
    (Ò_Ó)
    """,
    r"""
    (╯°□°)╯︵ ┻━┻
    """,
    r"""
    (ﾉ◕ヮ◕)ﾉ*: ･ﾟ
    """,
    r"""
    (ﾉ^_^)ﾉ
    """,
    r"""
    ʕ•ᴥ•ʔ 
    """
]

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    stdscr.clear(); stdscr.refresh()

    last_x = last_y = None
    cooldown = 0

    while True:
        try:
            k = stdscr.getch()
        except KeyboardInterrupt:
            break

        if k == curses.KEY_MOUSE:
            _, x, y, _, _ = curses.getmouse()
            if last_x is not None and (x != last_x or y != last_y):
                if cooldown <= 0:
                    cooldown = 12
                    e = random.choice(EMOJIS).strip()
                    stdscr.attron(curses.color_pair(1))
                    stdscr.addstr(y-1, max(0, x - len(e)//2), e)
                    stdscr.attroff(curses.color_pair(1))
                    stdscr.refresh()
            last_x, last_y = x, y
        else:
            cooldown = max(0, cooldown - 1)
            if cooldown == 0:
                stdscr.clear(); stdscr.refresh()

        time.sleep(0.04)

curses.wrapper(main)