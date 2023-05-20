import time

def focus_timer(duration):
    start_time = time.time()
    end_time = start_time + duration

    while time.time() < end_time:
        remaining_time = end_time - time.time()
        minutes = int(remaining_time / 60)
        seconds = int(remaining_time % 60)

        print(f"Remaining time: {minutes:02d}:{seconds:02d}")
        time.sleep(1)

    print("Focus timer completed!")

# 设置专注时间为30分钟（1800秒）
focus_timer(1800)
