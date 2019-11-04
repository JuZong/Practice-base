import psutil


def kill():
    video_player_component = "QyPlayer.exe"
    iqiyi_windows_client = "QyClient.exe"
    video_helper_program = "QyFragment.exe"
    iqiyi_video_helper = "QyKernel.exe"
    video_platform_services = "QiyiService.exe"

    processes = [video_player_component, iqiyi_windows_client, video_helper_program, iqiyi_video_helper,
                 video_platform_services]
    for proc in psutil.process_iter():
        # check whether the process name matches
        if proc.name() in processes:
            proc.kill()
            processes.remove(proc.name())
        if len(processes) == 0:
            break


if __name__ == "__main__":
    kill()
