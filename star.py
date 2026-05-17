def draw_pyramid(total_rows, num_star=1):
    print(" " * (total_rows - num_star) + "* " * num_star)

    if num_star < total_rows:
        num_star += 1
        draw_pyramid(total_rows, num_star)
    else:
        print(f"Done pyramid with {total_rows} * base")

draw_pyramid(int(input("How many is the base star? ")))
