import curses
import time

menu = ['Student','Cource','Mark','Exit']

def print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    for idx, row in enumerate(menu):
    x = w//2 - len(row)//2
    y = h//2 - len(menu)//2 + idx
    if idx == selected_row_idx:
        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(y, x, row)
        stdscr.attroff(curses.color_pair(1))
    else:
        stdscr.addstr(y, x, row)
    stdscr.refresh()
    time.sleep(3)

def main(stdscr):
    curses.set_curs(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curent_row_idx = 0
    print_menu(stdscr, curent_row_idx)

    while 1:
        key = stdscr.getch()
        stdscr.clear()
        if key ==curses.Key_up and curent_row_idx > 0:
            curent_row_idx -= 1
        elif key ==curses.Key_down and curent_row_idx < len(menu)-1:
            curent_row_idx += 1
        elif key == curses.Key_enter or key in [10, 13]:
            stdscr.clear()
            stdscr.addstr(0, 0, "You pressed {}".format(menu[curent_row_idx]))
            stdscr.refresh()
            if curent_row_idx == len(menu)-1:
                break

        print_menu(stdscr, curent_row_idx)
        stdscr.refresh()


curses.wrapper(print_menu)