from pywinauto import Desktop  # type: ignore


def get_all_windows():
    windows = Desktop(backend="uia").windows()

    result = []

    for w in windows:
        result.append(w)

    return result


def get_all_windows_with_text(text: str):
    windows = get_all_windows()

    result = []

    for w in windows:
        if text.lower() in w.window_text().lower():
            result.append(w)

    return result


def main():
    windows = get_all_windows_with_text("PowerShell")
    for w in windows:
        w.set_focus()
        w.capture_as_image().save("screenshot.png")


if __name__ == "__main__":
    main()
