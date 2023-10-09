import time

def focus_timer(work_minutes=25, break_minutes=5):
    work_seconds = work_minutes * 60
    break_seconds = break_minutes * 60

    while True:
        # 工作时间
        print(f"工作时间，专注倒计时：{work_minutes}分钟")
        time.sleep(work_seconds)
        print("时间到！请休息一下。")

        # 休息时间
        print(f"休息时间，休息倒计时：{break_minutes}分钟")
        time.sleep(break_seconds)
        print("休息结束！请开始下一轮工作。")

if __name__ == "__main__":
    focus_timer()
